import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import fitz # PyMuPDF
import textwrap
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip
import json
import logging

class SlideRenderer:
    def __init__(self, output_dir: Path, pdf_path: Path, tts_engine=None):
        self.output_dir = output_dir
        self.pdf_path = pdf_path
        self.tts_engine = tts_engine
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger("SlideRenderer")

        # Layout constants
        self.W = 1920
        self.H = 1080
        self.MARGIN = 60
        self.TITLE_FONT_SIZE = 80
        self.BODY_FONT_SIZE = 48
        
        # Load fonts (fallback to default if necessary)
        self.title_font = self._load_font("Arial Bold.ttf", self.TITLE_FONT_SIZE)
        self.body_font = self._load_font("Arial.ttf", self.BODY_FONT_SIZE)

    def _load_font(self, name, size):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            try:
                # macOS specific
                return ImageFont.truetype(f"/System/Library/Fonts/Supplemental/{name}", size)
            except OSError:
                return ImageFont.load_default()

    def _generate_audio(self, text, output_path):
        if not text:
             return None
        
        if self.tts_engine:
            try:
                # Assume Qwentts interface: return_audio(text) -> URL
                # Or other engine -> bytes
                # Preacher usually handles downloading if it's a URL
                # but here we are inside Renderer.
                
                # Check if tts_engine has 'return_audio' (Qwentts)
                if hasattr(self.tts_engine, 'return_audio'):
                     audio_url = self.tts_engine.return_audio(text)
                     # Download
                     import requests
                     resp = requests.get(audio_url)
                     if resp.status_code == 200:
                         with open(output_path, "wb") as f:
                             f.write(resp.content)
                         return str(output_path)
                
                # Check if it has 'synthesis' (Azure/OpenAI style?)
                # For now, just Qwentts support based on codebase
            except Exception as e:
                self.logger.error(f"TTS failed: {e}")
        
        # Fallback: create silent audio matching estimated duration?
        # Or just return None (Video will be silent duration)
        return None

    def render_scene(self, scene_plan: dict, scene_idx: int) -> str:
        """
        Render a full scene video based on the plan.
        Returns the path to the generated video file.
        """
        scene_dir = self.output_dir / f"scene_{scene_idx}"
        scene_dir.mkdir(exist_ok=True)
        
        layout = scene_plan.get("layout", {})
        elements = scene_plan.get("elements", {})
        builds = scene_plan.get("builds", [])
        
        if not builds:
             # Fallback if no builds defined (should not happen with new prompt)
             builds = [{
                 "step_index": 0,
                 "actions": [{"type": "show", "target": "all"}],
                 "audio_segment": scene_plan.get("audio_content", "")
             }]

        clips = []
        
        # Base image state
        current_img = self._create_base_slide(layout, elements)
        
        for i, build in enumerate(builds):
            # Apply build actions to current image
            current_img = self._apply_build_actions(current_img, build.get("actions", []), elements, layout)
            
            # Save frame for debugging
            frame_path = scene_dir / f"build_{i}.png"
            current_img.save(frame_path)
            
            # Generate audio for this build step
            audio_text = build.get("audio_segment", "")
            audio_path = self._generate_audio(audio_text, scene_dir / f"audio_{i}.mp3")
            
            audio_clip = None
            if audio_path and Path(audio_path).exists():
                audio_clip = AudioFileClip(str(audio_path))
                # Audio drives the duration — no truncation
                duration = audio_clip.duration
            else:
                # Fallback: use time_offset_sec to calculate duration
                current_start = build.get("time_offset_sec", 0.0)
                if i < len(builds) - 1:
                    next_start = builds[i+1].get("time_offset_sec", current_start + 2.0)
                    duration = max(0.5, next_start - current_start)
                else:
                    total_time = scene_plan.get("time_allocation_sec", 7.0)
                    duration = max(0.5, total_time - current_start)
            
            video_clip = ImageClip(str(frame_path)).set_duration(duration)
            if audio_clip:
                video_clip = video_clip.set_audio(audio_clip)
                
            clips.append(video_clip)
            
        # Concatenate
        final_clip = concatenate_videoclips(clips)
        output_path = scene_dir / f"scene{scene_idx}.mp4"
        final_clip.write_videofile(str(output_path), fps=24)
        
        return str(output_path)

    def _create_base_slide(self, layout, elements):
        img = Image.new('RGB', (self.W, self.H), (255, 255, 255)) # White background
        draw = ImageDraw.Draw(img)
        
        # Check template/regions
        regions = layout.get("regions", {})
        
        # ALWAYS draw title first if it exists
        if "title" in elements:
             title_region = regions.get("title", {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1})
             self._date_text(draw, elements["title"], title_region, self.title_font, align="center")
             
        # Other elements are drawn by _apply_build_actions dynamically?
        # OR we draw the "background" elements here?
        # The prompt says "actions: show title", "show figure". 
        # So we start blank (except maybe background color) and let builds add things.
        # But `_create_base_slide` implies the starting state.
        # Let's verify start state. Usually step 0 action is "show title".
        # So base slide is just background.
        
        return img

    def _apply_build_actions(self, img, actions, elements, layout):
        new_img = img.copy()
        draw = ImageDraw.Draw(new_img)
        regions = layout.get("regions", {})
        
        for action in actions:
            atype = action.get("type")
            target = action.get("target")
            
            if atype == "show" or atype == "fade_in":
                # Determine content and region
                content = None
                region = None
                
                if target == "title":
                    content = elements.get("title")
                    region = regions.get("title")
                    if content and region:
                        self._date_text(draw, content, region, self.title_font, align="center")
                        
                elif target == "figure":
                    fig_info = elements.get("figure")
                    region = regions.get("figure")
                    if fig_info and region:
                        self._draw_figure(new_img, fig_info, region)
                        
                elif target.startswith("bullets"):
                    # target="bullets[0]"
                    try:
                        idx = int(target.split("[")[1].strip("]"))
                        bullets = elements.get("bullets", [])
                        if idx < len(bullets):
                             content = bullets[idx]
                             region = regions.get("bullets")
                             self._draw_bullet(draw, content, region, idx, len(bullets))
                    except:
                        pass
                
                else:
                    # Generic handling for any other target
                    # Allows swapping content in a region using "content_ref"
                    # e.g. target="figure" (region), content_ref="figure_2" (element)
                    element_key = action.get("content_ref", target)
                    
                    if element_key in elements:
                        content = elements[element_key]
                        region = regions.get(target)
                        
                        if region:
                            if isinstance(content, str):
                                # Generic Text
                                # Use title font if target is title, else body
                                font = self.title_font if "title" in target.lower() else self.body_font
                                self._date_text(draw, content, region, font, align="center" if "title" in target.lower() else "left")
                                
                            elif isinstance(content, dict) and content.get("type") == "paper_figure":
                                self._draw_figure(new_img, content, region)

            elif atype == "highlight":
                 # Draw a red rectangle or similar
                 bbox = action.get("target_bbox") # [x, y, w, h] normalized
                 if bbox:
                     self._draw_highlight(draw, bbox)

        return new_img

    def _draw_figure(self, img, fig_info, region):
        # Extract figure from PDF
        # ref = "Figure 1"
        try:
            ref_text = fig_info.get('ref', '')
            # Parse number from ref string e.g. "Figure 1" -> 1
            import re
            m = re.search(r'\d+', ref_text)
            if m:
                element_num = int(m.group(0))
                # Determine type
                etype = 'image' # Must match slides.py check for 'image' in element_type
                if 'table' in ref_text.lower():
                    etype = 'table'
                
                # Temp path for extracted image
                temp_fig_path = self.output_dir / f"extracted_{element_num}.png"
                
                # Use utils.slides.get_specific_element
                from utils.slides import get_specific_element
                
                # Note: get_specific_element takes (pdf, type, num, output_path)
                # It returns the output_path
                extracted = get_specific_element(str(self.pdf_path), etype, element_num, str(temp_fig_path))
                
                if Path(extracted).exists() and Path(extracted).stat().st_size > 0:
                    # Load and draw
                    fig_img = Image.open(extracted)
                    x, y, w, h = self._to_px(region)
                    
                    # Resize to fit region while maintaining aspect ratio
                    fig_img.thumbnail((w, h), Image.Resampling.LANCZOS)
                    
                    # Center in region
                    draw_x = x + (w - fig_img.width) // 2
                    draw_y = y + (h - fig_img.height) // 2
                    
                    img.paste(fig_img, (draw_x, draw_y))
                    return

            # Fallback if extraction fails
            x, y, w, h = self._to_px(region)
            draw = ImageDraw.Draw(img)
            draw.rectangle([x, y, x+w, y+h], outline="blue", width=5)
            draw.text((x+50, y+50), f"FIGURE: {ref_text} (Extraction Failed)", fill="blue", font=self.body_font)
            
        except Exception as e:
            self.logger.error(f"Figure extraction failed: {e}")
            # Draw error placeholder
            x, y, w, h = self._to_px(region)
            draw = ImageDraw.Draw(img)
            draw.rectangle([x, y, x+w, y+h], outline="red", width=5)

        return None

    def _generate_audio(self, text, output_path):
        if not text:
             return None
        
        if self.tts_engine:
            try:
                if hasattr(self.tts_engine, 'return_audio'):
                     audio_url = self.tts_engine.return_audio(text)
                     import requests
                     resp = requests.get(audio_url)
                     if resp.status_code == 200:
                         with open(output_path, "wb") as f:
                             f.write(resp.content)
                         return str(output_path)
            except Exception as e:
                self.logger.error(f"TTS failed: {e}")
        return None

    def _draw_bullet(self, draw, text, region, index, total):
        if not region: return
        x, y, w, h = self._to_px(region)
        
        # Simple spacing
        line_height = h / (total + 1) # Distribution
        start_y = y + (index * line_height)
        
        # Draw bullet point
        draw.text((x, start_y), f"• {text}", fill="black", font=self.body_font)

    def _date_text(self, draw, text, region, font, align="left"):
        if not region: return
        x, y, w, h = self._to_px(region)
        # Center horizontally if align center
        draw_x = x
        if align == "center":
             # Estimate text width
             text_width = font.getbbox(text)[2]
             draw_x = x + (w - text_width) // 2
        draw.text((draw_x, y), text, fill="black", font=font)

    def _draw_highlight(self, draw, bbox):
        # bbox can be raw pixel coords [x1, y1, x2, y2] or normalized
        # Check if values are > 1 to determine format
        if all(v <= 1.0 for v in bbox):
            # Normalized format
            x, y, w, h = self._to_px({"x": bbox[0], "y": bbox[1], "w": bbox[2], "h": bbox[3]})
            draw.rectangle([x, y, x+w, y+h], outline="red", width=8)
        else:
            # Raw pixel coords [x1, y1, x2, y2]
            x1, y1, x2, y2 = [int(v) for v in bbox]
            draw.rectangle([x1, y1, x2, y2], outline="red", width=8)

    def _to_px(self, region):
        return (
            int(region["x"] * self.W),
            int(region["y"] * self.H),
            int(region["w"] * self.W),
            int(region["h"] * self.H)
        )
