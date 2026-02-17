_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

_Note: These user-assistant interactions are independent and the system message is always attached in each turn for GPT._

**System message for GPT**

You are an expert in reading academic papers and creating video summaries based on them. 

**Question**

Given a paper, please design a video summary. 
The number of scenes should be based on the RECOMMENDATION in the style context below.

## Similar Papers found in specific domain:
- 3DInAction- Understanding Human Actions in 3D Point Clouds
- Pos3R- 6D Pose Estimation for Unseen Objects Made Easy
- CVPR_CVPR-2025_Highlight-SLAM3R-Real-Time-Dense-Scene-Reconstruction-from-Mon__CVPR-2025-Highlight-SLAM3R-Real-Time-Den

## Reference Presentation Styles (from existing videos):
- Video '3DInAction- Understanding Human Actions in 3D Point Clouds': approx 3 slides, 16.0 builds/slide.
- Video 'Pos3R- 6D Pose Estimation for Unseen Objects Made Easy': approx 3 slides, 1.7 builds/slide.
- Video 'CVPR_CVPR-2025_Highlight-SLAM3R-Real-Time-Dense-Scene-Reconstruction-from-Mon__CVPR-2025-Highlight-SLAM3R-Real-Time-Den': approx 1 slides, 50.0 builds/slide.

RECOMMENDATION: Target approximately 4 scenes (Calculated from 10 pages of content and reference styles).

Requirements: 
1. Each scene must include strong relationship between last and next scene.
2. No overlapping content between scenes.
3. Collectively present all key findings in a coherent narrative.
4. Maintain high technical accuracy and professionalism.
5. Allow 5 to 10 seconds of video per scene.
6. Deliver only core content; omit acknowledgements and references.
7. Do NOT create a title/introduction scene. Scene 0 (title page with paper title, authors, logos) is auto-generated separately. Start your scenes from the paper's technical content.

You MUST output the scenes in the following STRICT JSON format (list of objects):
```json
[
  {
    "scene_id": 1,
    "title": "Brief title",
    "summary": "Scene description and content summary.",
    "paper_section": "Introduction/Method/etc",
    "narrative_role": "problem/solution/result/etc",
    "time_allocation_sec": 5,
    "target_layout": "two_col_fig_left/full_fig_with_callouts/etc",
    "text_density": "low/medium/high",
    "visual_density": "medium/high",
    "uses_builds": true,
    "expected_build_steps": 2,
    "primary_sources": ["Figure 1", "Section 1"],
    "reference_style_examples": []
  },
  ...
]
```
Do NOT just acknowledge this request. Generate the actual scene list NOW. Ensure strictly valid JSON.

**Answer (from GEMINI)**

"""```json
[
  {
    "scene_id": 1,
    "title": "The Gap in 3D Action Recognition",
    "summary": "Highlights the scarcity of ego-view 3D point cloud datasets compared to RGB. While existing 3D datasets use static sensors or focus on full-body motion, there is a critical need for fine-grained, ego-centric 3D data for AR and wearable applications.",
    "paper_section": "1. Introduction",
    "narrative_role": "problem",
    "time_allocation_sec": 8,
    "target_layout": "two_col_fig_right",
    "text_density": "medium",
    "visual_density": "medium",
    "uses_builds": true,
    "expected_build_steps": 3,
    "primary_sources": ["Table 1", "Section 2.1"],
    "reference_style_examples": ["3DInAction- Understanding Human Actions in 3D Point Clouds"]
  },
  {
    "scene_id": 2,
    "title": "IKEA Ego 3D Dataset Overview",
    "summary": "Introduces the IKEA Ego 3D dataset: 174 assembly sequences captured via HoloLens 2, featuring 493k frames and 56 atomic action classes. Shows the pipeline from RGB-D capture to aligned 3D point cloud sequences.",
    "paper_section": "3. The IKEA Ego3D dataset",
    "narrative_role": "solution",
    "time_allocation_sec": 10,
    "target_layout": "full_fig_with_callouts",
    "text_density": "low",
    "visual_density": "high",
    "uses_builds": true,
    "expected_build_steps": 4,
    "primary_sources": ["Figure 1", "Section 3.1"],
    "reference_style_examples": ["CVPR_CVPR-2025_Highlight-SLAM3R-Real-Time-Dense-Scene-Reconstruction-from-Mon__CVPR-2025-Highlight-SLAM3R-Real-Time-Den"]
  },
  {
    "scene_id": 3,
    "title": "Fine-Grained Actions & Challenges",
    "summary": "Visualizes the diversity of furniture (LACK, KALLAX, BEKVAM) and the complexity of actions like 'spin screwdriver' or 'attach side panel'. Discusses unique challenges: ego-view camera motion, frequent occlusions, and class imbalance.",
    "paper_section": "3.5 Dataset unique challenges",
    "narrative_role": "technical_detail",
    "time_allocation_sec": 8,
    "target_layout": "grid_2x2",
    "text_density": "medium",
    "visual_density": "high",
    "uses_builds": true,
    "expected_build_steps": 2,
    "primary_sources": ["Figure 2", "Figure 3", "Figure 4"],
    "reference_style_examples": ["Pos3R- 6D Pose Estimation for Unseen Objects Made Easy"]
  },
  {
    "scene_id": 4,
    "title": "Benchmarking SOTA Methods",
    "summary": "Presents evaluation results for state-of-the-art 3D action recognition methods. Key findings show that temporal smoothing significantly boosts performance and that hierarchical verb-noun decomposition helps decouple spatial and temporal representation power.",
    "paper_section": "4. Benchmark and Experiments",
    "narrative_role": "result",
    "time_allocation_sec": 9,
    "target_layout": "two_col_fig_left",
    "text_density": "high",
    "visual_density": "medium",
    "uses_builds": true,
    "expected_build_steps": 3,
    "primary_sources": ["Table 2", "Table 3", "Table 4"],
    "reference_style_examples": ["3DInAction- Understanding Human Actions in 3D Point Clouds"]
  }
]
```"""

Token usage so far: 5852 prompt tokens, 965 completion tokens

Cost so far: $0.08747

**Question**

You are an expert at reading academic papers.

Look at the FIRST PAGE of this paper and extract the following metadata:

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "paper_title": "The full paper title exactly as written",
  "authors": [
    {{"name": "First Author", "affiliation_id": 1}},
    {{"name": "Second Author", "affiliation_id": 2}}
  ],
  "affiliations": [
    {{"id": 1, "name": "University or Organization Name", "email_domain": "example.edu"}},
    {{"id": 2, "name": "Company Name", "email_domain": "company.com"}}
  ],
  "venue": "Conference or Journal Name and Year (e.g. CVPR 2025)"
}}

