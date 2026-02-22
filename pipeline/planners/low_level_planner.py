import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import _load_json_dict, classify_response

class LowLevelPlanner:
    def __init__(self, planner_func, evaluator_func, workflow_logger):
        self.planner = planner_func
        self.evaluator = evaluator_func
        self.workflow_logger = workflow_logger

    def low_plan_by_llm(self, pdf_path, scene_idx, part_plan, content_summary, style_plan, duration_stat, past_contents=None) -> dict:
        """Stage 3: Draft content (bullets, audio, figures) within the decided layout."""
        
        memory_context = ""
        if past_contents:
            memory_context = "## Previous Content\n"
            memory_context += "The following content was drafted for the immediately preceding scenes.\n"
            memory_context += "You MUST NOT repeat the exact text content or claims from these previous scenes in your current draft.\n\n"
            for past in past_contents:
                subset = {
                    "bullets": past.get("bullets", []),
                    "audio_content": past.get("audio_content", "")
                }
                memory_context += json.dumps(subset, indent=2) + "\n"

        prompt = prompts.low_level_planning_prompt.format(
            content_summary=json.dumps(content_summary, indent=2),
            style_plan=json.dumps(style_plan, indent=2),
            scene_context=json.dumps(part_plan, indent=2),
            duration_stat=json.dumps(duration_stat, indent=2),
            memory_context=memory_context,
        )
        
        max_retries = 3
        for attempt in range(max_retries):
            raw = eval(self.planner(
                prompt=prompt,
                pdf_path=Path(pdf_path),
            ))
            self.workflow_logger.info(f"  Content draft scene {scene_idx} (Attempt {attempt+1}): {raw[:200] if isinstance(raw, str) else str(raw)[:200]}")
            
            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                return parsed
                
            self.workflow_logger.warning(f"Content drafting parsing failed for scene {scene_idx} on attempt {attempt+1}. Retrying...")
            prompt += f"\n\nERROR: The previous response was not valid JSON. Please ensure you output ONLY valid JSON without any truncated strings or formatting errors."
            
        raise ValueError(f"Content drafting failed for scene {scene_idx} after {max_retries} attempts.")

    def low_evaluate_by_llm(self, pdf_path, scene_idx, low_plan_str) -> tuple:
        prompt = prompts.low_level_evaluate_prompt + ' \n ' + low_plan_str
        eval_results = eval(
            self.evaluator(
                prompt=prompt,
                pdf_path=Path(pdf_path),
            )
        )
        success = classify_response(eval_results)
        self.workflow_logger.info(f"Low eval scene {scene_idx}: {eval_results}")
        return success, eval_results
