system_message = "You are an expert in reading academic papers and creating video summaries based on them. "

math_prompt = "You are an expert in reading academic papers and creating video summaries based on them. "

high_level_planning_prompt = """Given a paper, please design a video summary. 
The number of scenes should be based on the RECOMMENDATION in the style context below.

{style_context}

Requirements: 
1. Each scene must include strong relationship between last and next scene.
2. No overlapping content between scenes.
3. Collectively present all key findings in a coherent narrative.
4. Maintain high technical accuracy and professionalism.
5. Allow 5 to 10 seconds of video per scene.
6. Deliver only core content; omit acknowledgements and references.

You MUST output the scenes in the following STRICT JSON format (list of objects):
```json
[
  {{
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
  }},
  ...
]
```
Do NOT just acknowledge this request. Generate the actual scene list NOW. Ensure strictly valid JSON."""

high_level_evaluate_prompt = "Below are the video-summary scenes I designed based on the corresponding paper. Please check it with answering questions: Do these scenes cover all the key points the original paper intends to convey? Do these scenes avoid overlapping content and redundancy? Do these scenes form a coherent and correct story? Please answer “YES/NO.” If you answer “NO” (i.e., issues exist), provide suggestions for improvement. Current plan:"

high_level_replanning_prompt = "The above are the scenes you previously designed. Please modify the scenes accordingly based on the following feedback while keeping the format unchanged:"

high_plan_format_prompt = " The next paragraph of TEXT will provide descriptions for multiple scenes. I need you to fill the \"***\" section of the dict LIST with the TEXT. Please output the LIST only. LIST:[{ \"SCENE1\": \"******\", \"DESCRIPTION\": \"******\", \"TIME_ALLOCATION\": \"******\"},{ \"SCENE2\": \"******\", \"DESCRIPTION\": \"******\", \"TIME_ALLOCATION\": \"******\"}...] TEXT:"

### ─────────────────────────────────────────────────
### Stage 1: Content Extraction
### ─────────────────────────────────────────────────

content_extraction_prompt = """
You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{scene_json}

Read the paper carefully and extract ALL relevant content from the section(s) referenced in this scene.

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "extracted_content": "A comprehensive summary of the key information from this section. Include main claims, methods, results, or insights. This should contain enough detail for someone to write presentation bullets from it.",
  "key_figures": [
    {{
      "ref": "Figure X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this figure matters for this scene"
    }}
  ],
  "key_tables": [
    {{
      "ref": "Table X",
      "caption": "The actual caption from the paper",
      "relevance": "Why this table matters for this scene"
    }}
  ],
  "key_equations": [
    {{
      "ref": "Equation X or description",
      "content": "The equation in text form",
      "relevance": "Why this equation matters for this scene"
    }}
  ],
  "section_refs": ["Section 3.1", "Section 3.2"]
}}

## STRICT RULES:
1. **Only reference figures/tables that actually appear in the paper section.** Do NOT invent or guess figure/table numbers.
2. **key_figures** must list figures by their exact label in the paper (e.g., "Figure 1", "Fig. 2").
3. If no figures/tables/equations are relevant, use empty lists `[]`.
4. **extracted_content** must be detailed enough to create 2-4 meaningful bullet points from it.
5. Output ONLY valid JSON, no markdown fences, no explanation.
"""

### ─────────────────────────────────────────────────
### Stage 2: Style Planning (Layout Only)
### ─────────────────────────────────────────────────

style_planning_prompt = """
You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{content_summary}

Scene context from high-level plan:
{scene_context}

Reference style advice:
{style_advice}

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

{{
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {{
    "title": {{"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1}},
    "figure": {{"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7}},
    "bullets": {{"x": 0.55, "y": 0.25, "w": 0.4, "h": 0.6}}
  }},
  "has_figure": true,
  "style_rationale": "Two-column layout with figure on left is ideal for showing the architecture diagram alongside explanatory bullets."
}}

## STRICT RULES:
1. **Region keys**: Only use `title`, `bullets`, `figure` as region keys. Do NOT invent keys like `callout_1`, `table`, etc.
2. **Coordinates**: All x/y/w/h values must be normalized (0.0 to 1.0). Regions must not overlap.
3. **has_figure**: Set to `true` only if the content summary has relevant figures. If no figure is available, omit `figure` from regions.
4. **No builds**: Do NOT include `build_skeleton`, `expected_build_steps`, or any animation information.
5. Output ONLY valid JSON, no markdown fences, no explanation.
"""

