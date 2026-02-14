import sys
from pathlib import Path
import logging
import json
from tqdm import tqdm

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from tools.video_processor import VideoProcessor
from utils.logger import get_logger

def build_style_db(limit=None):
    logging.basicConfig(level=logging.INFO)
    logger = get_logger("StyleDB_Builder")
    
    ref_dir = Path("data_reference/final")
    output_base = Path("data_reference/style_db")
    output_base.mkdir(parents=True, exist_ok=True)
    
    if not ref_dir.exists():
        logger.error(f"Reference directory {ref_dir} not found.")
        return

    # Find videos
    # Assuming video files are .mp4
    videos = list(ref_dir.rglob("*.mp4"))
    
    if limit:
        videos = videos[:limit]
        
    logger.info(f"Found {len(videos)} videos to process.")
    
    processor = VideoProcessor(fps_sample=2.0)
    
    summary = []
    
    for video_path in tqdm(videos, desc="Processing Videos"):
        try:
            # Create a folder for this video's style data
            # Use video stem as ID
            video_id = video_path.stem
            safe_video_id = "".join([c if c.isalnum() or c in "-_" else "_" for c in video_id])
            
            video_output_dir = output_base / safe_video_id
            
            # Skip if already processed?
            if (video_output_dir / "metadata.json").exists():
                logger.info(f"Skipping {video_id} (already processed)")
                with open(video_output_dir / "metadata.json", "r") as f:
                    data = json.load(f)
                summary.append({
                    "video_id": video_id,
                    "slides_count": len(data.get("slides", [])),
                    "path": str(video_output_dir)
                })
                continue

            data = processor.process_video(video_path, output_dir=video_output_dir)
            
            summary.append({
                "video_id": video_id,
                "slides_count": len(data.get("slides", [])),
                "path": str(video_output_dir)
            })
            
        except Exception as e:
            logger.error(f"Failed to process {video_path.name}: {e}")
            
    # Save global summary
    with open(output_base / "db_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
        
    logger.info(f"Style DB built at {output_base}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="Limit number of videos to process")
    args = parser.parse_args()
    
    build_style_db(limit=args.limit)
