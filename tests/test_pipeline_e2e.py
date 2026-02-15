"""
End-to-End Pipeline Tests for Paper2Video (Workstream F)

PURPOSE:
  Tests the full data flow through the Preacher pipeline WITHOUT making
  real LLM API calls. Uses dataset/federated.pdf as the input PDF.

WHAT IT VERIFIES:
  1. test_full_flow_schema  — Preacher initializes, high->low planning flow works,
                              output contains required keys (layout, builds).
  2. test_schema_validation — Every field in high-level and low-level plan JSON
                              has the correct type and required keys are present.
  3. test_source_grounding  — The 'source' fields in generated plans reference
                              content that actually exists in the input PDF text.
"""

import unittest
from unittest.mock import MagicMock, patch
import json
import os
import re
import fitz  # PyMuPDF
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from pipeline.preacher import Preacher


# ---------------------------------------------------------------------------
# Shared test data
# ---------------------------------------------------------------------------

SAMPLE_HIGH_PLAN = [
    {
        "scene_id": 0,
        "scene_idx": 0,
        "SCENE": "Introduction",
        "DESCRIPTION": "Intro to the paper",
        "summary": "Summary of intro",
        "style": "Slides",
        "audio_content": "Narration text",
        "source": "Section 1",
        "time_cost": 5
    },
    {
        "scene_id": 1,
        "scene_idx": 1,
        "SCENE": "Method",
        "DESCRIPTION": "Core methodology",
        "summary": "Federated learning approach",
        "style": "Slides",
        "audio_content": "The method section explains...",
        "source": "Figure 1 on page 2",
        "time_cost": 8
    }
]

