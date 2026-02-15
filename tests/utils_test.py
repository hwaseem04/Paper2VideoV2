import json
import logging

def validate_high_level_schema(plan: list) -> bool:
    if not isinstance(plan, list):
        return False
    required_keys = ["scene_id", "scene_idx", "summary", "style", "audio_content", "time_cost"]
    for scene in plan:
        if not all(k in scene for k in required_keys):
            logging.error(f"Missing keys in high level plan: {scene.keys()}")
            return False
    return True

def validate_low_level_schema(plan: dict) -> bool:
    if not isinstance(plan, dict):
        return False
    required_keys = ["layout", "elements", "builds"]
    if not all(k in plan for k in required_keys):
        logging.error(f"Missing keys in low level plan: {plan.keys()}")
        return False
    
    # Validate builds
    if not isinstance(plan["builds"], list):
        return False
    
    for build in plan["builds"]:
        if "actions" not in build or "audio_segment" not in build:
            return False
            
    return True
