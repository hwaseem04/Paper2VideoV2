import sys
import unittest
from pathlib import Path
import logging
import json

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from pipeline.preacher import Preacher
from tools.retriever import PaperRetriever

# Mock logger
logging.basicConfig(level=logging.INFO)

class TestPreacherRetrieval(unittest.TestCase):
    
    def setUp(self):
        # Create a subclass to bypass heavy initialization
        class MockPreacher(Preacher):
            def _create_components(self, llm_config_path, schedule_example_path, silent):
                self.qa_logger = logging.getLogger("QA")
                self.workflow_logger = logging.getLogger("Workflow")
                self.pdf_path = Path("dataset/ego3d.pdf") # Ensure this is set
                
                # Manual Init of Retrieval (what we want to test)
                try:
                    self.retriever = PaperRetriever(index_path=Path("output/test_index"))
                    self.style_db = {}
                    style_db_path = Path("data_reference/style_db/db_summary.json")
                    if style_db_path.exists():
                        with open(style_db_path, "r") as f:
                            summary = json.load(f)
                            for item in summary:
                                self.style_db[item["video_id"]] = item["path"]
                    else:
                        print("Style DB not found for test.")
                except Exception as e:
                    print(f"Failed to init retrieval: {e}")

        # Instantiate with dummy args
        self.preacher = MockPreacher(
            input_path=Path("dataset/ego3d.pdf"),
            output_dir=Path("output/test_preacher"),
            llm_config_path=Path("config.yml"),
            plan_by="depictqa",
            eval_by="depictqa",
            art_work="wanx",
            with_example=False
        )

    def test_retrieve_global_style(self):
        print("\nTesting retrieve_global_style...")
        
        # DEBUG: Check direct retrieval
        res = self.preacher.retriever.retrieve_similar_papers(pdf_path=self.preacher.pdf_path, k=3)
        print(f"DEBUG: Retrieved {len(res)} items")
        if res:
            print(f"DEBUG: Item 0 type: {type(res[0])}")
            print(f"DEBUG: Item 0 content: {res[0]}")
            
        ctx = self.preacher.retrieve_global_style()
        print("Context retrieved:")
        print(ctx)
        
        self.assertIn("Similar Papers", ctx)
        if self.preacher.style_db:
             self.assertIn("Reference Presentation Styles", ctx)

    def test_retrieve_scene_style(self):
        print("\nTesting retrieve_scene_style...")
        scene_plan = {"SCENE": "Introduction", "DESCRIPTION": "Overview of 3D vision"}
        advice = self.preacher.retrieve_scene_style(scene_plan)
        print("Advice retrieved:", advice)
        self.assertTrue(len(advice) > 0)

if __name__ == '__main__':
    unittest.main()