## STRICT RULES:
1. Extract the paper title EXACTLY as it appears — do not paraphrase.
2. List ALL authors in order. Use their full names as written.
3. Each author must have an affiliation_id matching one entry in the affiliations list.
4. For affiliations, extract the email domain from author emails if available (e.g. user@nvidia.com → nvidia.com).
5. If no email is visible, leave email_domain as an empty string.
6. For venue, look for conference/journal name (e.g. "CVPR 2025", "NeurIPS 2024", "ICLR 2025"). If not found, use empty string.
7. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "paper_title": "IKEA Ego 3D Dataset: Understanding furniture assembly actions from ego-view 3D Point Clouds",
  "authors": [
    {"name": "Yizhak Ben-Shabat", "affiliation_id": 1},
    {"name": "Jonathan Paul", "affiliation_id": 2},
    {"name": "Eviatar Segev", "affiliation_id": 2},
    {"name": "Oren Shrout", "affiliation_id": 2},
    {"name": "Stephen Gould", "affiliation_id": 1}
  ],
  "affiliations": [
    {"id": 1, "name": "Australian National University", "email_domain": "anu.edu.au"},
    {"id": 2, "name": "Technion, Israel Institute of Technology", "email_domain": "gmail.com"}
  ],
  "venue": "WACV 2023"
}"""

Token usage so far: 11415 prompt tokens, 1185 completion tokens

Cost so far: $0.14970

**Question**

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "IKEA Ego 3D Dataset: Understanding furniture assembly actions from ego-view 3D Point Clouds",
  "authors": [
    {
      "name": "Yizhak Ben-Shabat",
      "affiliation_id": 1
    },
    {
      "name": "Jonathan Paul",
      "affiliation_id": 2
    },
    {
      "name": "Eviatar Segev",
      "affiliation_id": 2
    },
    {
      "name": "Oren Shrout",
      "affiliation_id": 2
    },
    {
      "name": "Stephen Gould",
      "affiliation_id": 1
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Australian National University",
      "email_domain": "anu.edu.au"
    },
    {
      "id": 2,
      "name": "Technion, Israel Institute of Technology",
      "email_domain": "gmail.com"
    }
  ],
  "venue": "WACV 2023"
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Australian National University)
affiliation_2_logo: affiliation_2.png (Technion, Israel Institute of Technology)

Design a visually clean, professional title page layout. Use the reference style of academic presentation title slides:
- Conference logo in a top corner
- Affiliation logos grouped together (top row or below authors)
- Paper title large and centered
- Authors centered below title
- Affiliation text small, centered
- Venue name at bottom

IMPORTANT: Vary the placement naturally — do NOT always put logos in the same position. Sometimes conference logo goes top-left, sometimes top-right. Sometimes affiliation logos go in the top row, sometimes below authors. Be creative but professional.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "title_page",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "conference_logo": {"x": 0.0, "y": 0.0, "w": 0.15, "h": 0.12},
    "affiliation_logos": {"x": 0.5, "y": 0.0, "w": 0.45, "h": 0.12},
    "title": {"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25},
    "authors": {"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.12},
    "affiliations": {"x": 0.1, "y": 0.7, "w": 0.8, "h": 0.08},
    "venue": {"x": 0.3, "y": 0.82, "w": 0.4, "h": 0.06}
  },
  "style_rationale": "Brief explanation of why this positioning works."
}

## STRICT RULES:
1. All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
2. If no conference logo is available, omit the conference_logo region.
3. If no affiliation logos are available, omit the affiliation_logos region.
4. The title region should be generous — wide enough for long titles to wrap.
5. Keep at least 5% margin from all edges.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "title_page",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "conference_logo": {"x": 0.8, "y": 0.05, "w": 0.15, "h": 0.1},
    "affiliation_logos": {"x": 0.05, "y": 0.05, "w": 0.3, "h": 0.1},
    "title": {"x": 0.05, "y": 0.25, "w": 0.9, "h": 0.25},
    "authors": {"x": 0.1, "y": 0.55, "w": 0.8, "h": 0.1},
    "affiliations": {"x": 0.1, "y": 0.68, "w": 0.8, "h": 0.08},
    "venue": {"x": 0.3, "y": 0.85, "w": 0.4, "h": 0.05}
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum readability, with a clear vertical hierarchy for authors, affiliation text, and the venue at the bottom."
}"""

Token usage so far: 17510 prompt tokens, 1529 completion tokens

Cost so far: $0.22097

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 1,
  "title": "The Gap in 3D Action Recognition",
  "summary": "Highlights the scarcity of ego-view 3D point cloud datasets compared to RGB. While existing 3D datasets use static sensors or focus on full-body motion, there is a critical need for fine-grained, ego-centric 3D data for AR and wearable applications.",
  "paper_section": "1. Introduction",
  "narrative_role": "problem",
  "time_allocation_sec": 8,
  "target_layout": "two_col_fig_right",
  "text_density": "medium",
  "visual_density": "medium",
  "uses_builds": true,
  "expected_build_steps": 3,
  "primary_sources": [
    "Table 1",
    "Section 2.1"
  ],
  "reference_style_examples": [
    "3DInAction- Understanding Human Actions in 3D Point Clouds"
  ]
}

Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "The field of action recognition faces a significant disparity between the abundance of ego-view RGB datasets and the scarcity of 3D point cloud counterparts. Existing 3D datasets are primarily limited by two factors: the use of static, distant sensors and a focus on coarse, full-body motions. Static sensors (like those in NTU RGB+D or IKEA-ASM) fail to capture the camera motion inherent in wearable device scenarios and lack the resolution to distinguish fine-grained interactions with small objects. Furthermore, while datasets like EPIC-Kitchens provide ego-view data, they lack the 3D modality necessary for scenarios where RGB is degraded (e.g., poor lighting) or where spatial redundancy is required for safety-critical AR/VR applications. There is a critical need for datasets that provide fine-grained, ego-centric 3D point clouds to support the development of algorithms for head-mounted devices like HoloLens 2 or Apple Vision Pro.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "This table explicitly illustrates the 'gap' by showing that while other datasets have either 3D data or an ego-view, only the proposed IKEA Ego 3D dataset provides both in an assembly context."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "1. Introduction",
    "2.1. 3D action understanding datasets"
  ]
}"""

Token usage so far: 23369 prompt tokens, 1890 completion tokens

Cost so far: $0.29039

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The field of action recognition faces a significant disparity between the abundance of ego-view RGB datasets and the scarcity of 3D point cloud counterparts. Existing 3D datasets are primarily limited by two factors: the use of static, distant sensors and a focus on coarse, full-body motions. Static sensors (like those in NTU RGB+D or IKEA-ASM) fail to capture the camera motion inherent in wearable device scenarios and lack the resolution to distinguish fine-grained interactions with small objects. Furthermore, while datasets like EPIC-Kitchens provide ego-view data, they lack the 3D modality necessary for scenarios where RGB is degraded (e.g., poor lighting) or where spatial redundancy is required for safety-critical AR/VR applications. There is a critical need for datasets that provide fine-grained, ego-centric 3D point clouds to support the development of algorithms for head-mounted devices like HoloLens 2 or Apple Vision Pro.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "This table explicitly illustrates the 'gap' by showing that while other datasets have either 3D data or an ego-view, only the proposed IKEA Ego 3D dataset provides both in an assembly context."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "1. Introduction",
    "2.1. 3D action understanding datasets"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 1,
  "title": "The Gap in 3D Action Recognition",
  "summary": "Highlights the scarcity of ego-view 3D point cloud datasets compared to RGB. While existing 3D datasets use static sensors or focus on full-body motion, there is a critical need for fine-grained, ego-centric 3D data for AR and wearable applications.",
  "paper_section": "1. Introduction",
  "narrative_role": "problem",
  "time_allocation_sec": 8,
  "target_layout": "two_col_fig_right",
  "text_density": "medium",
  "visual_density": "medium",
  "uses_builds": true,
  "expected_build_steps": 3,
  "primary_sources": [
    "Table 1",
    "Section 2.1"
  ],
  "reference_style_examples": [
    "3DInAction- Understanding Human Actions in 3D Point Clouds"
  ]
}

Reference style advice:
General Content: Default to 'two_col_bullets_left' if a figure is available, otherwise 'one_col_bullets'.

Reference Best Practices:
- Avoid wall-of-text. Max 3-4 bullets per slide.
- Sync visual appearance with audio keywords.
- Keep it simple. One key idea per slide.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `title_only` — Just a title, possibly with a subtitle. Best for: section transitions.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "bullets": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "figure": {"x": 0.55, "y": 0.2, "w": 0.4, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "The two_col_fig_right layout allows for the problem statement bullets to be presented on the left while Table 1, which provides the empirical evidence for the 'gap' in existing datasets, is displayed on the right for immediate comparison."
}"""

