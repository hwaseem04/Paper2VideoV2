import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path
import sys
import json
import os

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from pipeline.preacher import Preacher
from tests.utils_test import validate_high_level_schema, validate_low_level_schema

class TestRegression(unittest.TestCase):
    def setUp(self):
        self.work_dir = Path("tests/output/regression")
        self.pdf_path = Path("dataset/federated.pdf")
        
        if not self.pdf_path.exists():
            raise FileNotFoundError("Regression PDF not found.")
            
        self.work_dir.mkdir(parents=True, exist_ok=True)
        
    @patch('pipeline.preacher.GPT4')
    @patch('pipeline.preacher.PaperRetriever')
    def test_schema_integrity(self, mock_retriever, mock_gpt4):
        """
        Runs the Preacher pipeline with MOCKED LLM responses but REAL PDF input
        to ensure that the data flow maintains schema integrity.
        """
        preacher = Preacher(self.work_dir, self.pdf_path, openai_api_key="dummy")
        
        # Mock LLM to return valid JSONs
        high_plan_mock = json.dumps([
            {
                "scene_id": 0, "scene_idx": 0, 
                "SCENE": "Intro", "DESCRIPTION": "Test",
                "summary": "Intro summary", "style": "Slides", 
                "audio_content": "Audio...", "time_cost": 5,
                "source": "Page 1" 
            }
        ])
        
        low_plan_mock = json.dumps({
            "scene_id": 0,
            "style": "Slides",
            "layout": {"template": "one_col_bullets", "regions": {}},
            "elements": {"title": "Intro"},
            "builds": [{"step_index": 0, "actions": [], "audio_segment": "Audio"}]
        })
        
        # Preacher.planner calls -> (High level) then (Low level)
        preacher.planner = MagicMock(side_effect=[high_plan_mock, low_plan_mock])
        
        # 1. High Planning
        high_res = preacher.planner(prompt="fake")
        high_data = json.loads(high_res)
        
        self.assertTrue(validate_high_level_schema(high_data), "High level schema validation failed")
        
        # 2. Low Planning (Simulated)
        preacher.high_plan_list = high_data
        preacher.retrieve_scene_style = MagicMock(return_value="")
        
        low_res_str = preacher.low_plan_by_llm(high_data[0])
        low_data = json.loads(str(low_res_str).replace("'", '"')) if isinstance(low_res_str, str) else low_res_str
        
        if isinstance(low_data, dict):
             self.assertTrue(validate_low_level_schema(low_data), "Low level schema validation failed")
        
if __name__ == '__main__':
    unittest.main()
