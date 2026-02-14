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

low_level_planning_prompt = """
Your task is to generate a detailed low-level plan for a single video scene based on the high-level description provided below.

Input Scene:
{scene_json}

Style Advice:
{style_advice}

You must design the best presentation layout and animation plan for this specific scene.
Do NOT default to a generic template. Analyze the content and the Style Advice below to make a decision.

Step 1: Analyze Content & Reference
- What is the core information? (A complex diagram? A list of contributions? A set of numerical results?)
- Look at the [Style Advice] provided. Does it suggest a specific layout for this content type?
- Decide on the `target_layout` that best visualizes this specific content.

Step 2: Design the Slide & Builds
- How should the information appear? 
- `builds` are CRITICAL. Determine how to break the content into 2-4 reveals.
- Example: If explaining a diagram, reveal the input -> then the encoder -> then the output.
- Example: If listing contributions, show them one by one.
- Define specific visual emphasis (e.g., highlighting a bounding box on a figure).

Step 3: Generate JSON
Output the plan strictly following the JSON schema.
- `style`: Generally "Slides" (unless a specific "Professional" visualization is required).
- `layout`: Define the geometry of regions based on your design.

```json
{{
  "scene_id": 1,
  "scenario": "Detailed visual description...",
  "time_cost_sec": 7,
  "audio_content": "Verbal narration script...",
  "style": "Slides", 
  "source": ["Figure 1"],
  "layout": {{
    "template": "two_col_fig_left",
    "background_color": "#FFFFFF",
    "regions": {{
      "title":   {{"x": 0.05, "y": 0.05, "w": 0.90, "h": 0.10}},
      "figure":  {{"x": 0.05, "y": 0.20, "w": 0.45, "h": 0.70}},
      "bullets": {{"x": 0.55, "y": 0.20, "w": 0.40, "h": 0.70}}
    }}
  }},
  "elements": {{
    "title": "Scene Title",
    "figure": {{"type": "paper_figure", "ref": "Figure 1"}},
    "bullets": ["Point 1", "Point 2"]
  }},
  "builds": [
    {{
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [{{"type": "show", "target": "title"}}],
      "audio_segment": "Corresponding narration...",
      "visual_emphasis": []
    }},
    {{
      "step_index": 1,
      "time_offset_sec": 2.0,
      "actions": [{{"type": "fade_in", "target": "bullets[0]"}}],
      "audio_segment": "Next sentence...",
      "visual_emphasis": []
    }}
  ]
}}
```
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