Token usage so far: 29861 prompt tokens, 2113 completion tokens

Cost so far: $0.36200

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The field of action recognition faces a significant disparity between the abundance of ego-view RGB datasets and the scarcity of 3D point cloud counterparts. Existing 3D datasets are primarily limited by two factors: the use of static, distant sensors and a focus on coarse, full-body motions. Static sensors (like those in NTU RGB+D or IKEA-ASM) fail to capture the camera motion inherent in wearable device scenarios and lack the resolution to distinguish fine-grained interactions with small objects. Furthermore, while datasets like EPIC-Kitchens provide ego-view data, they lack the 3D modality necessary for scenarios where RGB is degraded (e.g., poor lighting) or where spatial redundancy is required for safety-critical AR/VR applications. There is a critical need for datasets that provide fine-grained, ego-centric 3D point clouds to support the development of algorithms for head-mounted devices like HoloLens 2 or Apple Vision Pro.",
  "key_figures": [],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Dataset comparison. The proposed dataset is the first to have ego-view 3D point cloud data in an assembly context.",
      "relevance": "This table explicitly illustrates the 'gap' by showing that while other datasets have either 3D data or an ego-view, only the proposed IKEA Ego 3D dataset provides both in an assembly context."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "1. Introduction",
    "2.1. 3D action understanding datasets"
  ]
}

The layout has been decided:
{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    },
    "figure": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "The two_col_fig_right layout allows for the problem statement bullets to be presented on the left while Table 1, which provides the empirical evidence for the 'gap' in existing datasets, is displayed on the right for immediate comparison."
}

Scene context:
{
  "scene_id": 1,
  "title": "The Gap in 3D Action Recognition",
  "summary": "Highlights the scarcity of ego-view 3D point cloud datasets compared to RGB. While existing 3D datasets use static sensors or focus on full-body motion, there is a critical need for fine-grained, ego-centric 3D data for AR and wearable applications.",
  "paper_section": "1. Introduction",
  "narrative_role": "problem",
  "time_allocation_sec": 8,
  "target_layout": "two_col_fig_right",
  "text_density": "medium",
  "visual_density": "medium",
  "uses_builds": true,
  "expected_build_steps": 3,
  "primary_sources": [
    "Table 1",
    "Section 2.1"
  ],
  "reference_style_examples": [
    "3DInAction- Understanding Human Actions in 3D Point Clouds"
  ]
}

Your job is to **draft the actual content** (title, bullets, audio, figure choice) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. Keep it within the time budget.",
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "source": ["Figure 1", "Section 3.1"],
  "time_cost": "8",
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. Keep within the time budget (about 2-3 words per second).
5. **time_cost**: Must be a string (e.g., "8") matching the high-level plan's time allocation.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "The Gap in 3D Action Recognition",
  "audio_content": "Ego-view 3D datasets are scarce. Current data uses static sensors, lacking the fine-grained detail needed for AR applications.",
  "bullets": [
    "Ego-view 3D point cloud datasets are scarce compared to RGB counterparts.",
    "Existing 3D data uses static sensors and focuses on coarse motions.",
    "AR/VR needs fine-grained, ego-centric 3D data for interaction."
  ],
  "figure": {
    "type": "paper_table",
    "ref": "Table 1",
    "caption": "Comparison of datasets highlighting the lack of ego-view 3D data in assembly contexts."
  },
  "source": [
    "Table 1",
    "Section 2.1"
  ],
  "time_cost": "8",
  "prompt": "A slide with bullet points on the left explaining the scarcity of ego-view 3D data, and a comparison table on the right showing various datasets and their modalities."
}"""

Token usage so far: 36391 prompt tokens, 2362 completion tokens

Cost so far: $0.43477

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "The Gap in 3D Action Recognition",
  "audio_content": "Ego-view 3D datasets are scarce. Current data uses static sensors, lacking the fine-grained detail needed for AR applications.",
  "bullets": [
    "Ego-view 3D point cloud datasets are scarce compared to RGB counterparts.",
    "Existing 3D data uses static sensors and focuses on coarse motions.",
    "AR/VR needs fine-grained, ego-centric 3D data for interaction."
  ],
  "figure": {
    "type": "paper_table",
    "ref": "Table 1",
    "caption": "Comparison of datasets highlighting the lack of ego-view 3D data in assembly contexts."
  },
  "source": [
    "Table 1",
    "Section 2.1"
  ],
  "time_cost": "8",
  "prompt": "A slide with bullet points on the left explaining the scarcity of ego-view 3D data, and a comparison table on the right showing various datasets and their modalities."
}

Layout information:
{
  "layout_template": "two_col_fig_right",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    },
    "figure": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": "8"
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "The Gap in 3D Action Recognition",
    "figure": {
      "type": "paper_table",
      "ref": "Table 1",
      "caption": "Comparison of datasets highlighting the lack of ego-view 3D data in assembly contexts."
    },
    "bullets": [
      "Ego-view 3D point cloud datasets are scarce compared to RGB counterparts.",
      "Existing 3D data uses static sensors and focuses on coarse motions.",
      "AR/VR needs fine-grained, ego-centric 3D data for interaction."
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "Ego-view 3D datasets are scarce.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "Ego-view 3D point cloud datasets are scarce compared to RGB counterparts.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 4.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "Current data uses static sensors, lacking the fine-grained detail needed for AR applications.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 6.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "AR and VR applications specifically require fine-grained, ego-centric 3D data for effective interaction.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 42836 prompt tokens, 2947 completion tokens

Cost so far: $0.51677

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 2,
  "title": "IKEA Ego 3D Dataset Overview",
  "summary": "Introduces the IKEA Ego 3D dataset: 174 assembly sequences captured via HoloLens 2, featuring 493k frames and 56 atomic action classes. Shows the pipeline from RGB-D capture to aligned 3D point cloud sequences.",
  "paper_section": "3. The IKEA Ego3D dataset",
  "narrative_role": "solution",
  "time_allocation_sec": 10,
  "target_layout": "full_fig_with_callouts",
  "text_density": "low",
  "visual_density": "high",
  "uses_builds": true,
  "expected_build_steps": 4,
  "primary_sources": [
    "Figure 1",
    "Section 3.1"
  ],
  "reference_style_examples": [
    "CVPR_CVPR-2025_Highlight-SLAM3R-Real-Time-Dense-Scene-Reconstruction-from-Mon__CVPR-2025-Highlight-SLAM3R-Real-Time-Den"
  ]
}

Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "The IKEA Ego 3D dataset is a large-scale ego-view 3D point cloud dataset designed for fine-grained action recognition in furniture assembly. It comprises 174 unique assembly sequences totaling approximately 493k frames, annotated with 56 atomic action classes (12 verbs and 22 nouns). The data covers four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool step. Data collection utilized a Microsoft HoloLens 2, capturing RGB video at ~30 FPS and long-throw depth at ~5 FPS. To ensure high-quality capture, a holographic rectangular outline was projected to guide users to keep the assembly within the sensor's frustum. The processing pipeline involves syncing RGB and depth frames via nearest timestamps, projecting RGB onto depth maps, and extracting oriented 3D point clouds that include spatial coordinates, RGB color, and normal vectors (x, y, z, R, G, B, Nx, Ny, Nz).",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "This figure illustrates the end-to-end pipeline from assembly and capture to point cloud processing and action inference, providing the core visual summary for the dataset overview slide."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3",
    "Section 3.1"
  ]
}"""