### ─────────────────────────────────────────────────
### Stage 3: Low-Level Planning (Content Drafting)
### ─────────────────────────────────────────────────

low_level_planning_prompt = """
You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{content_summary}

The layout has been decided:
{style_plan}

Scene context:
{scene_context}

Your job is to **draft the actual content** (title, bullets, audio, figure choice) that fits into this layout. You do NOT decide the layout — that is already set. You also do NOT decide builds or animations — those will be planned later based on your drafted content.

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "title": "A clear, concise slide title",
  "audio_content": "Full narration transcript for this entire scene. Should be natural, conversational, and cover all key points. Keep it within the time budget.",
  "bullets": [
    "First concise bullet point",
    "Second concise bullet point",
    "Third concise bullet point"
  ],
  "figure": {{
    "type": "paper_figure",
    "ref": "Figure X",
    "caption": "Brief caption describing the figure"
  }},
  "source": ["Figure 1", "Section 3.1"],
  "time_cost": "8",
  "prompt": "Visual description of the scene for generation"
}}

## STRICT RULES:
1. **Number of bullets**: Write 2-4 concise, impactful bullets that cover the key points from the extracted content.
2. **Figure reference**: ONLY use figures listed in the content summary's `key_figures`. Do NOT invent figure references. If the style plan has `has_figure: false`, omit `figure` entirely.
3. **Bullet text**: Each bullet should be concise (under 15 words preferred), impactful, and directly derived from `extracted_content`. Not a copy — a focused summary.
4. **audio_content**: Natural narration covering all bullet points. Keep within the time budget (about 2-3 words per second).
5. **time_cost**: Must be a string (e.g., "8") matching the high-level plan's time allocation.
6. Output ONLY valid JSON, no markdown fences, no explanation.
"""

### ─────────────────────────────────────────────────
### Stage 4: Style Refinement (Assign Content → Builds)
### ─────────────────────────────────────────────────

style_refinement_prompt = """
You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{content_draft}

Layout information:
{layout_info}

Your job is to:
1. **Decide the build plan** — how many build steps, and what gets revealed in each step.
2. **Assign the drafted bullets to specific build steps** in the best storytelling order.
3. **Split the audio into per-build segments** so each build has matching narration.

## OUTPUT FORMAT — Return ONLY valid JSON:

{{
  "style": "Slides",
  "expected_build_steps": 3,
  "elements": {{
    "title": "The slide title from the draft",
    "figure": {{
      "type": "paper_figure",
      "ref": "Figure X",
      "caption": "Caption from draft"
    }},
    "bullets": [
      "First bullet",
      "Second bullet"
    ]
  }},
  "builds": [
    {{
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {{"type": "show", "target": "title"}},
        {{"type": "show", "target": "figure"}}
      ],
      "audio_segment": "Opening narration for this build step.",
      "visual_emphasis": []
    }},
    {{
      "step_index": 1,
      "time_offset_sec": 3.0,
      "actions": [
        {{"type": "fade_in", "target": "bullets[0]"}}
      ],
      "audio_segment": "Narration for the first bullet point.",
      "visual_emphasis": []
    }},
    {{
      "step_index": 2,
      "time_offset_sec": 6.0,
      "actions": [
        {{"type": "fade_in", "target": "bullets[1]"}}
      ],
      "audio_segment": "Narration for the second bullet point.",
      "visual_emphasis": []
    }}
  ]
}}

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
"""



low_level_evaluate_prompt = "This is the video summary plan we created for the scene of the part of the paper. Please respond to each of the following questions with either \"YES\" or \"NO\" to determine whether the current plan meets the requirements (if \"NO\", provide the correct answer)."

