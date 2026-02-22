import json
from pathlib import Path
from pipeline import prompts
from utils.textwork import _load_json_dict

class StyleRefiner:
    def __init__(self, planner_func, workflow_logger):
        self.planner = planner_func
        self.workflow_logger = workflow_logger

    def style_refine_by_llm(self, pdf_path, scene_idx, content_draft, style_plan) -> dict:
        """Stage 4: Decide builds from scratch, assign drafted content to build steps."""
        total_time_sec = content_draft.get("duration_sec", 8.0)
        prompt = prompts.style_refinement_prompt.format(
            content_draft=json.dumps(content_draft, indent=2),
            layout_info=json.dumps({
                "layout_template": style_plan.get("layout_template", ""),
                "layout_regions": style_plan.get("layout_regions", {}),
                "has_figure": style_plan.get("has_figure", False),
                "total_time_sec": total_time_sec,
            }, indent=2),
        )
        
        max_retries = 3
        for attempt in range(max_retries):
            raw = eval(self.planner(
                prompt=prompt,
                pdf_path=Path(pdf_path),
            ))
            self.workflow_logger.info(f"  Style refinement scene {scene_idx} (Attempt {attempt+1}): {raw[:200] if isinstance(raw, str) else str(raw)[:200]}")
            
            parsed = _load_json_dict(raw)
            if parsed and isinstance(parsed, dict):
                return parsed
                
            self.workflow_logger.warning(f"Style refinement parsing failed for scene {scene_idx} on attempt {attempt+1}. Retrying...")
            prompt += f"\n\nERROR: The previous response was not valid JSON. Please ensure you output ONLY valid JSON without any truncated strings or formatting errors."
            
        raise ValueError(f"Style refinement failed for scene {scene_idx} after {max_retries} attempts.")