Token usage so far: 48738 prompt tokens, 3359 completion tokens

Cost so far: $0.58815

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The IKEA Ego 3D dataset is a large-scale ego-view 3D point cloud dataset designed for fine-grained action recognition in furniture assembly. It comprises 174 unique assembly sequences totaling approximately 493k frames, annotated with 56 atomic action classes (12 verbs and 22 nouns). The data covers four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool step. Data collection utilized a Microsoft HoloLens 2, capturing RGB video at ~30 FPS and long-throw depth at ~5 FPS. To ensure high-quality capture, a holographic rectangular outline was projected to guide users to keep the assembly within the sensor's frustum. The processing pipeline involves syncing RGB and depth frames via nearest timestamps, projecting RGB onto depth maps, and extracting oriented 3D point clouds that include spatial coordinates, RGB color, and normal vectors (x, y, z, R, G, B, Nx, Ny, Nz).",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "This figure illustrates the end-to-end pipeline from assembly and capture to point cloud processing and action inference, providing the core visual summary for the dataset overview slide."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3",
    "Section 3.1"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 2,
  "title": "IKEA Ego 3D Dataset Overview",
  "summary": "Introduces the IKEA Ego 3D dataset: 174 assembly sequences captured via HoloLens 2, featuring 493k frames and 56 atomic action classes. Shows the pipeline from RGB-D capture to aligned 3D point cloud sequences.",
  "paper_section": "3. The IKEA Ego3D dataset",
  "narrative_role": "solution",
  "time_allocation_sec": 10,
  "target_layout": "full_fig_with_callouts",
  "text_density": "low",
  "visual_density": "high",
  "uses_builds": true,
  "expected_build_steps": 4,
  "primary_sources": [
    "Figure 1",
    "Section 3.1"
  ],
  "reference_style_examples": [
    "CVPR_CVPR-2025_Highlight-SLAM3R-Real-Time-Dense-Scene-Reconstruction-from-Mon__CVPR-2025-Highlight-SLAM3R-Real-Time-Den"
  ]
}

Reference style advice:
Detected 'Methodology' content: Consider a 'full_fig_with_callouts' layout to show the pipeline. Use builds to trace the data flow through the model.

Reference Best Practices:
- Avoid wall-of-text. Max 3-4 bullets per slide.
- Sync visual appearance with audio keywords.
- Keep it simple. One key idea per slide.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `title_only` — Just a title, possibly with a subtitle. Best for: section transitions.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.52
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "style_rationale": "The 'full_fig_with_callouts' layout is chosen to showcase the comprehensive dataset pipeline in Figure 1 as the central visual element. Placing bullets at the bottom allows for high-level dataset statistics (sequences, frames, classes) to act as callouts to the visual flow above."
}"""

Token usage so far: 55332 prompt tokens, 3629 completion tokens

Cost so far: $0.66219

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The IKEA Ego 3D dataset is a large-scale ego-view 3D point cloud dataset designed for fine-grained action recognition in furniture assembly. It comprises 174 unique assembly sequences totaling approximately 493k frames, annotated with 56 atomic action classes (12 verbs and 22 nouns). The data covers four furniture types: LACK side table, LACK TV bench, KALLAX drawer, and BEKVAM stool step. Data collection utilized a Microsoft HoloLens 2, capturing RGB video at ~30 FPS and long-throw depth at ~5 FPS. To ensure high-quality capture, a holographic rectangular outline was projected to guide users to keep the assembly within the sensor's frustum. The processing pipeline involves syncing RGB and depth frames via nearest timestamps, projecting RGB onto depth maps, and extracting oriented 3D point clouds that include spatial coordinates, RGB color, and normal vectors (x, y, z, R, G, B, Nx, Ny, Nz).",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset. The dataset includes 174 assembly sequences captured using a Microsoft HoloLens 2. The captured RGB and Depth streams are labelled with 56 action labels per frame. The data is then aligned and synced to form 3D point cloud sequences that are the input to 3D action recognition algorithms.",
      "relevance": "This figure illustrates the end-to-end pipeline from assembly and capture to point cloud processing and action inference, providing the core visual summary for the dataset overview slide."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3",
    "Section 3.1"
  ]
}

The layout has been decided:
{
  "layout_template": "full_fig_with_callouts",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.52
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "style_rationale": "The 'full_fig_with_callouts' layout is chosen to showcase the comprehensive dataset pipeline in Figure 1 as the central visual element. Placing bullets at the bottom allows for high-level dataset statistics (sequences, frames, classes) to act as callouts to the visual flow above."
}

Scene context:
{
  "scene_id": 2,
  "title": "IKEA Ego 3D Dataset Overview",
  "summary": "Introduces the IKEA Ego 3D dataset: 174 assembly sequences captured via HoloLens 2, featuring 493k frames and 56 atomic action classes. Shows the pipeline from RGB-D capture to aligned 3D point cloud sequences.",
  "paper_section": "3. The IKEA Ego3D dataset",
  "narrative_role": "solution",
  "time_allocation_sec": 10,
  "target_layout": "full_fig_with_callouts",
  "text_density": "low",
  "visual_density": "high",
  "uses_builds": true,
  "expected_build_steps": 4,
  "primary_sources": [
    "Figure 1",
    "Section 3.1"
  ],
  "reference_style_examples": [
    "CVPR_CVPR-2025_Highlight-SLAM3R-Real-Time-Dense-Scene-Reconstruction-from-Mon__CVPR-2025-Highlight-SLAM3R-Real-Time-Den"
  ]
}

Your job is to **draft the actual content** (title, bullets, audio, figure choice) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. Keep it within the time budget.",
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "source": ["Figure 1", "Section 3.1"],
  "time_cost": "8",
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. Keep within the time budget (about 2-3 words per second).
5. **time_cost**: Must be a string (e.g., "8") matching the high-level plan's time allocation.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "IKEA Ego 3D: Large-Scale Ego-View Dataset",
  "audio_content": "IKEA Ego 3D features 174 assembly sequences and 493k frames. Our pipeline syncs HoloLens 2 RGB-D data into aligned 3D point clouds for fine-grained action recognition.",
  "bullets": [
    "174 assembly sequences with 493k frames and 56 action classes",
    "Captured via HoloLens 2 with synced RGB and 5 FPS depth",
    "Aligned 3D point clouds including color and normal vectors"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "End-to-end pipeline from capture to 3D point cloud sequences"
  },
  "source": [
    "Figure 1",
    "Section 3.1"
  ],
  "time_cost": "10",
  "prompt": "A slide showing the IKEA Ego 3D dataset pipeline from Figure 1, illustrating the capture, processing, and point cloud generation steps, with summary statistics at the bottom."
}"""