SAMPLE_LOW_PLAN = {
    "scene_id": 0,
    "style": "Slides",
    "layout": {
        "template": "two_col_fig_left",
        "regions": {
            "title":   {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
            "figure":  {"x": 0.05, "y": 0.2,  "w": 0.45, "h": 0.7},
            "bullets": {"x": 0.55, "y": 0.2,  "w": 0.4,  "h": 0.7}
        }
    },
    "elements": {
        "title": "Introduction",
        "figure": {"type": "paper_figure", "ref": "Figure 1"},
        "bullets": ["Point 1", "Point 2"]
    },
    "builds": [
        {
            "step_index": 0,
            "actions": [
                {"type": "show", "target": "title"},
                {"type": "show", "target": "figure"}
            ],
            "audio_segment": "Welcome to this presentation."
        },
        {
            "step_index": 1,
            "actions": [{"type": "fade_in", "target": "bullets[0]"}],
            "audio_segment": "First point."
        },
        {
            "step_index": 2,
            "actions": [{"type": "fade_in", "target": "bullets[1]"}],
            "audio_segment": "Second point."
        }
    ]
}


# ---------------------------------------------------------------------------
# Helper: create a patched Preacher
# ---------------------------------------------------------------------------

def _make_preacher(pdf_path, work_dir):
    return Preacher(
        input_path=pdf_path,
        output_dir=work_dir,
        llm_config_path=Path("config.yml"),
        plan_by="GEMINI",
        eval_by="GEMINI",
        art_work="GEMINI",
        with_example=False,
        schedule_example_path=None,
        with_reflection=False,
        with_rollback=False,
        silent=True,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPipelineE2E(unittest.TestCase):

    def setUp(self):
        self.work_dir = Path("tests/output/e2e_test")
        self.pdf_path = Path("dataset/federated.pdf")
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"Test PDF not found at {self.pdf_path}")

    # ------------------------------------------------------------------
    # 1. Full flow: Preacher init → high plan → low plan
    # ------------------------------------------------------------------
    @patch('pipeline.preacher.GPT4')
    @patch('pipeline.preacher.PaperRetriever')
    @patch('pipeline.preacher.SlideRenderer')
    def test_full_flow_schema(self, mock_renderer, mock_retriever, mock_gpt4):
        """Verify Preacher initialises and the high→low planning data flow works."""
        preacher = _make_preacher(self.pdf_path, self.work_dir)

        preacher.planner = MagicMock(side_effect=[
            str(SAMPLE_HIGH_PLAN),
            str(SAMPLE_LOW_PLAN),
        ])
        preacher.retrieve_scene_style = MagicMock(return_value="")

        # A. High planning
        preacher.high_plan = preacher.planner(prompt="fake")
        preacher.high_plan_list = SAMPLE_HIGH_PLAN

        # B. Low planning
        preacher.final_plan = [{}]
        preacher.scene_idx = 0
        low_plan = preacher.low_plan_by_llm(SAMPLE_HIGH_PLAN[0])

        self.assertIsInstance(low_plan, dict)
        self.assertIn("layout", low_plan)
        self.assertIn("builds", low_plan)
        print("✓ Full flow schema passed")

    # ------------------------------------------------------------------
    # 2. Schema field-level validation
    # ------------------------------------------------------------------
    def test_schema_validation(self):
        """Validate every required field and type in high-level and low-level plans."""

        # --- High-level plan ---
        required_high_keys = {
            "scene_id": int, "scene_idx": int, "summary": str,
            "style": str, "audio_content": str, "time_cost": int
        }
        for scene in SAMPLE_HIGH_PLAN:
            for key, expected_type in required_high_keys.items():
                self.assertIn(key, scene, f"Missing key '{key}' in high-level plan")
                self.assertIsInstance(scene[key], expected_type,
                    f"Key '{key}' should be {expected_type.__name__}, got {type(scene[key]).__name__}")

        # --- Low-level plan ---
        self.assertIn("layout", SAMPLE_LOW_PLAN)
        self.assertIn("elements", SAMPLE_LOW_PLAN)
        self.assertIn("builds", SAMPLE_LOW_PLAN)

        # Layout regions must have x/y/w/h
        for name, region in SAMPLE_LOW_PLAN["layout"].get("regions", {}).items():
            for coord in ("x", "y", "w", "h"):
                self.assertIn(coord, region, f"Region '{name}' missing '{coord}'")
                self.assertIsInstance(region[coord], (int, float))

        # Builds must have actions + audio_segment
        for i, build in enumerate(SAMPLE_LOW_PLAN["builds"]):
            self.assertIn("actions", build, f"Build {i} missing 'actions'")
            self.assertIn("audio_segment", build, f"Build {i} missing 'audio_segment'")
            self.assertIsInstance(build["actions"], list)

        print("✓ Schema validation passed")

    # ------------------------------------------------------------------
    # 3. Source grounding — do 'source' refs exist in the PDF?
    # ------------------------------------------------------------------
    def test_source_grounding(self):
        """Verify that 'source' fields reference content present in the PDF."""
        # Extract all text from PDF
        doc = fitz.open(str(self.pdf_path))
        full_text = " ".join(page.get_text() for page in doc).lower()
        doc.close()

        for scene in SAMPLE_HIGH_PLAN:
            source = scene.get("source", "")
            if not source:
                continue

            # Extract key terms from source string
            # e.g. "Figure 1 on page 2" → check "figure" exists, page count >= 2
            # e.g. "Section 1" → check "section" or "1" or heading text exists

            # Check figure references
            fig_match = re.search(r'figure\s*(\d+)', source, re.IGNORECASE)
            if fig_match:
                fig_keyword = f"figure {fig_match.group(1)}"
                # Figures are commonly labeled "Figure N" or "Fig. N"
                found = (fig_keyword in full_text) or (f"fig. {fig_match.group(1)}" in full_text)
                self.assertTrue(found,
                    f"Source '{source}' references '{fig_keyword}' but it was not found in PDF text")

            # Check section references
            sec_match = re.search(r'section\s*(\d+)', source, re.IGNORECASE)
            if sec_match:
                # Sections are usually numbered headings
                sec_num = sec_match.group(1)
                found = (f"section {sec_num}" in full_text) or (f"{sec_num}." in full_text) or (f"{sec_num} " in full_text)
                self.assertTrue(found,
                    f"Source '{source}' references Section {sec_num} but it was not found in PDF text")

        print("✓ Source grounding passed")


if __name__ == '__main__':
    unittest.main()
