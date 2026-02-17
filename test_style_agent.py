"""
Minimal test script for the 5-stage style agent pipeline.

Runs content extraction → style planning → low-level planning → style refinement
on the first scene of a paper, outputting to style_agent_output/.

Usage:
    python test_style_agent.py
"""

import json
import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from pipeline.preacher import Preacher, _load_json_dict
from utils.logger import get_logger

PDF_PATH = "dataset/ego3d.pdf"
OUTPUT_DIR = "style_agent_output"
CONFIG_PATH = "config.yml"
LLM_BACKEND = "GEMINI"


def main():
    logger = get_logger("StyleAgentTest", console_log_level=logging.INFO)
    
    pdf_path = Path(PDF_PATH)
    if not pdf_path.exists():
        logger.error(f"PDF not found: {pdf_path}")
        sys.exit(1)
    
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(exist_ok=True)
    
    logger.info("=" * 50)
    logger.info("Style Agent Test — 5-Stage Pipeline")
    logger.info("=" * 50)
    
    # Initialize Preacher
    agent = Preacher(
        input_path=pdf_path,
        output_dir=output_dir,
        llm_config_path=Path(CONFIG_PATH),
        plan_by=LLM_BACKEND,
        eval_by=LLM_BACKEND,
        art_work=LLM_BACKEND,
        with_example=False,
        schedule_example_path=None,
        with_reflection=False,
        with_rollback=False,
    )
    
    # ── Step 1: High-level planning (or use cached) ──
    logger.info("\n[Step 1] High-level planning...")
    high_plan_path = agent.high_plan_path
    
    if high_plan_path.exists():
        logger.info(f"  Using cached high plan: {high_plan_path}")
        with open(high_plan_path, 'r') as f:
            agent.high_plan = f.read()
    else:
        logger.info("  Generating high-level plan...")
        agent.high_plan = agent.high_planning()
    
    # Parse the high plan
    raw = agent.high_plan
    if isinstance(raw, str):
        parsed = _load_json_dict(raw)
        if isinstance(parsed, dict) and len(parsed) == 1:
            parsed = list(parsed.values())[0]
        agent.high_plan_list = parsed if isinstance(parsed, list) else [parsed]
    elif isinstance(raw, list):
        agent.high_plan_list = raw
    else:
        agent.high_plan_list = [raw]
    
    num_scenes = len(agent.high_plan_list)
    logger.info(f"  High plan has {num_scenes} scenes.")
    
    # ── Step 2: Run low-level planning for FIRST SCENE only ──
    logger.info("\n[Step 2] Low-level planning for scene 0 (4-stage pipeline)...")
    agent.final_plan = [{}]
    agent.scene_idx = 0
    
    try:
        agent.low_planning(agent.high_plan_list[0])
    except Exception as e:
        logger.error(f"  Low planning failed: {e}", exc_info=True)
        sys.exit(1)
    
    # ── Step 3: Inspect results ──
    plan = agent.final_plan[0]
    log_dir = agent.log_dir
    
    logger.info("\n" + "=" * 50)
    logger.info("RESULTS")
    logger.info("=" * 50)
    
    # Check content extraction
    content_file = log_dir / "content_0.json"
    if content_file.exists():
        with open(content_file) as f:
            content = json.load(f)
        logger.info(f"\n✓ Content extraction ({content_file.name}):")
        logger.info(f"  extracted_content: {content.get('extracted_content', '')[:100]}...")
        logger.info(f"  key_figures: {content.get('key_figures', [])}")
    else:
        logger.error(f"✗ Content extraction file not found: {content_file}")
    
    # Check style plan
    style_file = log_dir / "style_0.json"
    if style_file.exists():
        with open(style_file) as f:
            style = json.load(f)
        logger.info(f"\n✓ Style plan ({style_file.name}):")
        logger.info(f"  layout_template: {style.get('layout_template', 'N/A')}")
        logger.info(f"  expected_build_steps: {style.get('expected_build_steps', 'N/A')}")
        logger.info(f"  build_skeleton: {json.dumps(style.get('build_skeleton', []), indent=2)}")
    else:
        logger.error(f"✗ Style plan file not found: {style_file}")
    
    # Check final plan
    plan_file = log_dir / "file_0.json"
    if plan_file.exists():
        logger.info(f"\n✓ Final merged plan ({plan_file.name}):")
        logger.info(f"  title: {plan.get('elements', {}).get('title', plan.get('title', 'N/A'))}")
        logger.info(f"  layout.template: {plan.get('layout', {}).get('template', 'N/A')}")
        logger.info(f"  audio_content: {plan.get('audio_content', '')[:100]}...")
        
        builds = plan.get("builds", [])
        logger.info(f"  builds: {len(builds)} steps")
        for b in builds:
            logger.info(f"    Build {b.get('step_index', '?')}: actions={[a.get('target') for a in b.get('actions', [])]}, audio_segment={b.get('audio_segment', '')[:60]}...")
        
        elements = plan.get("elements", {})
        bullets = elements.get("bullets", [])
        logger.info(f"  bullets ({len(bullets)}): {bullets}")
    else:
        logger.error(f"✗ Final plan file not found: {plan_file}")
    
    logger.info("\n" + "=" * 50)
    logger.info("Test complete! Inspect files in:")
    logger.info(f"  {log_dir}/")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()