Token usage so far: 61970 prompt tokens, 3902 completion tokens

Cost so far: $0.73676

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "IKEA Ego 3D: Large-Scale Ego-View Dataset",
  "audio_content": "IKEA Ego 3D features 174 assembly sequences and 493k frames. Our pipeline syncs HoloLens 2 RGB-D data into aligned 3D point clouds for fine-grained action recognition.",
  "bullets": [
    "174 assembly sequences with 493k frames and 56 action classes",
    "Captured via HoloLens 2 with synced RGB and 5 FPS depth",
    "Aligned 3D point clouds including color and normal vectors"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "End-to-end pipeline from capture to 3D point cloud sequences"
  },
  "source": [
    "Figure 1",
    "Section 3.1"
  ],
  "time_cost": "10",
  "prompt": "A slide showing the IKEA Ego 3D dataset pipeline from Figure 1, illustrating the capture, processing, and point cloud generation steps, with summary statistics at the bottom."
}

Layout information:
{
  "layout_template": "full_fig_with_callouts",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.18,
      "w": 0.9,
      "h": 0.52
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "total_time_sec": "10"
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "IKEA Ego 3D: Large-Scale Ego-View Dataset",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "End-to-end pipeline from capture to 3D point cloud sequences"
    },
    "bullets": [
      "174 assembly sequences with 493k frames and 56 action classes",
      "Captured via HoloLens 2 with synced RGB and 5 FPS depth",
      "Aligned 3D point clouds including color and normal vectors"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "IKEA Ego 3D features 174 assembly sequences and 493k frames.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "The dataset includes 56 action classes.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 5.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "Our pipeline syncs HoloLens 2 RGB-D data...",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 7.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "...into aligned 3D point clouds for fine-grained action recognition.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 68443 prompt tokens, 4486 completion tokens

Cost so far: $0.81901

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 3,
  "title": "Fine-Grained Actions & Challenges",
  "summary": "Visualizes the diversity of furniture (LACK, KALLAX, BEKVAM) and the complexity of actions like 'spin screwdriver' or 'attach side panel'. Discusses unique challenges: ego-view camera motion, frequent occlusions, and class imbalance.",
  "paper_section": "3.5 Dataset unique challenges",
  "narrative_role": "technical_detail",
  "time_allocation_sec": 8,
  "target_layout": "grid_2x2",
  "text_density": "medium",
  "visual_density": "high",
  "uses_builds": true,
  "expected_build_steps": 2,
  "primary_sources": [
    "Figure 2",
    "Figure 3",
    "Figure 4"
  ],
  "reference_style_examples": [
    "Pos3R- 6D Pose Estimation for Unseen Objects Made Easy"
  ]
}

Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "The IKEA Ego 3D dataset presents several unique challenges for action recognition. First, the ego-view perspective introduces significant camera motion, causing points to appear and disappear within frames, which is more complex than static sensor data. Second, the dataset contains three distinct types of point motion: action-related, noise-related, and camera-related, which are difficult to decouple. Third, there is a high degree of class imbalance, as shown in the action occurrence distribution, where some actions like 'spin leg' are frequent and long, while others like 'spin drawer knob' are short and rare. Finally, the fine-grained nature of the actions (verb-noun pairs) means that many classes are visually similar (e.g., different types of screws) but contextually distinct, requiring high-resolution ego-view data to discriminate small components.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Visualizes the diversity of furniture types included in the dataset, supporting the claim of varied assembly tasks."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the complexity and fine-grained nature of the actions, showing the alignment between RGB and 3D point cloud modalities."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the significant class imbalance challenge inherent in the dataset."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1",
    "Section 3.3",
    "Section 3.5"
  ]
}"""

Token usage so far: 74306 prompt tokens, 5030 completion tokens

Cost so far: $0.89396

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The IKEA Ego 3D dataset presents several unique challenges for action recognition. First, the ego-view perspective introduces significant camera motion, causing points to appear and disappear within frames, which is more complex than static sensor data. Second, the dataset contains three distinct types of point motion: action-related, noise-related, and camera-related, which are difficult to decouple. Third, there is a high degree of class imbalance, as shown in the action occurrence distribution, where some actions like 'spin leg' are frequent and long, while others like 'spin drawer knob' are short and rare. Finally, the fine-grained nature of the actions (verb-noun pairs) means that many classes are visually similar (e.g., different types of screws) but contextually distinct, requiring high-resolution ego-view data to discriminate small components.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Visualizes the diversity of furniture types included in the dataset, supporting the claim of varied assembly tasks."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the complexity and fine-grained nature of the actions, showing the alignment between RGB and 3D point cloud modalities."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the significant class imbalance challenge inherent in the dataset."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1",
    "Section 3.3",
    "Section 3.5"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 3,
  "title": "Fine-Grained Actions & Challenges",
  "summary": "Visualizes the diversity of furniture (LACK, KALLAX, BEKVAM) and the complexity of actions like 'spin screwdriver' or 'attach side panel'. Discusses unique challenges: ego-view camera motion, frequent occlusions, and class imbalance.",
  "paper_section": "3.5 Dataset unique challenges",
  "narrative_role": "technical_detail",
  "time_allocation_sec": 8,
  "target_layout": "grid_2x2",
  "text_density": "medium",
  "visual_density": "high",
  "uses_builds": true,
  "expected_build_steps": 2,
  "primary_sources": [
    "Figure 2",
    "Figure 3",
    "Figure 4"
  ],
  "reference_style_examples": [
    "Pos3R- 6D Pose Estimation for Unseen Objects Made Easy"
  ]
}

Reference style advice:
Detected 'Motivation' content: Consider a 'two_col_fig_right' layout. Use bullet points on the left to state the problem, with an illustrative figure on the right.

Reference Best Practices:
- Avoid wall-of-text. Max 3-4 bullets per slide.
- Sync visual appearance with audio keywords.
- Keep it simple. One key idea per slide.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `title_only` — Just a title, possibly with a subtitle. Best for: section transitions.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "bullets": {"x": 0.05, "y": 0.2, "w": 0.35, "h": 0.7},
    "figure": {"x": 0.45, "y": 0.2, "w": 0.5, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "The slide outlines technical challenges (camera motion, class imbalance, fine-grained actions). A two-column layout with bullets on the left and a composite figure on the right (showing actions and imbalance distribution) effectively pairs the conceptual problems with visual evidence, following the recommended style for motivation and problem-statement content."
}"""

