import sys
from pathlib import Path
import json

# Add current directory to sys.path to ensure imports work
# We need to find the root of the project.
project_root = Path(__file__).parent.resolve()
sys.path.append(str(project_root))

from pipeline.preacher import Preacher
from utils.textwork import _load_json_dict

def main():
    input_path = (project_root / 'dataset/ego3d.pdf').resolve()
    output_dir = (project_root / 'tests/output/regression').resolve()
    llm_config_path = (project_root / 'config.yml').resolve()

    print(f"Input: {input_path}")
    print(f"Output: {output_dir}")
    print(f"Config: {llm_config_path}")

    try:
        agent = Preacher(
            input_path=input_path, output_dir=output_dir, llm_config_path=llm_config_path,
            plan_by='GEMINI',
            eval_by='GEMINI',
            art_work='GEMINI',
            with_example=False,
            with_reflection=False,
            with_rollback=False,
            silent=False,
        )
    except Exception as e:
        print(f"Failed to initialize Preacher: {e}")
        import traceback
        traceback.print_exc()
        return

    # 1. High Planning
    print("Starting High Planning...")
    try:
        # Check if high plan exists to avoid re-generating it
        if agent.high_plan_path.exists():
             with open(agent.high_plan_path, 'r') as f:
                 agent.high_plan = f.read()
        else:
             agent.high_plan = agent.high_planning()
    except Exception as e:
        print(f"High planning failed: {e}")
        import traceback
        traceback.print_exc()
        return

    # 2. Parse High Plan
    try:
        agent.high_plan_list = _load_json_dict(agent.high_plan)
        
        # Handle string wrapping (logic copied from Preacher.run)
        if agent.high_plan_list is None or (isinstance(agent.high_plan_list, str)):
            try:
                unwrapped = json.loads(agent.high_plan) if isinstance(agent.high_plan, str) else agent.high_plan
                agent.high_plan_list = _load_json_dict(unwrapped)
            except Exception:
                pass
    except Exception as e:
        print(f"Failed to parse high plan: {e}")
        return

    # Ensure list
    if isinstance(agent.high_plan_list, dict):
         # Sometimes LLM returns dict with key "scenes" or similar
         found = False
         for key, v in agent.high_plan_list.items():
             if isinstance(v, list):
                 agent.high_plan_list = v
                 found = True
                 break
         if not found:
             # Try to wrap it if it's a single scene dict? 
             # Or just error out.
             print(f"Warning: High plan is a dict but no list value found. Keys: {agent.high_plan_list.keys()}")

    if not isinstance(agent.high_plan_list, list):
        print(f"Error: High plan is not a list: {type(agent.high_plan_list)}")
        print(agent.high_plan_list)
        return

    # 3. TRUNCATE TO ONE SCENE
    print(f"Plan has {len(agent.high_plan_list)} scenes. Processing all.")
    # agent.high_plan_list = agent.high_plan_list[:1]
    
    # 4. Low Planning Loop
    # Preacher.run initializes final_plan as list of dicts.
    agent.final_plan = []
    print("Starting Low Planning...")
    for i in range(len(agent.high_plan_list)):
        agent.final_plan.append({})
        agent.scene_idx = i
        try:
            agent.low_planning(agent.high_plan_list[i])
        except Exception as e:
            print(f"Error in low planning for scene {i}: {e}")
            import traceback
            traceback.print_exc()

    # 5. Generation Loop
    agent.video_list = []
    print("Starting Generation...")
    for i in range(len(agent.high_plan_list)):
        agent.scene_idx = i
        
        # Check if scene dir exists and clean it?
        # Preacher.generate_ creates it.
        
        print(f"Generating scene {i}...")
        try:
            agent.generate_(i)
            # Check if video was created
            # The path construction depends on internal logic of generate_
            # But generate_ returns video_path.
            # Wait, generate_ returns video_path, but it might just return url or something depending on handler.
            # But line 466 appending assumes a path.
            
            video_path = agent.work_dir / f"scene_{agent.scene_idx}" / "scene{}.mp4".format(agent.scene_idx)
            if video_path.exists():
                print(f"Scene {i} video generated at: {video_path}")
                agent.video_list.append(video_path)
            else:
                 # Check if generate_ returned a different path?
                 # pipeline/preacher.py:L626 returns video_path
                 # But we didn't capture return value in the loop in Preacher.run (line 465 just calls self.generate_(i)).
                 # Wait, line 465: self.generate_(i)
                 # line 466: self.video_list.append(self.work_dir / ... )
                 
                 print(f"Scene {i} video NOT found at: {video_path}")
                 
        except Exception as e:
            print(f"Error generating scene {i}: {e}")
            import traceback
            traceback.print_exc()

    print('REGRESSION COMPLETE')
    
    # 6. Concatenate Videos
    if agent.video_list:
        print(f"Concatenating {len(agent.video_list)} scenes...")
        final_output = agent.work_dir / "final_video.mp4"
        try:
            from utils.videowork import concatenate_videos
            concatenate_videos(agent.video_list, final_output)
            if final_output.exists():
                print(f"FINAL VIDEO GENERATED: {final_output}")
            else:
                print("Error: Final video file not found after concatenation.")
        except Exception as e:
            print(f"Error concatenating videos: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("No videos generated to concatenate.")

if __name__ == "__main__":
    main()
