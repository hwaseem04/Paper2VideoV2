import fitz  # PyMuPDF
from PIL import Image
import io
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorDevice, AcceleratorOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from .textwork import _CONVERTER, _CONVERSION_CACHE

def get_specific_element(pdf_path, element_type, element_label, target_caption, image_path):
    """
    :param element_type: 'table' or 'picture'
    :param element_label: The label string (e.g., "Figure 10", "Table 2")
    :param target_caption: The descriptive caption text from the planner
    :param image_path: Path to save the extracted image
    """
    if Path(image_path).exists() and Path(image_path).stat().st_size > 0:
        return image_path

    global _CONVERTER
    pdf_key = str(pdf_path)
    
    if pdf_key in _CONVERSION_CACHE:
        raw_result = _CONVERSION_CACHE[pdf_key]
    else:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.accelerator_options.device = AcceleratorDevice.CPU
        pipeline_options.do_ocr = False
        pipeline_options.images_scale = 5.0
        pipeline_options.generate_page_images = True
        pipeline_options.generate_picture_images = True

        import utils.textwork as tw
        if tw._CONVERTER is None:
            tw._CONVERTER = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
        
        raw_result = tw._CONVERTER.convert(pdf_path)
        tw._CONVERSION_CACHE[pdf_key] = raw_result

    best_match = None
    max_score = -1

    # Normalize label for matching (e.g., "Figure 10" -> "figure 10")
    norm_label = element_label.lower().strip()
    # Also handle "Fig. 10" vs "Figure 10"
    alt_label = norm_label.replace("figure", "fig.") if "figure" in norm_label else norm_label

    elements = []
    if "table" in element_type.lower():
        elements = raw_result.document.tables
    else:
        elements = raw_result.document.pictures

    for element in elements:
        caption_text = element.caption_text(raw_result.document).lower()
        if not caption_text:
            continue
        
        score = 0
        # 1. Label Match (Highest priority)
        if norm_label in caption_text or alt_label in caption_text:
            score += 100
            # If it starts with the label, it's almost certainly the one
            if caption_text.startswith(norm_label) or caption_text.startswith(alt_label):
                score += 50
        
        # 2. Content overlap match
        target_words = set(target_caption.lower().split())
        caption_words = set(caption_text.split())
        overlap = len(target_words.intersection(caption_words))
        score += overlap

        if score > max_score:
            max_score = score
            best_match = element
    
    if best_match and max_score > 0:
        with Path(image_path).open("wb") as fp:
            best_match.get_image(raw_result.document).save(fp, "PNG")
    
    return image_path


def create_ppt_style_image( image_path, description, output_path,  width=800):
    temp_img = Image.new('RGB', (width, 10), (255, 255, 255))
    temp_draw = ImageDraw.Draw(temp_img)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 40)
        desc_font = ImageFont.truetype("arial.ttf", 24)
    except:
        # 备用默认字体
        title_font = ImageFont.load_default()
        title_font.size = 40
        desc_font = ImageFont.load_default()
        desc_font.size = 24
    
    
    # title_bbox = temp_draw.textbbox((0, 0), title, font=title_font)
    # title_height = title_bbox[3] - title_bbox[1]
    
    
    content_img = Image.open(image_path)
    content_img.thumbnail((width-100, width-100))  # 限制图片大小
    
    
    char_width = desc_font.getlength("A")  # 获取字符平均宽度
    max_chars_per_line = int((width * 0.9) // char_width)  # 每行最多字符数
    wrapped_lines = textwrap.wrap(description, width=max_chars_per_line)
    
    
    line_height = int(desc_font.size * 1.2)
    desc_height = len(wrapped_lines) * line_height
    
    
    top_margin = 50
    spacing = 30
    total_height = (top_margin + spacing + 
                   content_img.height + spacing + 
                   desc_height + top_margin)
    width = int(total_height*16/9)
    
    image = Image.new('RGB', (width, total_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    #choosable with title
    #title_x = (width - (title_bbox[2] - title_bbox[0])) // 2
    #draw.text((title_x, top_margin), title, fill="black", font=title_font)
    
    img_y = top_margin  + spacing
    img_x = (width - content_img.width) // 2
    image.paste(content_img, (img_x, img_y))
    
    
    desc_y = img_y + content_img.height + spacing
    for i, line in enumerate(wrapped_lines):
        line_bbox = draw.textbbox((0, 0), line, font=desc_font)
        line_width = line_bbox[2] - line_bbox[0]
        line_x = (width - line_width) // 2
        draw.text((line_x, desc_y + i * line_height), 
                 line, fill="black", font=desc_font)
    
    image.save(output_path)
    return output_path

def crop_pdf_page(pdf_path, page_num, crop_coords, output_path=None, dpi=72):
    """
    crop_coords: [x_min, y_min, x_max, y_max] in pixels at given dpi
    """
    doc = fitz.open(pdf_path)
    page = doc[page_num]

    scale = 72.0 / dpi
    x0, y0, x1, y1 = [c * scale for c in crop_coords]

    clip = fitz.Rect(x0, y0, x1, y1)
    page_rect = page.rect

    clip = clip & page_rect  # 交集
    if clip.is_empty:
        raise ValueError(f"Crop box {crop_coords} is outside page {page_num}")

    mat = fitz.Matrix(dpi / 72.0, dpi / 72.0)
    pix = page.get_pixmap(matrix=mat, clip=clip)

    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    if output_path:
        img.save(str(output_path))

    doc.close()
    return img if output_path is None else output_path


# pdf_path = "C:\\Users\\87719\\Desktop\\AgenticIR-main\\dataset\\ControlNet.pdf"
# page_index = 3  # 假设 FIGURE 3 在第 4 页（索引从 0 开始）
# coords = [(332.11, 81.50), (347.82, 81.50), (347.82, 97.22), (332.11, 97.22)]


# cropped_image = crop_pdf_page(pdf_path, page_index, coords)
# cropped_image.save("C:\\Users\\87719\\Desktop\\AgenticIR-main\\output\\output.png")

# cropped_image.show()




