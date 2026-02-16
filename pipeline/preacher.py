from pathlib import Path
from PIL import Image
import logging
from time import localtime, strftime
import json
import random
from typing import Optional
import re
import os 
import fitz # PyMuPDF
from llms import GPT4, DepictQA, GPT4_AZ, GEMINI,QWEN
from . import prompts
from utils.slides import create_ppt_style_image, get_specific_element
from utils.logger import get_logger
from utils.custom_types import *
from utils.textwork import merge_dict_keys_values, classify_response, text_to_list, extract_code,replace_animate,extract_dict,extract_list_from_text, _load_json_dict
from utils                                                                                                                                                .videowork import extract_key_frames, merge_video_audio, image_to_images, image_to_video, concatenate_videos
from utils.math_vis import render_video
from moviepy.editor import VideoFileClip
from tools import Wanxiang_video, Wanxiang_image, Qwentts
from utils.misc import download_file, name_to_pdb_ids, download_pdb
from utils.mol import generate_mol_animation
from tools.retriever import PaperRetriever
from tools.renderer import SlideRenderer
import random
import json

class Preacher:
    """
    Args:
        input_path (Path): Path to the input image.
        output_dir (Path): Path to the output directory, in which a directory will be created.
        llm_config_path (Path, optional): Path to the config file of LLM. Defaults to Path("config.yml").
        plan_by (str, optional): The method of degradation evaluation, "depictqa" or "gpt4v". Defaults to "depictqa".
        with_retrieval (bool, optional): Whether to schedule with retrieval. Defaults to True.
        schedule_example_path (Path | None, optional): Path to the example hub. Defaults to Path( "memory/schedule_example.json").
        with_reflection (bool, optional): Whether to reflect on the results of tools. Defaults to True.
        eval_by (str, optional): The method of reflection on results of tools, "depictqa" or "gpt4v". Defaults to "depictqa".
        with_rollback (bool, optional): Whether to roll back when failing in one subtask. Defaults to True.
        silent (bool, optional): Whether to suppress the console output. Defaults to False.
    """

    def __init__(
        self,
        input_path: Path,
        output_dir: Path,
        llm_config_path: Path ,
        plan_by: str,
        eval_by: str,
        art_work: str,
        with_example: bool = True,
        schedule_example_path: Optional[Path] = Path(
            "memory/schedule_example.json"
        ),
        with_reflection: bool = True,
        with_rollback: bool = True,
        silent: bool = False,
        max_high_plan_iteration: int = 15,
        max_low_plan_iteration: int = 30,
        max_generate_iteration: int = 10,
        general_video_work: str = "wanx",
        captioning_work: str = "wanx",
        slides_work: str = "xinghuo",
        audio_work: str = "qwentts",
    ) -> None:
        # paths
        self.pdf_path = input_path
        self.low_plan_order = ["style","audio_content","source","prompt"]
        self._prepare_dir(input_path, output_dir)
        # config
        self._config(
            plan_by,
            with_example,
            with_reflection,
            eval_by,
            with_rollback,
            max_high_plan_iteration,
            max_low_plan_iteration,
            max_generate_iteration,
            art_work,
            general_video_work,
            captioning_work,
            slides_work,
            audio_work,
        )
        # components
        self._create_components(llm_config_path, schedule_example_path, silent)
        # constants
        self._set_constants()

    def _config(
        self,
        plan_by: str,
        with_example: bool,
        with_reflection: bool,
        eval_by: str,
        with_rollback: bool,
        max_low_plan_iteration:int,
        max_high_plan_iteration:int,
        max_generate_iteration:int,
        art_work: str,
        general_video_tool: str ,
        captioning_tool: str  ,
        slides_tool: str ,
        audio_tool: str ,
    ) -> None:
        #assert plan_by in {"GPT4v", "depictqa", "GPT4_AZ", "GEMINI"}
        self.plan_by = plan_by
        self.with_example = with_example
        
        self.eval_by = eval_by
        #assert eval_by in {"GPT4v", "depictqa", "GPT4_AZ", "GEMINI"}
        self.art_work = art_work
        self.with_reflection = with_reflection
        
        self.with_rollback = with_rollback
        self.max_high_plan_iteration=max_high_plan_iteration
        self.max_low_plan_iteration=max_low_plan_iteration
        
        self.general_video_tool = general_video_tool
        self.captioning_tool= captioning_tool
        self.slides_tool = slides_tool
        self.audio_tool = audio_tool
        self.max_generate_iteration =max_generate_iteration

    def _create_components(
        self,
        llm_config_path: Path,
        schedule_example_path: Optional[Path],
        silent: bool,
    ) -> None:
        # logger
        self.qa_logger = get_logger(
            logger_name="QA",
            log_file=self.qa_path,
            console_log_level=logging.WARNING,
            file_format_str="%(message)s",
            silent=silent,
        )
        workflow_format_str = "%(asctime)s - %(levelname)s\n%(message)s\n"
        self.workflow_logger: logging.Logger = get_logger(
            logger_name="Workflow",
            log_file=self.workflow_path,
            console_format_str=workflow_format_str,
            file_format_str=workflow_format_str,
            silent=silent,
        )

        # LLM
        if self.plan_by == "GPT4v":
            self.planner = GPT4(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.plan_by == "depictqa" or self.eval_by == "depictqa":
            self.planner = DepictQA(logger=self.qa_logger, silent=silent)
        elif self.plan_by == "GPT4_AZ":
            self.planner = GPT4_AZ(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.plan_by == "GEMINI":
            self.planner = GEMINI(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.plan_by == "QWEN":
            self.planner = QWEN(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        
        # LLM evaluator
        if self.eval_by == "GPT4v":
            self.evaluator = GPT4(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.eval_by == "depictqa" :
            self.evaluator = DepictQA(logger=self.qa_logger, silent=silent)
        elif self.eval_by== "GPT4_AZ":
            self.evaluator = GPT4_AZ(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.eval_by == "GEMINI":
            self.evaluator = GEMINI(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.eval_by == "QWEN":
            self.evaluator = QWEN(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        #Generator
        if self.art_work == "GPT4_AZ":
            self.art_agent = GPT4_AZ(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.art_work == "GEMINI":
            self.art_agent = GEMINI(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        elif self.art_work == "QWEN":
            self.art_agent = QWEN(
                config_path=llm_config_path,
                logger=self.qa_logger,
                silent=silent,
                system_message=prompts.system_message,
            )
        if self.audio_tool== "qwentts":
            self.audio_tool = Qwentts(config_path=llm_config_path)
        if self.general_video_tool == "wanx":
            self.general_video_tool = Wanxiang_video(config_path=llm_config_path)
        if self.captioning_tool == "wanx":
            self.captioning_tool = Wanxiang_image(config_path=llm_config_path)

        # SlideRenderer
        try:
            self.slide_renderer = SlideRenderer(self.work_dir, self.pdf_path, tts_engine=self.audio_tool)
        except Exception as e:
            self.workflow_logger.warning(f"Failed to initialize SlideRenderer: {e}")
            self.slide_renderer = None

        
        # Retriever & Style DB
        try:
            # Check for pre-computed index in data_reference first
            data_ref_index = Path("data_reference/paper_index")
            legacy_index = Path("output/test_index")
            
            if data_ref_index.exists():
                index_path = data_ref_index
                self.workflow_logger.info(f"Using pre-computed index at {index_path}")
            elif legacy_index.exists():
                index_path = legacy_index
                self.workflow_logger.info(f"Using legacy index at {index_path}")
            else:
                # Fallback: try to build from dataset if no index found
                self.workflow_logger.info("No index found. Attempting to build from 'dataset' directory...")
                index_path = legacy_index # Default save location for auto-build
                source_dir = Path("dataset")
                if source_dir.exists():
                    temp_retriever = PaperRetriever(logger=self.workflow_logger)
                    try:
                        temp_retriever.build_from_dir(source_dir, save_path=index_path)
                        self.workflow_logger.info("Index built successfully.")
                    except Exception as e:
                         self.workflow_logger.error(f"Failed to build index: {e}")
                else:
                     self.workflow_logger.warning("'dataset' directory not found. Cannot build index.")

            self.retriever = PaperRetriever(index_path=index_path)
            
            self.style_db = {}
            style_db_path = Path("data_reference/style_db/db_summary.json")
            if style_db_path.exists():
                with open(style_db_path, "r") as f:
                    summary = json.load(f)
                    for item in summary:
                        self.style_db[item["video_id"]] = item["path"]
            else:
                self.workflow_logger.warning("Style DB not found. Retrieval will be limited.")
        except Exception as e:
            self.workflow_logger.warning(f"Failed to init retrieval: {e}")


        # example
        if self.with_example:
            assert (
                schedule_example_path is not None
            ), "Example should be provided."
            with open(schedule_example_path, "r") as f:
                examples = json.load(f)
            self.high_example = examples["high_examples"]
            self.low_example = examples["low_examples"]
            self.manim_example = examples["MANIM_examples"]
        random.seed(0)

    def retrieve_global_style(self) -> str:
        """
        Retrieve context for high-level planning.
        """
        context = []
        try:
            # 1. Retrieve similar papers
            similar_papers = self.retriever.retrieve_similar_papers(pdf_path=self.pdf_path, k=3)
            self.workflow_logger.info(f"Retrieved {len(similar_papers)} papers. Type of first: {type(similar_papers[0]) if similar_papers else 'None'}")
            
            context.append("## Similar Papers found in specific domain:")
            for p in similar_papers:
                if isinstance(p, dict):
                    context.append(f"- {p.get('title', 'Unknown')}")
                else:
                    self.workflow_logger.warning(f"Unexpected item type in retrieval: {type(p)}")
                    context.append(f"- {str(p)}")
                
            # 2. Retrieve style examples (placeholder logic for now)
            # Find if we have video style for any of these
            style_matches = []
            for p in similar_papers:
                pdf_stem = Path(p['path']).stem
                if pdf_stem in self.style_db:
                    style_matches.append(pdf_stem)
                else:
                    raise KeyError(f"Retrieved paper '{pdf_stem}' not found in style_db. FAISS index and style DB are out of sync.")
            
           
            total_slides = 0
            if style_matches:
                context.append("\n## Reference Presentation Styles (from existing videos):")
                for vid_id in style_matches:
                    path = self.style_db[vid_id]
                    meta_path = Path(path) / "metadata.json"
                    if meta_path.exists():
                        with open(meta_path, "r") as f:
                            meta = json.load(f)
                            slides_cnt = len(meta.get("slides", []))
                            total_slides += slides_cnt
                            avg_builds = sum(len(s.get("builds", [])) for s in meta.get("slides", [])) / max(1, slides_cnt)
                            context.append(f"- Video '{vid_id}': approx {slides_cnt} slides, {avg_builds:.1f} builds/slide.")
                
                if len(style_matches) > 0:
                    avg_scenes = int(total_slides / len(style_matches))
                    
                    # Adjust based on PDF content length (heuristic)
                    try:
                        doc = fitz.open(self.pdf_path)
                        text_len = sum(len(p.get_text()) for p in doc)
                        page_count = len(doc)
                        
                        # Heuristic: ~2 scenes per page of dense text, or 1 scene per 1000 chars?
                        # Let's say baseline is 1 scene per 1.5 pages
                        content_estimated_scenes = max(5, int(page_count / 1.5))
                        
                        # Weighted average: 70% content, 30% style reference
                        final_scenes = int(0.7 * content_estimated_scenes + 0.3 * avg_scenes)
                        context.append(f"\nRECOMMENDATION: Target approximately {final_scenes} scenes (Calculated from {page_count} pages of content and reference styles).")
                    except Exception as e:
                         self.workflow_logger.warning(f"Failed to analyze PDF content for planning: {e}")
                         context.append(f"\nRECOMMENDATION: Target approximately {avg_scenes} scenes (Based on reference styles).")

        except Exception as e:
            self.workflow_logger.warning(f"Global retrieval failed: {e}")
            
        return "\n".join(context)

    def retrieve_scene_style(self, scene_plan: dict) -> str:
        """
        Retrieve context for low-level planning (scene specific).
        Dynamically selects a reference style/layout based on scene content keywords.
        """
        scene_desc = f"{scene_plan.get('SCENE', '')} {scene_plan.get('DESCRIPTION', '')} {scene_plan.get('summary', '')}".lower()
        
        advice = []
        
        # 1. Content Analysis -> Layout Suggestion
        if any(w in scene_desc for w in ['result', 'performance', 'accuracy', 'table', 'chart', 'graph']):
             advice.append("Detected 'Results' content: Consider a 'full_fig_with_callouts' or 'two_row_charts' layout. Use builds to highlight specific data points or rows in the table.")
        elif any(w in scene_desc for w in ['method', 'architecture', 'model', 'diagram', 'pipeline']):
             advice.append("Detected 'Methodology' content: Consider a 'full_fig_with_callouts' layout to show the pipeline. Use builds to trace the data flow through the model.")
        elif any(w in scene_desc for w in ['intro', 'motivation', 'problem', 'challenge']):
             advice.append("Detected 'Motivation' content: Consider a 'two_col_fig_right' layout. Use bullet points on the left to state the problem, with an illustrative figure on the right.")
        elif any(w in scene_desc for w in ['code', 'algorithm', 'pseudocode']):
             advice.append("Detected 'Algorithm' content: Use a 'code_snippet' layout. Use builds to highlight lines of code as they are explained.")
        else:
             advice.append("General Content: Default to 'two_col_bullets_left' if a figure is available, otherwise 'one_col_bullets'.")

        # 2. Retrieve Reference Layout (from similar papers/videos if available)
        # Placeholder: If we had a granular slide DB, we would query it here.
        # For now, we inject general "Best Practices" for scientific videography.
        advice.append("\nReference Best Practices:")
        advice.append("- Avoid wall-of-text. Max 3-4 bullets per slide.")
        advice.append("- Sync visual appearance with audio keywords.")
        advice.append("- Keep it simple. One key idea per slide.")
        
        return "\n".join(advice)

    def _set_constants(self) -> None:
        self.degra_subtask_dict: dict[Degradation, Subtask] = {
            "low resolution": "super-resolution",
            "noise": "denoising",
            "motion blur": "motion deblurring",
            "defocus blur": "defocus deblurring",
            "haze": "dehazing",
            "rain": "deraining",
            "dark": "brightening",
            "jpeg compression artifact": "jpeg compression artifact removal",
        }
        self.subtask_degra_dict: dict[Subtask, Degradation] = {
            v: k for k, v in self.degra_subtask_dict.items()
        }
        self.degradations = set(self.degra_subtask_dict.keys())
        self.subtasks = set(self.degra_subtask_dict.values())
        self.levels: list[Level] = ["very low", "low", "medium", "high", "very high"]
        
    def _ensure_audio(self, content: str, return_url=False) -> Path:
        target = self.curr_scene_dir / "audio.wav"
        if target.exists():
            return target
        url = self.audio_tool.return_audio(content)
        if return_url:
            return url 
        return Path(download_file(url, target)) 
    def run(self, high_plan: Optional[list[Subtask]]=None) -> None:
        # 1. High Planning
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 1: High-level planning...")
        self.workflow_logger.info("=" * 50)

        if high_plan is not None:
            self.workflow_logger.info(f"Loading pre-generated high plan from {high_plan}")
            with open(high_plan, 'r') as file:
                self.high_plan = file.read()
        elif self.high_plan_path.exists():
            self.workflow_logger.info(f"High plan already cached at {self.high_plan_path}. Loading...")
            with open(self.high_plan_path, 'r') as file:
                self.high_plan = file.read()
        else:
            self.high_plan = self.high_planning()

        # 2. Parse High Plan
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 2: Parsing high-level plan...")
        self.workflow_logger.info("=" * 50)

        self.high_plan_list = _load_json_dict(self.high_plan)

        # Handle double-serialized cache: json.dump wraps a string in quotes
        if self.high_plan_list is None or isinstance(self.high_plan_list, str):
            try:
                unwrapped = json.loads(self.high_plan) if isinstance(self.high_plan, str) else self.high_plan
                self.high_plan_list = _load_json_dict(unwrapped)
            except Exception:
                pass

        # Handle dict-wrapped plans (e.g. {"scenes": [...]})
        if isinstance(self.high_plan_list, dict):
            for v in self.high_plan_list.values():
                if isinstance(v, list):
                    self.high_plan_list = v
                    break

        if not isinstance(self.high_plan_list, list):
            raise ValueError(f"High plan parsing failed: expected list, got {type(self.high_plan_list)}. Raw: {str(self.high_plan)[:200]}")

        self.workflow_logger.info(f"Parsed {len(self.high_plan_list)} scenes from high plan.")

        # 3. Low Planning
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 3: Low-level planning...")
        self.workflow_logger.info("=" * 50)

        self.final_plan = []
        for i in range(len(self.high_plan_list)):
            self.final_plan.append({})
            self.scene_idx = i
            self.low_planning(self.high_plan_list[i])

        # 4. Video Generation
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 4: Generating scene videos...")
        self.workflow_logger.info("=" * 50)

        # Clean up previous scene outputs so videos are always regenerated
        import shutil
        for i in range(len(self.high_plan_list)):
            scene_dir = self.work_dir / f"scene_{i}"
            if scene_dir.exists():
                self.workflow_logger.info(f"Removing previous scene directory: {scene_dir}")
                shutil.rmtree(scene_dir)

        self.video_list = []
        for i in range(len(self.high_plan_list)):
            self.scene_idx = i
            self.workflow_logger.info(f"Generating scene {i}...")
            self.generate_(i)

            video_path = self.work_dir / f"scene_{i}" / f"scene{i}.mp4"
            if video_path.exists():
                self.workflow_logger.info(f"Scene {i} video generated at {video_path}")
                self.video_list.append(video_path)
            else:
                self.workflow_logger.error(f"Scene {i} video NOT found at {video_path}")

        # 5. Concatenation
        self.workflow_logger.info("=" * 50)
        self.workflow_logger.info("Step 5: Concatenating final video...")
        self.workflow_logger.info("=" * 50)

        if not self.video_list:
            raise RuntimeError("No scene videos were generated. Cannot concatenate.")

        concatenate_videos(self.video_list, self.final_video_path_)
        self.workflow_logger.info(f"Final video saved at {self.final_video_path_}")


    def high_planning(self) -> str: # Changed return type to str
        """Sets the initial plan."""

        style_context = self.retrieve_global_style()
        if self.with_reflection:
            high_planning_success=False
            iter=0
            eval_results=None
            high_plan=None
            while high_planning_success == False and (iter < self.max_high_plan_iteration):
                high_plan = self.high_plan_by_llm(style_context, eval_results, high_plan)
                high_plan_legal = self.setting_plan_format(high_plan,step="high")
                high_planning_success, eval_results = self.high_evaluate_by_llm(high_plan_legal)
                iter += 1
        else:
            high_plan = self.high_plan_by_llm(style_context)
            high_plan_legal = self.setting_plan_format(high_plan, step="high")
        self.workflow_logger.info(f"High Level Plan: {high_plan_legal}")
        # with open(self.high_plan_path, 'w') as file:
        #     file.write(high_plan_legal)
        with open(self.high_plan_path, 'w', encoding='utf-8') as f:
            json.dump(high_plan_legal, f, ensure_ascii=False, indent=2)
        return high_plan_legal
    
    def high_plan_by_llm(self, style_context, eval_results=None, high_plan=None) -> str:
        if eval_results:
            prompt = high_plan + ' \n '+ prompts.high_level_replanning_prompt + eval_results + ' \n ' + style_context
        else:
            # Inject style context into the placeholder
            # Note: prompts.high_level_planning_prompt has {style_context} placeholder now
            try:
                base_prompt = prompts.high_level_planning_prompt.format(style_context=style_context)
            except Exception as e:
                 # Fallback if format fails (e.g. if prompt doesn't have placeholder or has other braces)
                 self.workflow_logger.warning(f"Formatting failed: {e}")
                 base_prompt = prompts.high_level_planning_prompt + "\n\n" + style_context

            prompt = base_prompt
            if self.with_example :
                prompt += ' \n '+ merge_dict_keys_values(self.high_example) 
        high_plan = eval(
            self.planner(
                prompt=prompt,
                pdf_path=Path(self.pdf_path),
            )
        )
        self.workflow_logger.info(f"High_plan: {high_plan}")
        return  high_plan
    
    def high_evaluate_by_llm(self, high_plan) -> str:
        prompt = prompts.high_level_evaluate_prompt + ' \n '+ high_plan
        eval_results = eval(
            self.evaluator(
                prompt = prompt,
                pdf_path=Path(self.pdf_path),
                ))
        success = classify_response(eval_results)
        self.workflow_logger.info(f"Eval_Results: {eval_results}")
        return success, eval_results
    
    def low_planning(self, part_plan):
        plan_file = self.log_dir/f"file_{self.scene_idx}.json"
        # Check if plan file already exists - if so, load and skip planning
        if os.path.exists(plan_file):
            self.workflow_logger.info(f"Scene {self.scene_idx}: Low plan already exists at {plan_file}. Skipping generation.")
            with open(plan_file, "r") as file:
                self.final_plan[self.scene_idx] = json.load(file)
                return None
        
        self.workflow_logger.info(f"Scene {self.scene_idx}: No cached plan found. Generating low-level plan...")
        # Initialize with high-level info
        self.final_plan[self.scene_idx] = part_plan.copy()
        
        style_advice = self.retrieve_scene_style(part_plan)
        eval_results = None
        low_plan_str = None
        
        if self.with_reflection:
            low_planning_success = False
            iter = 0
            while not low_planning_success and iter < self.max_low_plan_iteration:
                low_plan_str = self.low_plan_by_llm(part_plan, style_advice, eval_results, low_plan_str)
                parsed_low_plan = _load_json_dict(low_plan_str)
                if parsed_low_plan and isinstance(parsed_low_plan, dict):
                    low_planning_success, eval_results = self.low_evaluate_by_llm(low_plan_str)
                else:
                    eval_results = f"Output was not valid JSON. Please output ONLY valid JSON, no markdown fences."
                iter += 1
        else:
            low_plan_str = self.low_plan_by_llm(part_plan, style_advice)
        
        # Parse and merge final result
        parsed_low_plan = _load_json_dict(low_plan_str)
        if parsed_low_plan and isinstance(parsed_low_plan, dict):
            self.final_plan[self.scene_idx].update(parsed_low_plan)
        else:
            raise ValueError(f"Failed to parse low plan for scene {self.scene_idx} after all attempts. Raw output: {low_plan_str[:200]}")
        
        # Save the complete plan
        with open(plan_file, "w") as file:
            json.dump(self.final_plan[self.scene_idx], file, indent=4)
    
    def low_plan_by_llm(self, part_plan, style_advice, eval_results=None, low_plan_str=None) -> str:
        if eval_results:
            prompt = low_plan_str + ' \n ' + prompts.low_level_replanning_prompt + eval_results + ' \n ' + style_advice
        else:
            try:
                prompt = prompts.low_level_planning_prompt.format(
                    scene_json=json.dumps(part_plan, indent=2), 
                    style_advice=style_advice
                )
            except Exception as e:
                self.workflow_logger.warning(f"Prompt formatting failed: {e}")
                prompt = prompts.low_level_planning_prompt + "\nInput: " + str(part_plan)

            if self.with_example:
                prompt += ' \n ' + merge_dict_keys_values(self.low_example)
             
        low_plan = eval(
            self.planner(
                prompt=prompt,
                pdf_path=Path(self.pdf_path),
            )
        )
        self.workflow_logger.info(f"Low_plan scene {self.scene_idx}: {low_plan}")
        return low_plan
    
    def low_evaluate_by_llm(self, low_plan_str) -> tuple:
        prompt = prompts.low_level_evaluate_prompt + ' \n ' + low_plan_str
        eval_results = eval(
            self.evaluator(
                prompt=prompt,
                pdf_path=Path(self.pdf_path),
            )
        )
        success = classify_response(eval_results)
        self.workflow_logger.info(f"Low eval scene {self.scene_idx}: {eval_results}")
        return success, eval_results
    
    def generate_(self, scene_idx):
        self.curr_scene_dir = self.work_dir / "scene_{}".format(scene_idx)
        if not os.path.isdir(self.curr_scene_dir):
            self.curr_scene_dir.mkdir()
        style = self.final_plan[scene_idx]["style"].lower()
        if "general" in style.lower() :
            video_path=self.general_work(scene_idx)
        elif "prof" in style.lower() or "scie" in style.lower() or "math" in style.lower() or "mol" in style.lower():
            video_path=self.professional_work(scene_idx)
        elif "cap" in style.lower():
            video_path=self.captioning_work(scene_idx)
        elif "slides" in style.lower():
            if hasattr(self, 'slide_renderer') and self.slide_renderer:
                try:
                    video_path = self.slide_renderer.render_scene(self.final_plan[scene_idx], scene_idx)
                except Exception as e:
                    self.workflow_logger.error(f"SlideRenderer failed: {e}. Falling back to legacy slides_work.")
                    video_path=self.slides_work(scene_idx)
            else:
                video_path=self.slides_work(scene_idx)
        else: print("error: Please check the style file")
        return video_path

    def math_single_work(self, plan, eval_results=None, code_str=None):
        eval_prompt = "Please check if the above code follows the rules mentioned. If not, modify it: "+\
            "The first line should be 'def animate(self):\n'; the last line should be in the format 'self.wait(X)', where X is a positive integer;"+\
                " does the code have a strong mathematical nature? Does it align with theme {}? Directly output the modified code (Code should be easy). Error message:".format(plan["prompt"])
        if eval_results==None:
            prompt = " Please write a python function named animate at the letf-bottom part in the bottom left corner of the screen about {}. ".format(plan["source"])+\
                "The requirements are: "+\
                "Use the MANIM package function should be part of the Scene class in MANIM , NO NEED TO IMPORT package"+\
                "The first line SHOULD be 'def animate(self):\n '; the last line should be in the format 'self.wait(X)'"+\
                " The function product visual content such as intuitive function graphs."+\
                " Should conform to {} and {}.".format(plan["source"], plan["prompt"]) +\
                " Only output the function defnition code. Example:"
            prompt_r = "Rewrite this promptso as A WHOLE sentence to make it fits as acaption in a video. Keep the word with around 5 words perline"+\
                " using \"\n\" to separate lines. JUST A MEANINGFUL sentence!"
            plan["prompt"] = eval(
                self.art_agent(
                    prompt=prompt_r+"\n" + plan["prompt"],
                ))
            code_str = eval(
                self.art_agent(
                    prompt=prompt+self.manim_example,
                    pdf_path=Path(self.pdf_path),
                    ))
        else:
            code_str = eval(
                self.art_agent(
                    prompt=  eval_results+ "\n"+code_str,
                    pdf_path=Path(self.pdf_path),
                    ))
        code_str = eval(
                self.art_agent(
                    prompt=prompts.pro_format_prompt+"\n" + code_str,
                    ))
        code_str = extract_code(code_str)
        video_path = None
        while video_path == None:
            try:
                replace_animate(self.animate_path, code_str)
                print("CHECKING CODE-2")
                video_path = render_video(self.curr_scene_dir,plan)
                print("CHECKING CODE-3")
            except Exception as e:
                error_msg = str(e)  # Capture the actual error message
                code_str = eval(
                self.evaluator(
                    prompt= code_str+ "\n"+ eval_prompt + f"\nError message: {error_msg}",
                ))
                code_str = eval(
                    self.evaluator(
                prompt=prompts.pro_format_prompt+"\n" + code_str,
                ))
                code_str = extract_code(code_str)
        return code_str, video_path
    
    def professional_work(self, scene_idx):
        video_success = False
        iter=0
        plan = self.final_plan[scene_idx]
        code_str = None
        eval_results = None
        
        self.curr_video_path = self.curr_scene_dir/"video.mp4"
        
        style_ = eval(
            self.evaluator(prompt=prompts.pro_classify_prompt+plan["prompt"],))
        if "math" in style_.lower():
            if os.path.exists(self.curr_video_path):
                  pass
            else:
                while video_success == False and iter < self.max_generate_iteration:
                    code_str, video_path = self.math_single_work(plan,eval_results,code_str)
                    video_success, eval_results = self.video_evaluate_by_mllm(plan, video_path, type='video')
                    iter += 1
                video = VideoFileClip(video_path)
                video.write_videofile(str(self.curr_video_path))
        elif "mol" in style_.lower():
            if os.path.exists(self.curr_video_path):
                pass
            else:
                
                prompt_mol = f'Please return the most related name  "X" of the protein in {plan["source"]} and {plan["prompt"]}. Keep it concise and breif."+" Return the name ONLY'
                
                pdb_name = eval(
                    self.evaluator(
                    prompt=prompt_mol,))
                audio_mol = f'Optimize the {plan["audio_content"]} to transform it into an introduction related to molecular biology, mentioning the protein {pdb_name}, without exceeding 50 words. Return the UPDATED prompt ONLY'
                self.final_plan[scene_idx]["audio_content"] = eval(
                    self.evaluator(
                    prompt=audio_mol,))
                #pdb_name = _load_json_dict(pdb_name)['name']
                ids = name_to_pdb_ids(pdb_name)
                if not ids:
                    print("[MANUAL] no PDB ID, please check:", pdb_name)
                    return
                pdb_id=ids[0]
                pdb_path = os.path.join(self.curr_scene_dir, f"{pdb_id.lower()}.pdb")
                if not os.path.exists(pdb_path):
                    download_pdb(pdb_id, pdb_path)
                if pdb_path:
                    print(f"[DONE] {pdb_id} is saved at  {pdb_path}")
                    generate_mol_animation(pdb_path, self.curr_video_path)
                else:
                    url = f"https://files.rcsb.org/download/{pdb_id.upper()}.pdb"
                    print(f"[MANUAL] please download and generate by yourself:{url}")
                    
                #video = VideoFileClip(self.curr_video_path)
                #video.write_videofile(self.curr_video_path)
        self.curr_audio_path = self._ensure_audio(self.final_plan[scene_idx]["audio_content"])
        self.final_video_path = self.curr_scene_dir/"scene{}.mp4".format(scene_idx)
        if "time_cost" in plan:
            time = plan["time_cost"]
        else:
            time = '8'
        merge_video_audio(self.curr_video_path, self.curr_audio_path, time,self.final_video_path)
        return self.final_video_path

    def general_single_work(self, plan, eval_results=None):
        if eval_results==None:
            prompt_r = " Please use {} as the materials to depict a video scene that a diffusion model can understand and generate.".format( plan["prompt"])
            plan["prompt"] = eval(
            self.art_agent(
                    prompt=prompt_r+ "\n" + plan["prompt"],
            ))
        else:
            plan["prompt"] = eval(
            self.art_agent(
                    prompt=eval_results + "\n" + plan["prompt"],
            ))
        video_url = self.general_video_tool.query(plan["prompt"])
        return video_url
    
    def general_work(self, scene_idx):
        video_success = False
        iter=0
        plan = self.final_plan[scene_idx]
        eval_results = None
        self.final_video_path = self.curr_scene_dir/"scene{}.mp4".format(scene_idx)
        self.curr_video_path = self.curr_scene_dir/"video.mp4".format(scene_idx)
        self.curr_audio_path = self._ensure_audio(plan["audio_content"])
        if os.path.exists(self.curr_video_path):
            video_path=self.curr_video_path
            pass
        else:
            while video_success == False and iter < self.max_generate_iteration:
                video_path = self.curr_scene_dir/"test{}.mp4".format(iter)
                if not os.path.exists(video_path):
                    video_url = self.general_single_work(plan, eval_results)
                    video_path = download_file(video_url, video_path)
                video_success, eval_results = self.video_evaluate_by_mllm(plan, video_path, type='video')
                iter += 1
        if "time_cost" in plan:
            time = plan["time_cost"]
        else:
            time = '8'
        merge_video_audio(video_path, self.curr_audio_path, time, self.final_video_path)
        return self.final_video_path
    
    def captioning_single_work(self, plan, eval_results=None):
        if eval_results==None:
            prompt_r = " Please use {} and {} as the materials to depict a image scene that a diffusion model can understand and generate. Return the prompt ONLY".format(plan.get("scenario", ""), plan["prompt"])
            plan["prompt"] = eval(
            self.art_agent(
                    prompt=prompt_r+ "\n" + plan["prompt"],
            ))
        else:
            plan["prompt"] = eval(
            self.art_agent(
                    prompt=eval_results + "\n" + "\n" +"Please provide new prompt to depict a image scene. Be relative to" +  plan["prompt"]+ "Return the prompt ONLY.",
            ))
        image_url= self.captioning_tool.query(plan["prompt"])
        return image_url
    
    def captioning_work(self, scene_idx):
        video_success = False
        iter=0
        plan = self.final_plan[scene_idx]
        eval_results = None
        
        self.curr_image_path = self.curr_scene_dir/"image.png"
        self.curr_audio_path = self._ensure_audio(plan["audio_content"])
        if os.path.exists(self.curr_image_path):
            pass
        else:
            while video_success == False and iter < self.max_generate_iteration:
                image_path = self.curr_scene_dir/"test{}.png".format(iter)
                if not os.path.exists(image_path):
                    image_url = self.captioning_single_work(plan, eval_results)
                    image_path = download_file(image_url, image_path)
                video_success, eval_results = self.video_evaluate_by_mllm(plan, [image_path], type='image')
                iter += 1
            with Image.open(image_path) as img:
                img.save(self.curr_image_path)
        
        self.final_video_path = self.curr_scene_dir/"scene{}.mp4".format(scene_idx)
        if "time_cost" in plan:
            time = plan["time_cost"]
        else:
            time = '8'
        image_to_video(self.curr_image_path, self.curr_audio_path, time, self.final_video_path)
        return self.final_video_path


    
    def slides_single_work(self, scene_idx, plan, image_path, eval_results=None):
        if eval_results==None and (os.path.exists(image_path) is False):
            prompt_r = (
                f"Please return the type and index of the {plan['source']} in the PDF "
                "with the dict: {'type': TABLE/IMAGE, 'number': INT}"
                "where a is TABLE or IMAGE, and b is its index."
            )
            crop_dict = eval(
            self.planner(
                prompt=prompt_r,
                pdf_path=Path(self.pdf_path),
            ))
            result = _load_json_dict(crop_dict)
            # LLM may return a list of dicts; take the first element
            if isinstance(result, list):
                result = result[0] if result else {"type": "IMAGE", "number": 1}
            image_path = get_specific_element(self.pdf_path, result['type'], result['number'], image_path)
            
        else:
            if not eval_results:
                eval_results = ''
            # Fallback to summary if prompt is missing
            old_prompt = plan.get('prompt', plan.get('summary', ''))
            self.final_plan[scene_idx]["prompt"] = eval(
            self.planner(
                prompt= 'With this reason'+ eval_results+"Provide a better prompt"+eval_results+"\n Old prompt is"+old_prompt +"\n RETURN new prompt ***ONLY***",
                pdf_path=Path(self.pdf_path),
            ))

        return image_path
        
    def slides_work(self, scene_idx):
        video_success = False
        iter=0
        image_path =  self.curr_scene_dir/"image{}.png".format(iter)
        plan = self.final_plan[scene_idx]
        eval_results = None
        self.final_video_path = self.curr_scene_dir/"scene{}.mp4".format(scene_idx)
        if os.path.exists(self.final_video_path):
            return self.final_video_path
        self.curr_image_path = self.curr_scene_dir/"image.png"
        self.curr_audio_path = self._ensure_audio(plan["audio_content"])
        if os.path.exists(self.curr_image_path):
            image_path = self.curr_image_path
            pass
        else:
            while video_success == False and iter < self.max_generate_iteration:
                image_path = self.curr_scene_dir/"image{}.png".format(0)
                self.slides_single_work(scene_idx, plan, image_path, eval_results)
                video_success, eval_results = self.video_evaluate_by_mllm(plan, [image_path], type='image') 
                iter += 1
            #with Image.open(self.curr_image_path) as img:
                #img.save(self.curr_image_path)
            self.curr_image_path = create_ppt_style_image(image_path, plan.get('prompt', ''), self.curr_image_path)
        
        if "time_cost" in plan:
            time = plan["time_cost"]
        else:
            time = '8'
        image_to_video(self.curr_image_path, self.curr_audio_path, time, self.final_video_path)
        return self.final_video_path
        
    def video_evaluate_by_mllm(self, plan, video_path, type='video'):
        if type=='video':
            img_list = extract_key_frames(video_path)
        elif type=='image':
            img_list = image_to_images(video_path)
        else:
            img_list = None
        if "general" in plan["style"].lower():
            prompt_e = plan["prompt"] + ' \n '+ prompts.gen_vis_eval
        elif "professional" in plan["style"].lower():
            prompt_e =  plan["scenario"] + ' \n '+   plan["prompt"] + ' \n '+ prompts.pro_vis_eval 
        elif "captioning" in plan["style"].lower():
            prompt_e = prompts.gen_vis_eval
        elif "slides" in plan["style"].lower():
            # Use summary or audio_content as the text to evaluate against since 'prompt' is missing for slides
            text_desc = plan.get('summary', plan.get('audio_content', ''))
            prompt_e = prompts.slides_vis_eval + text_desc
        else: print("error: Please check the style file of"+plan["scenario"])
        eval_results = eval(
            self.evaluator(
                prompt = prompt_e,
                img_path=img_list,
                ))
        success = classify_response(eval_results)
        return success, eval_results
    
    def setting_plan_format(self, plan, step="low"):
        # Deprecated: Now we rely on strict JSON prompting
        # But high_planning still uses logic that expects a string return
        return plan


    def _prepare_dir(self, input_path, output_dir) -> None:

        pdf_name = input_path.stem
        self.input_path = input_path
        self.work_dir = output_dir / pdf_name
        if not os.path.isdir(self.work_dir):
            self.work_dir.mkdir(parents=True)

        self.log_dir = self.work_dir / "logs"
        if not os.path.isdir(self.log_dir):
            self.log_dir.mkdir()
        self.qa_path = self.log_dir / "llm_qa.md"
        self.workflow_path = self.log_dir / "workflow.log"
        self.high_plan_path = self.log_dir / "highplan.txt"
        self.final_video_path_= self.log_dir / "final_video.mp4"
        self.animate_path =  Path("utils/math_vis.py").resolve()
        #self.plan_path = self.log_dir


    # def tolist(self, high_plan: str) -> list:
    #     if self.plan_by=='GEMINI':
    #         return text_to_list(high_plan)

