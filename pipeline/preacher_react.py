from pathlib import Path
from PIL import Image
import yaml
import logging
from time import localtime, strftime
import json
import random
from typing import Optional
import re
import os 
import fitz # PyMuPDF
import sys
from llms import GPT4, DepictQA, GPT4_AZ, GEMINI,QWEN
from . import prompts_react as prompts
from utils.slides import create_ppt_style_image, get_specific_element
from utils.logger import get_logger, Tee
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
from tools.logo_manager import format_authors_display, format_affiliations_display, format_authors_with_superscripts
from tools.asset_analyser import AssetAnalyser

class PreacherReAct:
    """ReAct-based orchestration agent for creating academic video summaries."""

    def __init__(
        self,
        input_path: Path,
        output_dir: Path,
        llm_config_path: Path,
        plan_by: str,
        eval_by: str,
        art_work: str,
        with_example: bool = True,
        schedule_example_path: Optional[Path] = Path("memory/schedule_example.json"),
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
        self.pdf_path = input_path
        self._prepare_dir(input_path, output_dir)
        
        # Configuration
        self._config(
            plan_by, with_example, with_reflection, eval_by, with_rollback,
            max_low_plan_iteration, max_high_plan_iteration, max_generate_iteration,
            art_work, general_video_work, captioning_work, slides_work, audio_work
        )
        
        # Initialize components and services
        self._create_components(llm_config_path, schedule_example_path, silent)
        self._set_constants()
        
        # Shared State for ReAct Agent
        self.shared_state = {
            "metadata": {},
            "high_plan": [],
            "past_scenes_content": [], # List of content dicts for context sliding window
            "current_scene_idx": 0,
            "total_scenes": 0,
            "final_video_path": str(self.final_video_path_)
        }
        
        # Redirect stdout and stderr to a log file
        self.terminal_log_path = self.log_dir / "terminal.log"
        sys.stdout = Tee(str(self.terminal_log_path), sys.stdout)
        sys.stderr = Tee(str(self.terminal_log_path), sys.stderr)

    # --- Initialization Methods ---
    def _config(self, plan_by, with_example, with_reflection, eval_by, with_rollback, max_low_plan_iteration, max_high_plan_iteration, max_generate_iteration, art_work, general_video_tool, captioning_tool, slides_tool, audio_tool):
        self.plan_by = plan_by
        self.with_example = with_example
        self.eval_by = eval_by
        self.art_work = art_work
        self.with_reflection = with_reflection
        self.with_rollback = with_rollback
        self.max_high_plan_iteration = max_high_plan_iteration
        self.max_low_plan_iteration = max_low_plan_iteration
        self.general_video_tool = general_video_tool
        self.captioning_tool = captioning_tool
        self.slides_tool = slides_tool
        self.audio_tool = audio_tool
        self.max_generate_iteration = max_generate_iteration

    def _prepare_dir(self, input_path, output_dir):
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
        self.high_plan_path = self.log_dir / "highplan.json"
        self.final_video_path_= self.log_dir / "final_video.mp4"
        self.animate_path =  Path("utils/math_vis.py").resolve()

    def _create_components(self, llm_config_path, schedule_example_path, silent):
        with open(llm_config_path, "r", encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)

        self.qa_logger = get_logger(
            logger_name="QA",
            log_file=self.qa_path,
            console_log_level=logging.WARNING,
            file_format_str="%(message)s",
            silent=silent,
        )
        workflow_format_str = "%(asctime)s - %(levelname)s\n%(message)s\n"
        self.workflow_logger = get_logger(
            logger_name="Workflow",
            log_file=self.workflow_path,
            console_format_str=workflow_format_str,
            file_format_str=workflow_format_str,
            silent=silent,
        )

        # Initialize LLM Planners based on self.plan_by
        if self.plan_by == "GEMINI":
            self.planner = GEMINI(config_path=llm_config_path, logger=self.qa_logger, silent=silent, system_message=prompts.system_message)
        elif self.plan_by == "GPT4v":
            self.planner = GPT4(config_path=llm_config_path, logger=self.qa_logger, silent=silent, system_message=prompts.system_message)
        elif self.plan_by == "GPT4_AZ":
            self.planner = GPT4_AZ(config_path=llm_config_path, logger=self.qa_logger, silent=silent, system_message=prompts.system_message)
        elif self.plan_by == "QWEN":
             self.planner = QWEN(config_path=llm_config_path, logger=self.qa_logger, silent=silent, system_message=prompts.system_message)
        else:
            self.planner = DepictQA(logger=self.qa_logger, silent=silent)
            
        # Mock Evaluator and Art Agent initialization for brevity, identically configured...
        self.evaluator = self.planner
        self.art_agent = self.planner
        
        if self.audio_tool == "qwentts":
            self.audio_tool_client = Qwentts(config_path=llm_config_path)
            
        try:
            self.slide_renderer = SlideRenderer(self.work_dir, self.pdf_path, tts_engine=self.audio_tool_client)
        except Exception as e:
            self.workflow_logger.warning(f"Failed to initialize SlideRenderer: {e}")
            self.slide_renderer = None

        self.asset_analyser = AssetAnalyser(self.work_dir, self.pdf_path, self.planner, self.workflow_logger)
        
        # Retrieval setup...
        try:
            openai_global_index = Path("data_reference/faiss/global")
            data_ref_index = Path("data_reference/paper_index")
            if openai_global_index.exists():
                self.retriever = PaperRetriever(index_path=openai_global_index, use_openai=True)
            elif data_ref_index.exists():
                self.retriever = PaperRetriever(index_path=data_ref_index, use_openai=False)
            else:
                 self.retriever = PaperRetriever(logger=self.workflow_logger)
                 
            self.retrieval_top_k = self.cfg.get("GEMINI", {}).get("retrieval_top_k", 5)
            self.style_db = {}
            style_db_path = Path("data_reference/style_db_refined_final/db_summary.json")
            if style_db_path.exists():
                with open(style_db_path, "r") as f:
                    summary = json.load(f)
                    for item in summary:
                        self.style_db[item["video_id"]] = item["path"]
        except Exception as e:
            self.workflow_logger.warning(f"Failed to init retrieval: {e}")

        if self.with_example:
            with open(schedule_example_path, "r") as f:
                examples = json.load(f)
            self.high_example = examples["high_examples"]
            self.low_example = examples["low_examples"]
            self.manim_example = examples["MANIM_examples"]
        random.seed(0)

    def _set_constants(self):
        pass

    def _safe_get(self, data: Any, key: str, default: Any = None) -> Any:
        """Safely gets a value from a dictionary, handling non-dict types."""
        if isinstance(data, dict):
            return data.get(key, default)
        self.workflow_logger.warning(f"Attempted to .get('{key}') from non-dict object of type {type(data)}: {str(data)[:100]}")
        return default

    # --- ReAct Global Loop ---
    def run(self):
        self.workflow_logger.info("Starting ReAct Orchestration Pipeline")
        
        # Tools definitions for prompt
        tools_str = ["ExtractMetadataTool", "GenerateHighLevelPlanTool", "BuildTitleSceneTool", "ProcessLowLevelSceneTool", "RenderSceneTool", "MergeVideosTool"]
        
        history = ""
        max_steps = 50
        step = 0
        
        prompt_template = prompts.react_global_orchestrator_prompt.replace("{tools}", ", ".join(tools_str))
        
        while step < max_steps:
            prompt = prompt_template.replace("{history}", history)
            response = self.planner(prompt=prompt, pdf_path=Path(self.pdf_path))
            self.workflow_logger.info(f"ReAct Agent Response:\n{response}")
            
            history += f"\nAgent:\n{response}\n"
            
            # Parse ReAct Action
            match = re.search(r"Action:\s*(.*?)\s*(?:\n|$)Action Input:\s*(.*)", response, re.DOTALL | re.IGNORECASE)
            if match:
                action = match.group(1).strip().strip("`").strip()
                action_input_str = match.group(2).split("Observation:")[0].strip()
                # Remove trailing quotes, backticks, or other non-JSON artifacts that LLMs sometimes append
                while action_input_str and not action_input_str[-1] in ('}', ']'):
                    action_input_str = action_input_str[:-1].strip()
                
                # Robust extraction using helper
                action_input = _load_json_dict(action_input_str)
                if not isinstance(action_input, dict):
                    # Fallback to fuzzy extraction
                    try:
                        action_input = extract_dict(response)
                    except:
                        action_input = {}
                
                if not isinstance(action_input, dict):
                    action_input = {}
                
                self.workflow_logger.info(f"Executing Action: {action} with input {action_input}")
                
                # Execute Tool
                try:
                    observation = self._execute_tool(action, action_input)
                except Exception as e:
                    observation = f"Error executing tool {action}: {str(e)}"
                    self.workflow_logger.error(observation)
                
                history += f"\nObservation: {observation}\n"
                step += 1
            else:
                if "Final Answer:" in response:
                    final_answer = response.split("Final Answer:")[1].strip()
                    self.workflow_logger.info(f"Pipeline Completed: {final_answer}")
                    break
                else:
                    self.workflow_logger.error("ReAct Loop Error: No Action or Final Answer found.")
                    break

        if step >= max_steps:
            self.workflow_logger.warning("ReAct Loop reached maximum iterations limit.")

    def _execute_tool(self, tool_name: str, parameters: Any) -> str:
        """Dispatcher for tool execution."""
        if not isinstance(parameters, dict):
            parameters = {}
            
        if tool_name == "ExtractMetadataTool":
            return self.tool_extract_metadata()
        elif tool_name == "GenerateHighLevelPlanTool":
            return self.tool_generate_high_level_plan()
        elif tool_name == "BuildTitleSceneTool":
            return self.tool_build_title_scene()
        elif tool_name == "ProcessLowLevelSceneTool":
            scene_idx = self._safe_get(parameters, "scene_idx", self._safe_get(parameters, "scene_index", self._safe_get(parameters, "scene_id", 0)))
            try:
                scene_idx = int(scene_idx)
            except (ValueError, TypeError):
                scene_idx = 0
            return self.tool_process_low_level_scene(scene_idx)
        elif tool_name == "RenderSceneTool":
            scene_idx = self._safe_get(parameters, "scene_idx", self._safe_get(parameters, "scene_index", self._safe_get(parameters, "scene_id", 0)))
            try:
                scene_idx = int(scene_idx)
            except (ValueError, TypeError):
                scene_idx = 0
            return self.tool_render_scene(scene_idx)
        elif tool_name == "MergeVideosTool":
            return self.tool_merge_videos()
        else:
            return f"Unknown tool: {tool_name}"

    # --- Tool Implementations ---
    
    def tool_extract_metadata(self) -> str:
        """Extracts title, authors, etc. via LLM prompt."""
        self.workflow_logger.info(f"Running ExtractMetadataTool...")
        cache_path = self.log_dir / "title_metadata.json"
        if cache_path.exists():
            with open(cache_path, "r") as f:
                self.shared_state["metadata"] = json.load(f)
            return "Metadata loaded from cache."

        raw = self.planner(prompt=prompts.title_extraction_prompt, pdf_path=Path(self.pdf_path))
        metadata = _load_json_dict(raw)
        if not isinstance(metadata, dict):
            # Fallback
            metadata = {
                "paper_title": Path(self.pdf_path).stem,
                "authors": [],
                "affiliations": [],
                "venue": ""
            }
        
        # Ensure paper_title is a string and clean
        paper_title = self._safe_get(metadata, "paper_title", Path(self.pdf_path).stem)
        if not isinstance(paper_title, str):
            paper_title = str(paper_title)
        
        # Merge back to shared state safely
        if not isinstance(self.shared_state["metadata"], dict):
            self.shared_state["metadata"] = {}
        self.shared_state["metadata"].update(metadata)
        with open(cache_path, "w") as f:
            json.dump(metadata, f, indent=4)
        return f"Metadata extracted: {paper_title}"

    def tool_generate_high_level_plan(self) -> str:
        """ReAct implementation: Instead of grouping everything, generates iterative high-level scenes."""
        self.workflow_logger.info(f"Running GenerateHighLevelPlanTool...")
        
        # For this version, we stick to the one-shot generation prompt to maintain stability with the base logic,
        # but we parse it into the shared state. Advanced iterative one-by-one is left as an optimization if this fails.
        style_context = self.retrieve_global_style()
        prompt = prompts.high_level_planning_prompt.format(
            style_context=style_context,
            video_assets_context=""
        )
        
        if self.high_plan_path.exists():
            with open(self.high_plan_path, 'r') as file:
                self.shared_state["high_plan"] = json.load(file)
            self.shared_state["total_scenes"] = len(self.shared_state["high_plan"])
            return f"High plan loaded from cache. Generated {self.shared_state['total_scenes']} scenes."

        raw = self.planner(prompt=prompt, pdf_path=Path(self.pdf_path))
        parsed = _load_json_dict(raw)
        
        if isinstance(parsed, dict):
            for v in parsed.values():
                if isinstance(v, list):
                    parsed = v
                    break

        self.shared_state["high_plan"] = parsed
        self.shared_state["total_scenes"] = len(parsed)
        
        with open(self.high_plan_path, 'w', encoding='utf-8') as f:
            json.dump(parsed, f, ensure_ascii=False, indent=2)
            
        return f"High level plan generated successfully with {self.shared_state['total_scenes']} scenes."

    def tool_build_title_scene(self) -> str:
        """Generates scene 0: the title page."""
        self.workflow_logger.info(f"Running BuildTitleSceneTool...")
        metadata = self._safe_get(self.shared_state, "metadata", {})
        authors = self._safe_get(metadata, "authors", [])
        affiliations = self._safe_get(metadata, "affiliations", [])
        venue = self._safe_get(metadata, "venue", "")
        paper_title = self._safe_get(metadata, "paper_title", "Untitled Paper")
        
        logos = self.asset_analyser.analyze_images()
        available_logos_desc = []
        if logos.get("conference"):
            available_logos_desc.append(f"conference_logo: {Path(logos['conference']).name}")
        for i, aff_logo in enumerate(logos.get("affiliations", [])):
            if aff_logo:
                aff_name = affiliations[i].get("name", f"Affiliation {i+1}") if i < len(affiliations) else f"Affiliation {i+1}"
                available_logos_desc.append(f"affiliation_{i+1}_logo: {Path(aff_logo).name} ({aff_name})")
        
        style_prompt = prompts.title_style_prompt.format(
            metadata_json=json.dumps(metadata, indent=2),
            available_logos="\n".join(available_logos_desc) if available_logos_desc else "No logos available."
        )
        
        raw = self.planner(prompt=style_prompt, pdf_path=Path(self.pdf_path))
        style_plan = _load_json_dict(raw)
        if not isinstance(style_plan, dict):
            style_plan = {
                "layout_template": "title_page", "background_color": "#FFFFFF",
                "layout_regions": {
                    "title": {"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25},
                    "authors": {"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.12}
                }
            }
            
        # Build final elements with layout advice
        elements = {"title": paper_title, "authors": format_authors_with_superscripts(authors), "affiliations": format_affiliations_display(authors, affiliations), "venue": venue}
        
        # Add logos from AssetAnalyser
        if logos.get("conference"):
            elements["conference_logo"] = {"type": "logo", "path": str(logos["conference"])}
        
        if logos.get("affiliations"):
            elements["affiliation_logos"] = [{"type": "logo", "path": str(p)} for p in logos["affiliations"]]
        
        # Ensure the layout regions match what logos we actually found
        final_regions = style_plan.get("layout_regions", {}).copy()
        if not logos.get("conference") and "conference_logo" in final_regions:
            del final_regions["conference_logo"]
        if not logos.get("affiliations") and "affiliation_logos" in final_regions:
            del final_regions["affiliation_logos"]

        scene = {
            "scene_id": 0, "title": paper_title, "summary": f"Title page for: {paper_title}", "paper_section": "Title",
            "narrative_role": "title", "time_allocation_sec": 5, "style": "Slides",
            "layout": {
                "template": "title_page",
                "background_color": style_plan.get("background_color", "#FFFFFF"),
                "regions": final_regions
            },
            "elements": elements,
            "builds": [{"step_index": 0, "time_offset_sec": 0.0, "actions": [{"type": "show", "target": "all"}], "audio_segment": f"This paper is titled {paper_title}."}],
            "expected_build_steps": 1, "time_cost": "5", "audio_content": f"This paper is titled {paper_title}."
        }
        # Save to shared state
        self.shared_state["high_plan"].insert(0, scene)
        self.shared_state["total_scenes"] = len(self.shared_state["high_plan"])
        
        # Ensure title_scene.json is saved as file_0.json for consistent indexing
        with open(self.log_dir / "file_0.json", "w") as f:
            json.dump(scene, f, indent=4)
            
        with open(self.log_dir / "title_scene.json", "w") as f:
            json.dump(scene, f, indent=4)
            
        return "Title scene built and inserted at index 0."

    def tool_process_low_level_scene(self, scene_idx: int) -> str:
        """Runs the ReAct Agent per-scene to do low-level planning."""
        self.workflow_logger.info(f"Running ProcessLowLevelSceneTool for scene {scene_idx}...")
        
        if scene_idx >= len(self.shared_state["high_plan"]):
            return f"Error: scene_idx {scene_idx} out of range."

        part_plan = self.shared_state["high_plan"][scene_idx]
        plan_file = self.log_dir / f"file_{scene_idx}.json"
        
        if part_plan.get("narrative_role") == "title":
            with open(plan_file, "w") as file:
                json.dump(part_plan, file, indent=4)
            return "Scene is title page, low level planning skipped."
            
        if os.path.exists(plan_file):
            with open(plan_file, "r") as file:
                self.shared_state["high_plan"][scene_idx] = json.load(file)
            return "Scene already planned."

        # Disentangled Execution via sequential calls (simulating sub-agent via code for stability)
        # Stage 1: Content
        past_contents = []
        for past_idx in range(max(0, scene_idx - 2), scene_idx):
            past_file = self.log_dir / f"content_{past_idx}.json"
            if os.path.exists(past_file):
                try:
                    with open(past_file, "r") as f:
                        past_contents.append(json.load(f))
                except Exception: pass
                
        memory_context = ""
        if past_contents:
            memory_context = "## Previous Scenes Memory\n"
            for past in past_contents: memory_context += json.dumps({"extracted_content": past.get("extracted_content")}, indent=2) + "\n"
        prompt = prompts.content_extraction_prompt.format(scene_json=json.dumps(part_plan, indent=2), memory_context=memory_context)
        for _ in range(3):
            raw = self.planner(prompt=prompt, pdf_path=Path(self.pdf_path))
            content_summary = _load_json_dict(raw)
            if content_summary: break
        else:
            content_summary = {"extracted_content": part_plan.get("summary", ""), "key_figures": [], "key_tables": [], "key_equations": [], "section_refs": []}
        
        # Stage 2: Layout
        style_advice = self.retrieve_scene_style(part_plan)
        style_plan = self.style_plan_by_llm(part_plan, content_summary, style_advice, scene_idx)
        
        # Stage 3: Draft
        past_drafts = []
        if scene_idx > 0:
            past_file = self.log_dir / f"low_{scene_idx - 1}.json"
            if os.path.exists(past_file):
                try:
                    with open(past_file, "r") as f:
                        past_drafts.append(json.load(f))
                except Exception: pass
        duration_stat = part_plan.get("duration_stat", {"min": 5.0, "max": 15.0, "avg": 8.0})
        content_draft = self.low_plan_by_llm(part_plan, content_summary, style_plan, duration_stat, past_drafts, scene_idx)
        
        # Stage 4: Refine
        final_refined = self.style_refine_by_llm(content_draft, style_plan, scene_idx)
        final_refined["time_allocation_sec"] = content_draft.get("duration_sec", 8.0)
        
        # Merge
        merged = part_plan.copy()
        merged["extracted_content"] = content_summary.get("extracted_content", "")
        merged["layout"] = {"template": style_plan.get("layout_template", "one_col_bullets"), "background_color": style_plan.get("background_color", "#FFFFFF"), "regions": style_plan.get("layout_regions", {})}
        merged.update(final_refined)
        merged["source"] = content_draft.get("source", [])
        merged["time_allocation_sec"] = content_draft.get("duration_sec", merged.get("time_allocation_sec", 8.0))
        merged["audio_content"] = content_draft.get("audio_content", "")
        merged["prompt"] = content_draft.get("prompt", "")
        
        self.shared_state["high_plan"][scene_idx] = merged
        with open(plan_file, "w") as file:
            json.dump(merged, file, indent=4)
            
        return f"Scene {scene_idx} low level planning completed successfully."

    def tool_render_scene(self, scene_idx: int) -> str:
        self.workflow_logger.info(f"Running RenderSceneTool for scene {scene_idx}...")
        curr_scene_dir = self.work_dir / f"scene_{scene_idx}"
        if not os.path.isdir(curr_scene_dir):
            curr_scene_dir.mkdir()
            
        scene_plan = self.shared_state["high_plan"][scene_idx]
        
        if self.slide_renderer:
            try:
                video_path = self.slide_renderer.render_scene(scene_plan, scene_idx)
                return f"Scene {scene_idx} rendered successfully at {video_path}"
            except Exception as e:
                return f"Error rendering scene {scene_idx}: {e}"
        return "SlideRenderer not available."

    def tool_merge_videos(self) -> str:
        self.workflow_logger.info(f"Running MergeVideosTool...")
        video_list = []
        for i in range(self.shared_state["total_scenes"]):
            video_path = self.work_dir / f"scene_{i}" / f"scene{i}.mp4"
            if video_path.exists():
                video_list.append(video_path)
        
        if not video_list:
            return "No videos rendered, merge failed."
            
        concatenate_videos(video_list, self.final_video_path_)
        return f"Final video concatenated at {self.final_video_path_}"

    # --- Tool Under-the-hood Helpers (Moved from preacher.py) ---
    def retrieve_global_style(self) -> str:
        # Same as preacher.py
        context = []
        try:
            k = self.retrieval_top_k
            similar_papers = self.retriever.retrieve_similar_papers(pdf_path=self.pdf_path, k=k)
            context.append("## Similar Papers found in specific domain:")
            for p in similar_papers: context.append(f"- {p.get('paper_name', 'Unknown')}")
            
            style_matches = []
            for p in similar_papers:
                if p.get('paper_name', '') in self.style_db:
                    style_matches.append((p['paper_name'], self.style_db[p['paper_name']]))
            
            total_slides_list = []
            if style_matches:
                context.append("\n## Reference Presentation Styles:")
                for title, path in style_matches:
                    if Path(path).exists():
                        with open(path, "r") as f:
                            meta = json.load(f)
                            total_slides_list.append(meta.get("total_slides", len(meta.get("slides", []))))
                if total_slides_list:
                    context.append(f"\nRECOMMENDATION: Target approximately {int(sum(total_slides_list)/len(total_slides_list))} scenes.")
        except Exception as e:
            self.workflow_logger.warning(f"Global retrieval failed: {e}")
        return "\n".join(context)
        
    def retrieve_scene_style(self, scene_plan: dict) -> str:
        narrative_role = scene_plan.get('narrative_role', '').lower()
        if not narrative_role or narrative_role not in ['introduction', 'method', 'experiments', 'results']: return ""
        try:
            k = self.retrieval_top_k
            index_dir = Path("data_reference/faiss") / narrative_role
            if not index_dir.exists(): return ""
            section_retriever = PaperRetriever(logger=self.workflow_logger, use_openai=True)
            section_retriever.load_index(index_dir, index_name=f"{narrative_role}.faiss", meta_name="metadata.json")
            similar_papers = section_retriever.retrieve_similar_papers(pdf_path=self.pdf_path, k=k)
            layout_descriptions = []
            for p in similar_papers:
                if p.get('paper_name') in self.style_db:
                    meta_path = Path(self.style_db[p.get('paper_name')])
                    if meta_path.exists():
                        with open(meta_path, "r") as f:
                            meta = json.load(f)
                            for slide in meta.get("slides", []):
                                if slide.get("slide_section", "").lower() == narrative_role:
                                    layout_desc = slide.get("layout_structure", {}).get("layout_description", "")
                                    if layout_desc: layout_descriptions.append(layout_desc)
            if layout_descriptions: return "\n".join(random.sample(layout_descriptions, min(5, len(layout_descriptions))))
            return ""
        except Exception: return ""

    def content_extract_by_llm(self, part_plan, past_contents, idx) -> dict:
        memory_context = ""
        if past_contents:
            memory_context = "## Previous Scenes Memory\n"
            for past in past_contents: memory_context += json.dumps({"extracted_content": past.get("extracted_content")}, indent=2) + "\n"
        prompt = prompts.content_extraction_prompt.format(scene_json=json.dumps(part_plan, indent=2), memory_context=memory_context)
        for _ in range(3):
            raw = self.planner(prompt=prompt, pdf_path=Path(self.pdf_path))
            content_summary = _load_json_dict(raw)
            if content_summary: break
        else:
            content_summary = {"extracted_content": part_plan.get("summary", ""), "key_figures": [], "key_tables": [], "key_equations": [], "section_refs": []}
        
        content_file = self.log_dir / f"content_{idx}.json"
        with open(content_file, "w") as f: json.dump(content_summary, f, indent=4)
        return content_summary

    def style_plan_by_llm(self, part_plan, content_summary, style_advice, idx) -> dict:
        prompt = prompts.style_planning_prompt.format(content_summary=json.dumps(content_summary, indent=2), scene_context=json.dumps(part_plan, indent=2), style_advice=style_advice)
        for _ in range(3):
            raw = self.planner(prompt=prompt, pdf_path=Path(self.pdf_path))
            parsed = _load_json_dict(raw)
            if isinstance(parsed, dict):
                with open(self.log_dir / f"style_{idx}.json", "w") as f: json.dump(parsed, f, indent=4)
                return parsed
        return {}
        
    def low_plan_by_llm(self, part_plan, content_summary, style_plan, duration_stat, past_contents, idx) -> dict:
        memory_context = ""
        prompt = prompts.low_level_planning_prompt.format(content_summary=json.dumps(content_summary, indent=2), style_plan=json.dumps(style_plan, indent=2), scene_context=json.dumps(part_plan, indent=2), duration_stat=json.dumps(duration_stat, indent=2), memory_context=memory_context)
        for _ in range(3):
            raw = self.planner(prompt=prompt, pdf_path=Path(self.pdf_path))
            parsed = _load_json_dict(raw)
            if isinstance(parsed, dict):
                with open(self.log_dir / f"low_{idx}.json", "w") as f: json.dump(parsed, f, indent=4)
                return parsed
        return {}
        
    def style_refine_by_llm(self, content_draft, style_plan, idx) -> dict:
        prompt = prompts.style_refinement_prompt.format(content_draft=json.dumps(content_draft, indent=2), layout_info=json.dumps(style_plan, indent=2))
        for _ in range(3):
            raw = self.planner(prompt=prompt, pdf_path=Path(self.pdf_path))
            parsed = _load_json_dict(raw)
            if isinstance(parsed, dict):
                with open(self.log_dir / f"refine_{idx}.json", "w") as f: json.dump(parsed, f, indent=4)
                return parsed
        return {}
        
    # Legacy code comments from preacher.py (for future reference)
    # def tolist(self, high_plan: str) -> list:
    #     if self.plan_by=='GEMINI':
    #         return text_to_list(high_plan)
