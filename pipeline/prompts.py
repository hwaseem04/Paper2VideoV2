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

## STRICT RULES — You MUST follow these exactly:

1. **Region keys**: Only use these region keys in `layout.regions` and `elements`: `title`, `bullets`, `figure`. Do NOT invent new keys like `callout_1`, `callout_2`, `table`, `chart`, etc.
2. **Build count**: Set `expected_build_steps` to `1 + number_of_bullets`. Build 0 reveals the title (and optionally the figure), then each subsequent build reveals exactly one bullet. This OVERRIDES the high-level plan's `expected_build_steps`.
3. **Audio segments**: Every build step MUST have a non-empty `audio_segment` string. The audio_content should be split across build steps so each build has a meaningful narration chunk.
4. **Action targets**: Actions can only target elements that exist in `elements`. Valid targets: `title`, `figure`, `bullets[0]`, `bullets[1]`, `bullets[2]`, etc.
5. **Build 0 always shows title**: The first build (step_index 0) must always include `{{"type": "show", "target": "title"}}`.
6. **Figure reference**: If using a figure, `elements.figure` must be `{{"type": "paper_figure", "ref": "Figure X"}}` where X matches `primary_sources`.
7. **One bullet per build**: After build 0, each subsequent build step reveals exactly ONE bullet. Never reveal multiple bullets in the same build step.
8. **visual_emphasis**: Always set to empty list `[]`. Do not put anything in visual_emphasis.
9. **time_offset_sec**: Space build offsets evenly across the total time. For example, 4 builds over 10 seconds → offsets at 0.0, 2.5, 5.0, 7.5.
10. **No extra keys**: Do not add keys outside the schema shown in the example below.

## IDEAL EXAMPLE

Here is a PERFECT example of a well-formed low-level plan. Your output must follow this exact structure:

High-level input was:
```json
{{
    "scene_id": 1,
    "title": "Bridging the Gap in 3D Action Recognition",
    "summary": "Introduces the IKEA Ego 3D dataset, addressing the scarcity of ego-view 3D point cloud data. Unlike existing static-sensor datasets, this work focuses on fine-grained furniture assembly actions captured from a first-person perspective using a HoloLens 2.",
    "paper_section": "Introduction",
    "narrative_role": "problem",
    "time_allocation_sec": 7,
    "target_layout": "two_col_fig_left",
    "text_density": "low",
    "visual_density": "medium",
    "uses_builds": true,
    "expected_build_steps": 2,
    "primary_sources": ["Figure 1", "Section 1"],
    "reference_style_examples": ["3DInAction- Understanding Human Actions in 3D Point Clouds"]
  }}
```

Ideal output:
```json
{{
  "scenario": "The slide introduces the IKEA Ego 3D dataset, highlighting the problem of data scarcity in ego-view 3D action recognition. Figure 1, showing the dataset overview, is positioned on the left, while a bullet on the right summarizes the limitations of existing static-sensor datasets.",
  "time_cost_sec": 7,
  "audio_content": "Current 3D action recognition is limited by static sensors and a lack of ego-view data. We introduce the IKEA Ego 3D dataset to bridge this gap.",
  "style": "Slides",
  "source": [
    "Figure 1",
    "Section 1"
  ],
  "layout": {{
    "template": "two_col_fig_left",
    "background_color": "#FFFFFF",
    "regions": {{
      "title": {{
        "x": 0.05,
        "y": 0.05,
        "w": 0.9,
        "h": 0.1
      }},
      "figure": {{
        "x": 0.05,
        "y": 0.2,
        "w": 0.45,
        "h": 0.7
      }},
      "bullets": {{
        "x": 0.55,
        "y": 0.25,
        "w": 0.4,
        "h": 0.6
      }}
    }}
  }},
  "elements": {{
    "title": "Bridging the Gap in 3D Action Recognition",
    "figure": {{
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "Overview of the IKEA Ego 3D dataset"
    }},
    "bullets": [
      "Static sensors hinder fine-grained ego-view recognition"
    ]
  }},
  "expected_build_steps": 2,
  "builds": [
    {{
      "step_index": 0,
      "time_offset_sec": 0.0,
      "actions": [
        {{
          "type": "show",
          "target": "title"
        }},
        {{
          "type": "show",
          "target": "figure"
        }}
      ],
      "audio_segment": "Current 3D action recognition is limited by static sensors and a lack of ego-view data.",
      "visual_emphasis": []
    }},
    {{
      "step_index": 1,
      "time_offset_sec": 3.5,
      "actions": [
        {{
          "type": "fade_in",
          "target": "bullets[0]"
        }}
      ],
      "audio_segment": "We introduce the IKEA Ego 3D dataset to bridge this gap.",
      "visual_emphasis": []
    }}
  ]
}}
```

Notice how:
- There are exactly 4 builds and `expected_build_steps` is 4
- Build 0 shows title + figure together
- Builds 1-3 each reveal one bullet
- Audio_content is split across 4 audio_segments
- time_offset_sec values are evenly spaced (0.0, 2.5, 5.0, 7.5 across 10 seconds)
- Only `title`, `bullets`, `figure` are used as region keys
- visual_emphasis is always empty

Now generate the low-level plan for the Input Scene above. Output ONLY valid JSON, no markdown fences, no explanation.
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