Token usage so far: 80995 prompt tokens, 5266 completion tokens

Cost so far: $0.96793

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The IKEA Ego 3D dataset presents several unique challenges for action recognition. First, the ego-view perspective introduces significant camera motion, causing points to appear and disappear within frames, which is more complex than static sensor data. Second, the dataset contains three distinct types of point motion: action-related, noise-related, and camera-related, which are difficult to decouple. Third, there is a high degree of class imbalance, as shown in the action occurrence distribution, where some actions like 'spin leg' are frequent and long, while others like 'spin drawer knob' are short and rare. Finally, the fine-grained nature of the actions (verb-noun pairs) means that many classes are visually similar (e.g., different types of screws) but contextually distinct, requiring high-resolution ego-view data to discriminate small components.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "IKEA Ego3D Furniture. The assemblies in the IKEA Ego3D dataset include the (a) LACK Side table, (b) LACK TV bench, (c) KALLAX Drawer, and BEKVAM (d) Stepping stool.",
      "relevance": "Visualizes the diversity of furniture types included in the dataset, supporting the claim of varied assembly tasks."
    },
    {
      "ref": "Figure 3",
      "caption": "IKEA Ego 3D Dataset actions. Visualizing the RGB image (top), 3D point cloud (middle), and action label (bottom) for the Drawer (a-d) and Stool (e-h) assemblies.",
      "relevance": "Demonstrates the complexity and fine-grained nature of the actions, showing the alignment between RGB and 3D point cloud modalities."
    },
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Provides quantitative evidence of the significant class imbalance challenge inherent in the dataset."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 3.1",
    "Section 3.3",
    "Section 3.5"
  ]
}

The layout has been decided:
{
  "layout_template": "two_col_fig_right",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    },
    "figure": {
      "x": 0.45,
      "y": 0.2,
      "w": 0.5,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "The slide outlines technical challenges (camera motion, class imbalance, fine-grained actions). A two-column layout with bullets on the left and a composite figure on the right (showing actions and imbalance distribution) effectively pairs the conceptual problems with visual evidence, following the recommended style for motivation and problem-statement content."
}

Scene context:
{
  "scene_id": 3,
  "title": "Fine-Grained Actions & Challenges",
  "summary": "Visualizes the diversity of furniture (LACK, KALLAX, BEKVAM) and the complexity of actions like 'spin screwdriver' or 'attach side panel'. Discusses unique challenges: ego-view camera motion, frequent occlusions, and class imbalance.",
  "paper_section": "3.5 Dataset unique challenges",
  "narrative_role": "technical_detail",
  "time_allocation_sec": 8,
  "target_layout": "grid_2x2",
  "text_density": "medium",
  "visual_density": "high",
  "uses_builds": true,
  "expected_build_steps": 2,
  "primary_sources": [
    "Figure 2",
    "Figure 3",
    "Figure 4"
  ],
  "reference_style_examples": [
    "Pos3R- 6D Pose Estimation for Unseen Objects Made Easy"
  ]
}

Your job is to **draft the actual content** (title, bullets, audio, figure choice) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. Keep it within the time budget.",
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "source": ["Figure 1", "Section 3.1"],
  "time_cost": "8",
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. Keep within the time budget (about 2-3 words per second).
5. **time_cost**: Must be a string (e.g., "8") matching the high-level plan's time allocation.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Fine-Grained Actions & Dataset Challenges",
  "audio_content": "The dataset features 56 fine-grained actions. It introduces unique challenges like ego-view camera motion and significant class imbalance.",
  "bullets": [
    "56 fine-grained verb-noun actions across 4 furniture types",
    "Complex ego-view camera motion and point volatility",
    "Significant class imbalance across action categories"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualization of RGB, 3D point cloud, and fine-grained action labels."
  },
  "source": [
    "Section 3.5",
    "Figure 3",
    "Figure 4"
  ],
  "time_cost": "8",
  "prompt": "A slide showing three bullet points on the left describing dataset challenges like camera motion and class imbalance. On the right, Figure 3 from the paper is displayed, showing the alignment between RGB video, 3D point clouds, and action labels for furniture assembly."
}"""

Token usage so far: 87725 prompt tokens, 5520 completion tokens

Cost so far: $1.04285

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Fine-Grained Actions & Dataset Challenges",
  "audio_content": "The dataset features 56 fine-grained actions. It introduces unique challenges like ego-view camera motion and significant class imbalance.",
  "bullets": [
    "56 fine-grained verb-noun actions across 4 furniture types",
    "Complex ego-view camera motion and point volatility",
    "Significant class imbalance across action categories"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Visualization of RGB, 3D point cloud, and fine-grained action labels."
  },
  "source": [
    "Section 3.5",
    "Figure 3",
    "Figure 4"
  ],
  "time_cost": "8",
  "prompt": "A slide showing three bullet points on the left describing dataset challenges like camera motion and class imbalance. On the right, Figure 3 from the paper is displayed, showing the alignment between RGB video, 3D point clouds, and action labels for furniture assembly."
}

Layout information:
{
  "layout_template": "two_col_fig_right",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "bullets": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.35,
      "h": 0.7
    },
    "figure": {
      "x": 0.45,
      "y": 0.2,
      "w": 0.5,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": "8"
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Fine-Grained Actions & Dataset Challenges",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 3",
      "caption": "Visualization of RGB, 3D point cloud, and fine-grained action labels."
    },
    "bullets": [
      "56 fine-grained verb-noun actions across 4 furniture types",
      "Complex ego-view camera motion and point volatility",
      "Significant class imbalance across action categories"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {
          "type": "show",
          "target": "title"
        },
        {
          "type": "show",
          "target": "figure"
        }
      ],
      "audio_segment": "The IKEA Ego 3D dataset features 56 fine-grained actions.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "These are categorized as verb-noun actions performed across four different furniture types.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 4.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "The dataset introduces unique challenges like complex ego-view camera motion and point volatility.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 6.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "Finally, it exhibits significant class imbalance across the various action categories.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 94175 prompt tokens, 6086 completion tokens

Cost so far: $1.12433

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 4,
  "title": "Benchmarking SOTA Methods",
  "summary": "Presents evaluation results for state-of-the-art 3D action recognition methods. Key findings show that temporal smoothing significantly boosts performance and that hierarchical verb-noun decomposition helps decouple spatial and temporal representation power.",
  "paper_section": "4. Benchmark and Experiments",
  "narrative_role": "result",
  "time_allocation_sec": 9,
  "target_layout": "two_col_fig_left",
  "text_density": "high",
  "visual_density": "medium",
  "uses_builds": true,
  "expected_build_steps": 3,
  "primary_sources": [
    "Table 2",
    "Table 3",
    "Table 4"
  ],
  "reference_style_examples": [
    "3DInAction- Understanding Human Actions in 3D Point Clouds"
  ]
}

Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }
  ],
  "key_tables": [
    {
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }
  ],
  "key_equations": [
    {
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "extracted_content": "The benchmark evaluates prominent 3D action recognition methods including PointNet (PN), PointNet++ (PN++), Set Transformer, PSTNet, P4Transformer, and 3DinAction. Performance is measured using top1/top3 accuracy, macro-recall, and mAP, revealing that the IKEA Ego 3D dataset is highly challenging. A key finding is that incorporating naive temporal smoothing (TS) via a convolutional layer over the temporal dimension significantly boosts performance for all per-frame baselines, with PN++ + TS achieving the highest top1 accuracy of 52.98%. Hierarchical experiments decoupling actions into nouns and verbs show that nouns are easier to recognize from static frames (spatial quality), while verbs are inherently more difficult as they require accumulating sequence information (temporal quality). Specialized models like PSTNet performed well, whereas 3DinAction was limited by the large sensor motions inherent in ego-view data, which caused temporal patches (t-patches) to collapse.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Illustrates the class imbalance challenge that impacts the macro-recall and mAP metrics reported in the benchmark."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the primary performance comparison of all baseline and SOTA methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Shows how well models recognize the objects involved in actions, reflecting their spatial representation power."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the models' ability to distinguish the motion component of actions, reflecting their temporal representation power."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4. Benchmark and Experiments",
    "Section 4.1. Experiment setup",
    "Section 4.2. Benchmark results discussion",
    "Section 4.3. Noun and Verb clustering experiment"
  ]
}"""

