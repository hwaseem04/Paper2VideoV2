import sys
from pathlib import Path
import logging
import cv2

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from tools.video_processor import VideoProcessor

def test_video_processor():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("TestVideoProcessor")
    
    ref_dir = Path("data_reference/final")
    if not ref_dir.exists():
        logger.error("Reference directory not found.")
        return

    # Find a sample video (mp4)
    videos = list(ref_dir.rglob("*.mp4"))
    if not videos:
        logger.error("No videos found in data_reference/final.")
        return

    sample_video = videos[0]
    logger.info(f"Testing on video: {sample_video.name}")

    # Initialize Processor
    processor = VideoProcessor(fps_sample=1.0) # Low FPS for speed
    
    output_dir = Path("output/test_video_process")
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        data = processor.process_video(sample_video, output_dir=output_dir)
        
        # Validation
        logger.info(f"Duration: {data['duration']:.2f}s")
        logger.info(f"Detected {len(data['slides'])} slides.")
        
        for slide in data['slides'][:5]:
            logger.info(f"Slide {slide['slide_id']}: {slide['t_start']:.2f}s - {slide.get('t_end', '?')}s | Builds: {len(slide['builds'])}")
            
        if len(data['slides']) > 0:
            logger.info("SUCCESS: Slides detected.")
        else:
            logger.warning("FAILURE: No slides detected.")
            
    except Exception as e:
        logger.error(f"Processing failed: {e}", exc_info=True)

if __name__ == "__main__":
    test_video_processor()
