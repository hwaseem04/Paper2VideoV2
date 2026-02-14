import cv2
import numpy as np
import json
from pathlib import Path
from typing import List, Dict, Optional
from skimage.metrics import structural_similarity as ssim
import logging
from tqdm import tqdm

from utils.logger import get_logger

class VideoProcessor:
    """
    Process reference videos to extract slide timings and build steps.
    """
    def __init__(
        self,
        fps_sample: float = 2.0,
        slide_threshold: float = 0.6, # SSIM < 0.6 implies major change (new slide)
        build_threshold_low: float = 0.85, # SSIM between 0.85 and 0.98 implies build
        build_threshold_high: float = 0.99,
        logger: Optional[logging.Logger] = None
    ):
        self.fps_sample = fps_sample
        self.slide_threshold = slide_threshold
        self.build_threshold_low = build_threshold_low
        self.build_threshold_high = build_threshold_high
        self.logger = logger or get_logger("VideoProcessor")

    def process_video(self, video_path: Path, output_dir: Optional[Path] = None) -> Dict:
        """
        Analyze video to find slides and builds.
        Returns a dict with metadata.
        """
        video_path = Path(video_path)
        if not video_path.exists():
            raise FileNotFoundError(f"Video not found: {video_path}")

        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            raise RuntimeError(f"Could not open video: {video_path}")

        video_fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / video_fps
        
        step = int(max(1, round(video_fps / self.fps_sample)))
        
        self.logger.info(f"Processing {video_path.name} ({duration:.1f}s) at step {step}...")

        slides = []
        current_slide = {
            "slide_id": 0,
            "t_start": 0.0,
            "builds": [{"t": 0.0, "type": "base"}],
            "keyframes": []
        }
        
        prev_frame_gray = None
        frame_idx = 0
        
        # We'll save keyframes if output_dir is provided
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)

        pbar = tqdm(total=total_frames)
        
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            if not ret:
                break
            
            timestamp = frame_idx / video_fps
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            if prev_frame_gray is not None:
                # Compute SSIM
                try:
                    score, _ = ssim(prev_frame_gray, gray, full=True)
                except ValueError:
                    # Frame too small?
                    score = 1.0

                # Detect Transitions
                if score < self.slide_threshold:
                    # New Slide
                    current_slide["t_end"] = timestamp
                    slides.append(current_slide)
                    
                    self.logger.info(f"New Slide at {timestamp:.2f}s (Score: {score:.3f})")
                    
                    current_slide = {
                        "slide_id": len(slides),
                        "t_start": timestamp,
                        "builds": [{"t": timestamp, "type": "base"}],
                        "keyframes": []
                    }
                    
                    # Save keyframe for new slide
                    if output_dir:
                        kf_path = output_dir / f"slide_{current_slide['slide_id']}_start.jpg"
                        cv2.imwrite(str(kf_path), frame)
                        current_slide["keyframes"].append({"t": timestamp, "path": str(kf_path)})

                elif (score < self.build_threshold_high) and (score > self.build_threshold_low):
                    # Potential Build Step
                    # We might want to debounce this, but for now just log it
                    # Only record if it's been > 1 second since last build to avoid noise
                    last_build_time = current_slide["builds"][-1]["t"]
                    if (timestamp - last_build_time) > 1.0:
                        self.logger.info(f"Build Step at {timestamp:.2f}s (Score: {score:.3f})")
                        current_slide["builds"].append({"t": timestamp, "type": "addition"})
                        
                        if output_dir:
                            kf_path = output_dir / f"slide_{current_slide['slide_id']}_build_{len(current_slide['builds'])}.jpg"
                            cv2.imwrite(str(kf_path), frame)

            else:
                 # First frame
                 if output_dir:
                    kf_path = output_dir / f"slide_0_start.jpg"
                    cv2.imwrite(str(kf_path), frame)
                    current_slide["keyframes"].append({"t": 0.0, "path": str(kf_path)})

            prev_frame_gray = gray
            frame_idx += step
            pbar.update(step)
            
        pbar.close()
        cap.release()
        
        # Close last slide
        current_slide["t_end"] = duration
        slides.append(current_slide)
        
        result = {
            "video_id": video_path.stem,
            "duration": duration,
            "fps_sampled": self.fps_sample,
            "slides": slides
        }
        
        if output_dir:
            with open(output_dir / "metadata.json", "w") as f:
                json.dump(result, f, indent=2)
                
        return result

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("VideoProcessor initialized.")