Token usage so far: 100024 prompt tokens, 6749 completion tokens

Cost so far: $1.20271

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The benchmark evaluates prominent 3D action recognition methods including PointNet (PN), PointNet++ (PN++), Set Transformer, PSTNet, P4Transformer, and 3DinAction. Performance is measured using top1/top3 accuracy, macro-recall, and mAP, revealing that the IKEA Ego 3D dataset is highly challenging. A key finding is that incorporating naive temporal smoothing (TS) via a convolutional layer over the temporal dimension significantly boosts performance for all per-frame baselines, with PN++ + TS achieving the highest top1 accuracy of 52.98%. Hierarchical experiments decoupling actions into nouns and verbs show that nouns are easier to recognize from static frames (spatial quality), while verbs are inherently more difficult as they require accumulating sequence information (temporal quality). Specialized models like PSTNet performed well, whereas 3DinAction was limited by the large sensor motions inherent in ego-view data, which caused temporal patches (t-patches) to collapse.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Illustrates the class imbalance challenge that impacts the macro-recall and mAP metrics reported in the benchmark."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the primary performance comparison of all baseline and SOTA methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Shows how well models recognize the objects involved in actions, reflecting their spatial representation power."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the models' ability to distinguish the motion component of actions, reflecting their temporal representation power."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4. Benchmark and Experiments",
    "Section 4.1. Experiment setup",
    "Section 4.2. Benchmark results discussion",
    "Section 4.3. Noun and Verb clustering experiment"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 4,
  "title": "Benchmarking SOTA Methods",
  "summary": "Presents evaluation results for state-of-the-art 3D action recognition methods. Key findings show that temporal smoothing significantly boosts performance and that hierarchical verb-noun decomposition helps decouple spatial and temporal representation power.",
  "paper_section": "4. Benchmark and Experiments",
  "narrative_role": "result",
  "time_allocation_sec": 9,
  "target_layout": "two_col_fig_left",
  "text_density": "high",
  "visual_density": "medium",
  "uses_builds": true,
  "expected_build_steps": 3,
  "primary_sources": [
    "Table 2",
    "Table 3",
    "Table 4"
  ],
  "reference_style_examples": [
    "3DInAction- Understanding Human Actions in 3D Point Clouds"
  ]
}

Reference style advice:
Detected 'Results' content: Consider a 'full_fig_with_callouts' or 'two_row_charts' layout. Use builds to highlight specific data points or rows in the table.

Reference Best Practices:
- Avoid wall-of-text. Max 3-4 bullets per slide.
- Sync visual appearance with audio keywords.
- Keep it simple. One key idea per slide.

Your job is to decide the **visual layout** for this slide. Do NOT decide builds or animations — those will be planned later.

## CHOOSE THE BEST LAYOUT

Pick the layout template that best suits the content. Common templates include (but you are NOT limited to these):
- `two_col_fig_left` — Figure on left, bullets on right. Best for: method diagrams, architecture figures.
- `two_col_fig_right` — Bullets on left, figure on right. Best for: motivation slides with illustrative figures.
- `full_fig_with_callouts` — Large figure with small bullet callouts below. Best for: results, data visualizations.
- `one_col_bullets` — Full-width bullets, no figure. Best for: text-heavy overview or summary slides.
- `title_only` — Just a title, possibly with a subtitle. Best for: section transitions.

