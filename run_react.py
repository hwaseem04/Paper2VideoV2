"""
Unified entry point for Paper2Video pipeline using ReAct Agent.

Usage:
  python run_react.py <input_pdf>
  python run_react.py <input_pdf> --output_dir output --llm GEMINI --reflection --examples
"""

import sys
import logging
from pathlib import Path

import fire

project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

from pipeline.preacher_react import PreacherReAct
from utils.logger import get_logger

def main(
    input_pdf: str,
    output_dir: str = "output",
    config: str = "config.yml",
    llm: str = "GEMINI",
    examples: bool = False,    
    reflection: bool = False,
    rollback: bool = False
):
    """
    Run the Paper2Video ReAct pipeline.

    Args:
        input_pdf: Path to the input PDF file.
        output_dir: Output directory.
        config: Path to LLM config YAML.
        llm: LLM backend (GEMINI, GPT4_AZ, GPT4v, QWEN).
        reflection: Enable reflection loops for planning.
        examples: Enable few-shot examples in prompts.
    """
    logger = get_logger("Paper2VideoReAct", console_log_level=logging.INFO)

    input_path = Path(input_pdf).resolve()
    output_dir = Path(output_dir).resolve()
    llm_config_path = Path(config).resolve()

    if not input_path.exists():
        logger.error(f"Input PDF not found: {input_path}")
        sys.exit(1)

    # Step 3: Run Preacher ReAct agent
    logger.info("=" * 50)
    logger.info("Step 3: Running Preacher ReAct agent...")
    logger.info("=" * 50)

    agent = PreacherReAct(
        input_path=input_path,
        output_dir=output_dir,
        llm_config_path=llm_config_path,
        plan_by=llm,
        eval_by=llm,
        art_work=llm,
        with_example=examples,
        with_reflection=reflection,
        with_rollback=rollback,
        silent=False,
    )

    agent.run()

    logger.info("=" * 50)
    logger.info("Pipeline complete!")
    logger.info("=" * 50)


if __name__ == "__main__":
    fire.Fire(main)