low_level_replanning_prompt = "The above is the scene style selection plan you designed earlier, but it seems that the following issues have arisen. Please make the corresponding modifications and ensure that the updated version maintains the exact same format as the previous version.:"

low_plan_format_prompt="Fill in the dictionary (***** means blank ) with the given above text. For \"style,\" the blank can only be filled with one of the following options: (Slides, Professional, Talking Heads, Captioning, or General Video). If there is no suitable match, write \"PASS\":{ \"audio_content\": \"******\", \"style\": \"******\", \"source\": \"******\", \" prompt\": \"******\"} Only output this dictionary, no extra content is needed! For example: { \"audio_content\": \"This is the picture from the original paper, which means a lot.\",\"style\": \"Slides\",\"source\": \"Fig.1\",\"prompt\": \"Previous palaeomagnetic investigations using samples from Apollo and Chang'e-5 missions have revealed the Moon's magnetic history. However, these studies were limited to the nearside, leaving the farside largely unexplored.\". \n Make sure that the content replacing \"******\" are strings and does not contain double quotes inside.}"

low_level_evaluate_prompt_list = ["\n Is the video style exactly one of those choices: [Slides, Professional, Talking Heads, Captioning, or General Video] ? \n Do you think the choice of this style is reasonable?", "\n Does the \" audio_ content\" part appear to meet the required time_cost? Avoid overly lengthy text. The time_cost is fixed and cannot be changed. \n Do you think the audio_content is reasonable?","  Only If the video \" style \" is \" slides \", answer: Does the \" source \" part explicitly provide a specific source element (exact table/picture/equation)in the original paper? \n Is the professionalism of the current plan acceptable? \n Only if the video \"style \"  is \" professional \", does the original plan provide a clear mathematical expression or molecular formula so that I can know the content without reading original paper? \n","The \"prompt\" part should be a description of the scenes for the video to be generated. Does the existing \"prompt\" work as a prompt for a generation model (if the style is a General video, Captioning) or as a note to show (if the style is Slides or Professional)?\n"] 

load_table_prompt="Can you return the content of the specific table of the original paper in table fomular? No extra TEXT in output."

pro_classify_prompt = "Is this scene related to mathematical content? If yes, output \"math\". Is this scene related to molecular visualization content? If yes, output \"mol\""

pro_format_prompt = "The code I require does not need to be complete; it only needs to exist as an animation function. Please check if the following code meets my requirements: It should not contain any import statements. It should be simple and within 100 lines! It should start with 'def animate(self):\n    '. It should end with 'self.wait(X)' (where X is a number). Conforms to indentation rules! If it does not meet the requirements, rewrite it in the format I requested. Output the code Only!"

pro_gen_prompt = "Why can't the following code run? Please modify the code and make it generate the correct video. Your result must be understandable by the Python compiler! Conforms to indentation rules. Make it SIMPLE and meaningful! Make sure the code Only output the code!"

pro_vis_eval = "This is the video we created to introduce the above content, and I would like you to answer the following questions with (\"YES\" or \"NO\") to determine if the current video meets the requirements while maintaining structural integrity. If the answer is \"NO,\" please provide a reason:Is there visual content (animation) in the bottom left corner of the video? Is the animation in the video reasonable and mathematically strong? Do the visual content and text avoid meanlingless overlap in the video?"

pro_vis_rege = "The code you write has the following issues, please output the updated code ONLY:"

gen_vis_eval = "This is the video we created to introduce the above content, and I would like you to answer the following questions with (\"YES\" or \"NO\") to determine if the current video meets the requirements while maintaining structural integrity. If the answer is \"NO,\" please provide a reason:  Does it convey serious subject matter? Is the image filled with vivid scenes rather than meaningless numbers, letters, and symbols? Is the image strongly relevant to the following description?"

slides_vis_eval = "This is the video we created to introduce the above content, and I would like you to answer the following questions with (\"YES\" or \"NO\") . Is the following text works well as a caption beneath an image in a PowerPoint slide?  Is the following text explaining the image? Following text:"