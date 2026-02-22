import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import _load_json_dict

class StylePlanner:
    def __init__(self, planner_func, workflow_logger):
        self.planner = planner_func
        self.workflow_logger = workflow_logger

    def style_plan_by_llm(self, pdf_path, scene_idx, part_plan, content_summary, style_advice) -> dict:
        """Stage 2: Decide layout and build skeleton using content + reference styles."""
        prompt = prompts.style_planning_prompt.format(
            content_summary=json.dumps(content_summary, indent=2),
            scene_context=json.dumps(part_plan, indent=2),
            style_advice=style_advice,
        )
        
        max_retries = 3
        for attempt in range(max_retries):
            raw = eval(self.planner(
                prompt=prompt,
                pdf_path=Path(pdf_path),
            ))
            self.workflow_logger.info(f"  Style plan scene {scene_idx} (Attempt {attempt+1}): {raw[:200] if isinstance(raw, str) else str(raw)[:200]}")
            
            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                return parsed
                
            self.workflow_logger.warning(f"Style planning parsing failed for scene {scene_idx} on attempt {attempt+1}. Retrying...")
            prompt += f"\n\nERROR: The previous response was not valid JSON. Please ensure you output ONLY valid JSON without any truncated strings or formatting errors."
            
        raise ValueError(f"Style planning failed for scene {scene_idx} after {max_retries} attempts.")