If none of these fit, invent a descriptive template name and define its regions.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}
  },
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.47, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.2, "w": 0.4, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the primary results table (Table 2) on the left allows for a direct comparison with the key analytical findings in the bullets on the right. This layout supports the high text density required to explain the performance boosts from temporal smoothing and the insights from the verb-noun decomposition."
}"""

Token usage so far: 106821 prompt tokens, 6984 completion tokens

Cost so far: $1.27773

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The benchmark evaluates prominent 3D action recognition methods including PointNet (PN), PointNet++ (PN++), Set Transformer, PSTNet, P4Transformer, and 3DinAction. Performance is measured using top1/top3 accuracy, macro-recall, and mAP, revealing that the IKEA Ego 3D dataset is highly challenging. A key finding is that incorporating naive temporal smoothing (TS) via a convolutional layer over the temporal dimension significantly boosts performance for all per-frame baselines, with PN++ + TS achieving the highest top1 accuracy of 52.98%. Hierarchical experiments decoupling actions into nouns and verbs show that nouns are easier to recognize from static frames (spatial quality), while verbs are inherently more difficult as they require accumulating sequence information (temporal quality). Specialized models like PSTNet performed well, whereas 3DinAction was limited by the large sensor motions inherent in ego-view data, which caused temporal patches (t-patches) to collapse.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "IKEA Ego 3D dataset action occurrence. A highly imbalanced dataset provides a challenge for learning-based algorithms. Note the y-axis is log scaled, therefore a small gap in this axis reflects a significant gap in proportions.",
      "relevance": "Illustrates the class imbalance challenge that impacts the macro-recall and mAP metrics reported in the benchmark."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 2",
      "caption": "Action recognition results on IKEA Ego 3D. Comparing between recent state-of-the-art approaches using frame accuracy (top1 and top3), macro recall and mAP metrics.",
      "relevance": "Provides the primary performance comparison of all baseline and SOTA methods on the new dataset."
    },
    {
      "ref": "Table 3",
      "caption": "Noun recognition results. We cluster the action classes by nouns and report the performance of state-of-the-art approaches. This experiment demonstrates the spatial quality of the methods (how well they capture objects).",
      "relevance": "Shows how well models recognize the objects involved in actions, reflecting their spatial representation power."
    },
    {
      "ref": "Table 4",
      "caption": "Verb recognition results. We cluster the action classes by verbs and report the performance of state-of-the-art approaches. This experiment demonstrates the temporal quality of the methods (how well they distinguish motions).",
      "relevance": "Evaluates the models' ability to distinguish the motion component of actions, reflecting their temporal representation power."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 4. Benchmark and Experiments",
    "Section 4.1. Experiment setup",
    "Section 4.2. Benchmark results discussion",
    "Section 4.3. Noun and Verb clustering experiment"
  ]
}

The layout has been decided:
{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.47,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the primary results table (Table 2) on the left allows for a direct comparison with the key analytical findings in the bullets on the right. This layout supports the high text density required to explain the performance boosts from temporal smoothing and the insights from the verb-noun decomposition."
}

Scene context:
{
  "scene_id": 4,
  "title": "Benchmarking SOTA Methods",
  "summary": "Presents evaluation results for state-of-the-art 3D action recognition methods. Key findings show that temporal smoothing significantly boosts performance and that hierarchical verb-noun decomposition helps decouple spatial and temporal representation power.",
  "paper_section": "4. Benchmark and Experiments",
  "narrative_role": "result",
  "time_allocation_sec": 9,
  "target_layout": "two_col_fig_left",
  "text_density": "high",
  "visual_density": "medium",
  "uses_builds": true,
  "expected_build_steps": 3,
  "primary_sources": [
    "Table 2",
    "Table 3",
    "Table 4"
  ],
  "reference_style_examples": [
    "3DInAction- Understanding Human Actions in 3D Point Clouds"
  ]
}

Your job is to **draft the actual content** (title, bullets, audio, figure choice) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. Keep it within the time budget.",
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  },
  "source": ["Figure 1", "Section 3.1"],
  "time_cost": "8",
  "prompt": "Visual description of the scene for generation"
}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. Keep within the time budget (about 2-3 words per second).
5. **time_cost**: Must be a string (e.g., "8") matching the high-level plan's time allocation.
6. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""{
  "title": "Benchmarking SOTA Methods",
  "audio_content": "Our benchmark reveals a challenging dataset. Temporal smoothing significantly boosts performance, with PointNet plus plus plus TS achieving the highest accuracy at 53 percent.",
  "bullets": [
    "IKEA Ego 3D is highly challenging for current SOTA methods.",
    "Temporal smoothing (TS) significantly boosts performance for all baselines.",
    "PN++ + TS achieves the highest top-1 accuracy of 52.98%.",
    "Verb-noun decomposition highlights gaps in temporal representation power."
  ],
  "figure": {
    "type": "paper_table",
    "ref": "Table 2",
    "caption": "Action recognition results comparing SOTA methods on IKEA Ego 3D."
  },
  "source": [
    "Table 2",
    "Table 3",
    "Table 4",
    "Section 4.2"
  ],
  "time_cost": "9",
  "prompt": "A slide showing a comparison table of 3D action recognition results on the left and summary bullets on the right. The table (Table 2) highlights performance metrics like top-1 accuracy and mAP for various models."
}"""

Token usage so far: 113655 prompt tokens, 7266 completion tokens

Cost so far: $1.35453

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Benchmarking SOTA Methods",
  "audio_content": "Our benchmark reveals a challenging dataset. Temporal smoothing significantly boosts performance, with PointNet plus plus plus TS achieving the highest accuracy at 53 percent.",
  "bullets": [
    "IKEA Ego 3D is highly challenging for current SOTA methods.",
    "Temporal smoothing (TS) significantly boosts performance for all baselines.",
    "PN++ + TS achieves the highest top-1 accuracy of 52.98%.",
    "Verb-noun decomposition highlights gaps in temporal representation power."
  ],
  "figure": {
    "type": "paper_table",
    "ref": "Table 2",
    "caption": "Action recognition results comparing SOTA methods on IKEA Ego 3D."
  },
  "source": [
    "Table 2",
    "Table 3",
    "Table 4",
    "Section 4.2"
  ],
  "time_cost": "9",
  "prompt": "A slide showing a comparison table of 3D action recognition results on the left and summary bullets on the right. The table (Table 2) highlights performance metrics like top-1 accuracy and mAP for various models."
}

Layout information:
{
  "layout_template": "two_col_fig_left",
  "layout_regions": {
    "title": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.9,
      "h": 0.1
    },
    "figure": {
      "x": 0.05,
      "y": 0.2,
      "w": 0.47,
      "h": 0.7
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": "9"
}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {
    "title": "The slide title from the draft",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    },
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }
  ]
}

## STRICT RULES:
1. **Build count**: `expected_build_steps` = 1 + number_of_bullets. Build 0 shows title (and figure if present), then one build per bullet.
2. **One bullet per build**: After build 0, each build reveals exactly ONE bullet. `bullets[0]` in build 1, `bullets[1]` in build 2, etc.
3. **Build 0**: Always shows `title` (and `figure` if present). Never shows bullets in build 0.
4. **Audio segments**: Split the `audio_content` from the draft into segments. Each build's `audio_segment` must be non-empty and correspond to what that build reveals.
5. **Bullet ordering**: Assign bullets to builds in the order that creates the best storytelling flow for the audience.
6. **time_offset_sec**: Space evenly across the total time. For N builds over T seconds: offsets at 0, T/N, 2T/N, etc.
7. **visual_emphasis**: Always set to empty list `[]`.
8. **Action targets**: Only use targets that exist in `elements`: `title`, `figure`, `bullets[0]`, `bullets[1]`, etc.
9. **elements**: Copy the drafted title, figure, and bullets exactly — do not modify the text content.
10. Output ONLY valid JSON, no markdown fences, no explanation.


**Answer (from GEMINI)**

"""```json
{
  "style": "Slides",
  "expected_build_steps": 5,
  "elements": {
    "title": "Benchmarking SOTA Methods",
    "figure": {
      "type": "paper_table",
      "ref": "Table 2",
      "caption": "Action recognition results comparing SOTA methods on IKEA Ego 3D."
    },
    "bullets": [
      "IKEA Ego 3D is highly challenging for current SOTA methods.",
      "Temporal smoothing (TS) significantly boosts performance for all baselines.",
      "PN++ + TS achieves the highest top-1 accuracy of 52.98%.",
      "Verb-noun decomposition highlights gaps in temporal representation power."
    ]
  },
  "builds": [
    {
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {"type": "show", "target": "title"},
        {"type": "show", "target": "figure"}
      ],
      "audio_segment": "Our benchmark reveals a challenging dataset.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 1.8,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "The IKEA Ego 3D dataset is highly challenging for current state-of-the-art methods.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 3.6,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Temporal smoothing significantly boosts performance for all baselines.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 5.4,
      "actions": [
        {"type": "fade_in", "target": "bullets[2]"}
      ],
      "audio_segment": "with PointNet plus plus plus TS achieving the highest accuracy at 53 percent.",
      "visual_emphasis": []
    },
    {
      "step_index": 4,
      "time_offset_sec": 7.2,
      "actions": [
        {"type": "fade_in", "target": "bullets[3]"}
      ],
      "audio_segment": "Finally, verb-noun decomposition highlights gaps in temporal representation power.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 120133 prompt tokens, 7901 completion tokens

Cost so far: $1.43836

