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
        # Title page fonts
        self.title_page_font = self._load_font("Arial Bold.ttf", 64)
        self.author_font = self._load_font("Arial.ttf", 36)
        self.affiliation_font = self._load_font("Arial.ttf", 28)
        self.venue_font = self._load_font("Arial Bold.ttf", 32)

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
        
        # Check if this is a title page
        template = layout.get("template", "")
        if template == "title_page":
            current_img = self._render_title_page(elements, layout)
        else:
            # Base image state
            current_img = self._create_base_slide(layout, elements)
        
        # Track all visible bullets across builds to prevent overlap
        all_visible_bullets = set()

        for i, build in enumerate(builds):
            # Apply build actions to current image
            current_img, all_visible_bullets = self._apply_build_actions(
                current_img, build.get("actions", []), elements, layout, all_visible_bullets
            )
            
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

    def _render_title_page(self, elements, layout):
        """Render a title page with paper title, authors, affiliations, venue, and logos."""
        bg_color = layout.get("background_color", "#FFFFFF")
        img = Image.new('RGB', (self.W, self.H), bg_color)
        draw = ImageDraw.Draw(img)
        regions = layout.get("regions", {})
        
        # --- Draw paper title (with text wrapping) ---
        title_text = elements.get("title", "")
        if title_text and "title" in regions:
            title_region = regions["title"]
            tx, ty, tw, th = self._to_px(title_region)
            
            # Wrap title text to fit region width
            lines = self._wrap_text(title_text, tw, self.title_page_font)
            line_height = self.title_page_font.getbbox("Ay")[3] + 8
            
            # Center vertically within region
            total_text_height = len(lines) * line_height
            start_y = ty + max(0, (th - total_text_height) // 2)
            
            for line in lines:
                line_bbox = self.title_page_font.getbbox(line)
                line_w = line_bbox[2] - line_bbox[0]
                line_x = tx + (tw - line_w) // 2  # Center each line
                draw.text((line_x, start_y), line, fill="black", font=self.title_page_font)
                start_y += line_height
        
        # --- Draw authors ---
        authors_text = elements.get("authors", "")
        if authors_text and "authors" in regions:
            authors_region = regions["authors"]
            ax, ay, aw, ah = self._to_px(authors_region)
            
            # Wrap if too wide
            lines = self._wrap_text(authors_text, aw, self.author_font)
            line_height = self.author_font.getbbox("Ay")[3] + 6
            total_h = len(lines) * line_height
            start_y = ay + max(0, (ah - total_h) // 2)
            
            for line in lines:
                line_bbox = self.author_font.getbbox(line)
                line_w = line_bbox[2] - line_bbox[0]
                line_x = ax + (aw - line_w) // 2
                draw.text((line_x, start_y), line, fill=(60, 60, 60), font=self.author_font)
                start_y += line_height
        
        # --- Draw affiliations ---
        aff_text = elements.get("affiliations", "")
        if aff_text and "affiliations" in regions:
            aff_region = regions["affiliations"]
            fx, fy, fw, fh = self._to_px(aff_region)
            
            aff_bbox = self.affiliation_font.getbbox(aff_text)
            aff_w = aff_bbox[2] - aff_bbox[0]
            aff_x = fx + (fw - aff_w) // 2
            aff_y = fy + (fh - (aff_bbox[3] - aff_bbox[1])) // 2
            draw.text((aff_x, aff_y), aff_text, fill=(100, 100, 100), font=self.affiliation_font)
        
        # --- Draw venue ---
        venue_text = elements.get("venue", "")
        if venue_text and "venue" in regions:
            venue_region = regions["venue"]
            vx, vy, vw, vh = self._to_px(venue_region)
            
            venue_bbox = self.venue_font.getbbox(venue_text)
            venue_w = venue_bbox[2] - venue_bbox[0]
            venue_x = vx + (vw - venue_w) // 2
            venue_y = vy + (vh - (venue_bbox[3] - venue_bbox[1])) // 2
            draw.text((venue_x, venue_y), venue_text, fill=(40, 40, 40), font=self.venue_font)
        
        # --- Place conference logo ---
        conf_logo = elements.get("conference_logo")
        if conf_logo and isinstance(conf_logo, dict) and "conference_logo" in regions:
            self._place_logo(img, conf_logo.get("path", ""), regions["conference_logo"])
        
        # --- Place affiliation logos ---
        aff_logos = elements.get("affiliation_logos", [])
        if aff_logos and isinstance(aff_logos, list) and "affiliation_logos" in regions:
            aff_region = regions["affiliation_logos"]
            rx, ry, rw, rh = self._to_px(aff_region)
            
            # Space logos evenly across the region
            n_logos = len(aff_logos)
            if n_logos > 0:
                slot_w = rw // n_logos
                for i, logo_info in enumerate(aff_logos):
                    if isinstance(logo_info, dict):
                        logo_path = logo_info.get("path", "")
                    else:
                        logo_path = str(logo_info)
                    
                    # Create a sub-region for this logo
                    sub_region = {
                        "x": aff_region["x"] + (i * aff_region["w"] / n_logos),
                        "y": aff_region["y"],
                        "w": aff_region["w"] / n_logos,
                        "h": aff_region["h"],
                    }
                    self._place_logo(img, logo_path, sub_region)
        
        return img
    
    def _place_logo(self, img, logo_path, region):
        """Place a logo image into the given region, preserving aspect ratio."""
        if not logo_path or not Path(logo_path).exists():
            return
        
        try:
            logo = Image.open(logo_path)
            # Convert to RGBA if needed
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
            
            rx, ry, rw, rh = self._to_px(region)
            
            # Scale logo to fit region while preserving aspect ratio
            logo_ratio = logo.width / logo.height
            region_ratio = rw / rh
            
            if logo_ratio > region_ratio:
                new_w = int(rw * 0.9)  # 90% of region width
                new_h = int(new_w / logo_ratio)
            else:
                new_h = int(rh * 0.9)
                new_w = int(new_h * logo_ratio)
            
            if new_w < 1 or new_h < 1:
                return
            
            logo = logo.resize((new_w, new_h), Image.LANCZOS)
            
            # Center in region
            paste_x = rx + (rw - new_w) // 2
            paste_y = ry + (rh - new_h) // 2
            
            # Paste with transparency
            img.paste(logo, (paste_x, paste_y), logo if logo.mode == 'RGBA' else None)
            
        except Exception as e:
            self.logger.warning(f"Failed to place logo {logo_path}: {e}")

    def _apply_build_actions(self, img, actions, elements, layout, cumulative_visible_bullets=None):
        new_img = img.copy()
        draw = ImageDraw.Draw(new_img)
        regions = layout.get("regions", {})

        # Track cumulative visible bullets across all builds
        if cumulative_visible_bullets is None:
            cumulative_visible_bullets = set()

        # Collect new bullet indices from this build's actions
        for action in actions:
            atype = action.get("type")
            target = action.get("target")

            if (atype == "show" or atype == "fade_in") and target and target.startswith("bullets"):
                try:
                    idx = int(target.split("[")[1].strip("]"))
                    cumulative_visible_bullets.add(idx)
                except:
                    pass

        # Render non-bullet actions
        for action in actions:
            atype = action.get("type")
            target = action.get("target")

            # Skip bullet actions (handled separately below)
            if target and target.startswith("bullets"):
                continue

            if atype == "show" or atype == "fade_in":
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

                else:
                    # Generic handling for any other target
                    element_key = action.get("content_ref", target)

                    if element_key in elements:
                        content = elements[element_key]
                        region = regions.get(target)

                        if region:
                            if isinstance(content, str):
                                font = self.title_font if "title" in target.lower() else self.body_font
                                self._date_text(draw, content, region, font, align="center" if "title" in target.lower() else "left")

                            elif isinstance(content, dict) and content.get("type") == "paper_figure":
                                self._draw_figure(new_img, content, region)

            elif atype == "highlight":
                 bbox = action.get("target_bbox")
                 if bbox:
                     self._draw_highlight(draw, bbox)

        # Redraw ALL visible bullets in correct stacked positions
        # This clears and redraws the bullet region to prevent overlap
        if cumulative_visible_bullets:
            bullets = elements.get("bullets", [])
            bullet_region = regions.get("bullets")

            if bullet_region and bullets:
                # Clear the bullet region first (fill with background color)
                bx, by, bw, bh = self._to_px(bullet_region)
                bg_color = layout.get("background_color", "#FFFFFF")
                draw.rectangle([bx, by, bx + bw, by + bh], fill=bg_color)

                bullet_y_offset = 0

                for idx in sorted(cumulative_visible_bullets):
                    if idx < len(bullets):
                        content = bullets[idx]
                        height_used = self._draw_bullet(draw, content, bullet_region, bullet_y_offset)
                        bullet_y_offset += height_used + 10

        return new_img, cumulative_visible_bullets

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

    def _draw_bullet(self, draw, text, region, bullet_y_offset=0):
        """
        Draw a bullet point with automatic text wrapping.

        Args:
            draw: PIL ImageDraw object
            text: Bullet text content
            region: Region dictionary with normalized coordinates
            bullet_y_offset: Y offset in pixels from region top (for dynamic positioning)

        Returns:
            Height in pixels consumed by this bullet (including wrapping)
        """
        if not region:
            return 0

        x, y, w, h = self._to_px(region)

        # Constants for bullet formatting
        BULLET_CHAR = "• "
        BULLET_INDENT = 30  # Pixels for bullet character
        LINE_SPACING = 1.15  # Standard line spacing (like Google Slides default)

        # Calculate available width for text (excluding bullet character)
        available_width = w - BULLET_INDENT - 20  # 20px right margin

        # Get font metrics for proper line height calculation
        # Use ascent + descent for accurate font height
        try:
            ascent, descent = self.body_font.getmetrics()
            font_height = ascent + descent
        except AttributeError:
            # Fallback: use bounding box if getmetrics not available
            bbox = self.body_font.getbbox("Ay")
            font_height = bbox[3] - bbox[1]

        # Apply standard line spacing (1.15x like Google Slides)
        line_height = int(font_height * LINE_SPACING)

        # Word-wrap the text
        wrapped_lines = self._wrap_text(text, available_width, self.body_font)

        # Calculate starting position
        current_y = y + bullet_y_offset

        # Draw bullet character on first line
        draw.text((x, current_y), BULLET_CHAR, fill="black", font=self.body_font)

        # Draw text lines with proper indentation
        for i, line in enumerate(wrapped_lines):
            if i == 0:
                # First line: positioned after bullet
                text_x = x + BULLET_INDENT
            else:
                # Wrapped lines: indented to align with first line text
                text_x = x + BULLET_INDENT

            draw.text((text_x, current_y), line, fill="black", font=self.body_font)
            current_y += line_height

        # Return total height consumed
        total_height = len(wrapped_lines) * line_height
        return total_height

    def _wrap_text(self, text, max_width, font):
        """
        Wrap text to fit within max_width using the given font.

        Args:
            text: Text to wrap
            max_width: Maximum width in pixels
            font: PIL ImageFont object

        Returns:
            List of wrapped text lines
        """
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            # Test if adding this word exceeds max width
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            text_width = bbox[2] - bbox[0]

            if text_width <= max_width:
                current_line.append(word)
            else:
                # Current line is full, start new line
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # Single word is too long, force it on its own line
                    lines.append(word)
                    current_line = []

        # Add remaining words
        if current_line:
            lines.append(' '.join(current_line))

        return lines if lines else [text]

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
