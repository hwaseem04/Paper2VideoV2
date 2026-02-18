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
- NeurIPS_NeurIPS-2024_Dual-Prototype-Evolving-for-Test-Time-Generalizatio__NeurIPS-2024-Dual-Prototype-Evolving-for_Media
- CVPR_CVPR 2025_ Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Object__Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper
- Unsqueeze [CLS] Bottleneck to Learn Rich Representations

## Reference Presentation Styles (from existing videos):
- Video 'NeurIPS_NeurIPS-2024_Dual-Prototype-Evolving-for-Test-Time-Generalizatio__NeurIPS-2024-Dual-Prototype-Evolving-for_Media': approx 5 slides, 1.6 builds/slide.
- Video 'CVPR_CVPR 2025_ Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Object__Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper': approx 3 slides, 1.7 builds/slide.
- Video 'Unsqueeze [CLS] Bottleneck to Learn Rich Representations': approx 3 slides, 1.0 builds/slide.

RECOMMENDATION: Target approximately 9 scenes (Calculated from 19 pages of content and reference styles).

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
    "title": "The Challenge of Double-Blind Adaptation",
    "summary": "Foundation Models (FMs) require task-specific adaptation, but privacy barriers exist: Learning Service Providers (LSPs) must protect proprietary models, while data owners must keep sensitive data confidential. This creates a 'double-blind' constraint where neither party can access the other's assets.",
    "paper_section": "Introduction",
    "narrative_role": "problem",
    "time_allocation_sec": 7,
    "reference_style_examples": ["NeurIPS-2024-Dual-Prototype-Evolving-for_Media"]
  },
  {
    "scene_id": 2,
    "title": "Introducing BlindFed",
    "summary": "BlindFed is a framework for collaborative FM adaptation using Fully Homomorphic Encryption (FHE). It enables data owners to adapt models without accessing the FM, while the LSP performs computations without seeing the raw task data.",
    "paper_section": "Abstract",
    "narrative_role": "solution",
    "time_allocation_sec": 6,
    "reference_style_examples": ["Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"]
  },
  {
    "scene_id": 3,
    "title": "FHE-Friendly Architecture Redesign",
    "summary": "To support encrypted inference, standard non-linear operations like Softmax, GELU, and LayerNorm are replaced with low-degree polynomial approximations, such as Taylor series and quadratic functions, making the FM compatible with FHE schemes like CKKS.",
    "paper_section": "Proposed BlindFed Framework",
    "narrative_role": "methodology",
    "time_allocation_sec": 8,
    "reference_style_examples": ["Unsqueeze [CLS] Bottleneck to Learn Rich Representations"]
  },
  {
    "scene_id": 4,
    "title": "Stage 1: Offline Knowledge Distillation",
    "summary": "The LSP first performs offline distillation using an auxiliary dataset. The original FM acts as a teacher to train the FHE-friendly 'student' model, ensuring the approximated blocks retain the representational power of the original foundation model.",
    "paper_section": "Two-stage Split Learning",
    "narrative_role": "methodology",
    "time_allocation_sec": 7,
    "reference_style_examples": ["NeurIPS-2024-Dual-Prototype-Evolving-for_Media"]
  },
  {
    "scene_id": 5,
    "title": "Stage 2: Online Encrypted Inference",
    "summary": "During adaptation, clients encrypt their data and interact with the server block-by-block. Clients decrypt and re-encrypt intermediate representations to manage multiplicative depth, ensuring the server never sees the plaintext data.",
    "paper_section": "Encrypted Inference",
    "narrative_role": "methodology",
    "time_allocation_sec": 9,
    "reference_style_examples": ["Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"]
  },
  {
    "scene_id": 6,
    "title": "Local Learning and Secure Aggregation",
    "summary": "Clients receive intermediate representations to train local low-rank parallel adapters and classification heads. These local updates are then combined using MPC-based secure aggregation to form a global adapted model.",
    "paper_section": "Local Learning",
    "narrative_role": "methodology",
    "time_allocation_sec": 8,
    "reference_style_examples": ["Unsqueeze [CLS] Bottleneck to Learn Rich Representations"]
  },
  {
    "scene_id": 7,
    "title": "Boosting Model Privacy",
    "summary": "To prevent model extraction attacks, BlindFed introduces sample-level permutation and Stochastic Block Sampling (SBS). These techniques ensure clients cannot easily map input-output pairs of individual transformer blocks.",
    "paper_section": "Model Privacy Boosting",
    "narrative_role": "methodology",
    "time_allocation_sec": 7,
    "reference_style_examples": ["NeurIPS-2024-Dual-Prototype-Evolving-for_Media"]
  },
  {
    "scene_id": 8,
    "title": "Empirical Performance Results",
    "summary": "Experiments on CIFAR-10, CIFAR-100, and SVHN show that BlindFed achieves accuracy comparable to LoRA and full fine-tuning, significantly outperforming standard linear probing while maintaining strict double-blind privacy.",
    "paper_section": "Experiments and Results",
    "narrative_role": "result",
    "time_allocation_sec": 8,
    "reference_style_examples": ["Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"]
  },
  {
    "scene_id": 9,
    "title": "Efficiency and Scalability",
    "summary": "While FHE introduces computational overhead, BlindFed remains efficient in terms of trainable parameters and GPU memory. It demonstrates scalability across varying numbers of clients and heterogeneous data distributions.",
    "paper_section": "Conclusions",
    "narrative_role": "conclusion",
    "time_allocation_sec": 7,
    "reference_style_examples": ["Unsqueeze [CLS] Bottleneck to Learn Rich Representations"]
  }
]
```"""

Token usage so far: 10521 prompt tokens, 1309 completion tokens

Cost so far: $0.14448

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
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {"name": "Nurbek Tastan", "affiliation_id": 1},
    {"name": "Karthik Nandakumar", "affiliation_id": 2}
  ],
  "affiliations": [
    {"id": 1, "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE", "email_domain": "mbzuai.ac.ae"},
    {"id": 2, "name": "Michigan State University (MSU), USA", "email_domain": "msu.edu"}
  ],
  "venue": ""
}"""

Token usage so far: 20764 prompt tokens, 1470 completion tokens

Cost so far: $0.25174

**Question**

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE)
affiliation_2_logo: affiliation_2.png (Michigan State University (MSU), USA)

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
    "conference_logo": {
      "x": 0.8,
      "y": 0.05,
      "w": 0.15,
      "h": 0.1
    },
    "affiliation_logos": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.35,
      "h": 0.1
    },
    "title": {
      "x": 0.05,
      "y": 0.25,
      "w": 0.9,
      "h": 0.2
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.08
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.6,
      "w": 0.8,
      "h": 0.12
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.06
    }
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum impact, followed by a clear hierarchy for authors and their respective institutional details. The venue is placed at the bottom to anchor the design."
}"""

Token usage so far: 31471 prompt tokens, 1887 completion tokens

Cost so far: $0.37132

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 1,
  "title": "The Challenge of Double-Blind Adaptation",
  "summary": "Foundation Models (FMs) require task-specific adaptation, but privacy barriers exist: Learning Service Providers (LSPs) must protect proprietary models, while data owners must keep sensitive data confidential. This creates a 'double-blind' constraint where neither party can access the other's assets.",
  "paper_section": "Introduction",
  "narrative_role": "problem",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViTs achieve state-of-the-art results but require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: computational complexity and data availability. Privacy concerns and regulations prevent data owners (e.g., hospitals or banks) from sharing sensitive datasets with the Learning Service Provider (LSP). Simultaneously, proprietary restrictions prevent the LSP from sharing the FM weights with data owners. This creates a 'double-blind' privacy constraint where (i) the LSP must not learn anything about local datasets (Data Privacy) and (ii) data owners must not learn anything about the original FM (Model Privacy). Existing parameter-efficient fine-tuning (PEFT) methods like LoRA typically require backpropagation through the FM backbone, which is computationally expensive and often incompatible with these privacy constraints.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "Visually defines the 'double-blind' scenario where the LSP (Server) and Data Owners (Clients) collaborate to adapt an FM without accessing each other's proprietary assets or sensitive data."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 1",
    "Section 3"
  ]
}"""

Token usage so far: 41927 prompt tokens, 2220 completion tokens

Cost so far: $0.48587

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViTs achieve state-of-the-art results but require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: computational complexity and data availability. Privacy concerns and regulations prevent data owners (e.g., hospitals or banks) from sharing sensitive datasets with the Learning Service Provider (LSP). Simultaneously, proprietary restrictions prevent the LSP from sharing the FM weights with data owners. This creates a 'double-blind' privacy constraint where (i) the LSP must not learn anything about local datasets (Data Privacy) and (ii) data owners must not learn anything about the original FM (Model Privacy). Existing parameter-efficient fine-tuning (PEFT) methods like LoRA typically require backpropagation through the FM backbone, which is computationally expensive and often incompatible with these privacy constraints.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "Visually defines the 'double-blind' scenario where the LSP (Server) and Data Owners (Clients) collaborate to adapt an FM without accessing each other's proprietary assets or sensitive data."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 1",
    "Section 3"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 1,
  "title": "The Challenge of Double-Blind Adaptation",
  "summary": "Foundation Models (FMs) require task-specific adaptation, but privacy barriers exist: Learning Service Providers (LSPs) must protect proprietary models, while data owners must keep sensitive data confidential. This creates a 'double-blind' constraint where neither party can access the other's assets.",
  "paper_section": "Introduction",
  "narrative_role": "problem",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with bullets on the left and the conceptual figure on the right is ideal for a problem motivation slide. It allows the text to define the 'double-blind' constraints while Figure 1 provides the visual context of the LSP-Client interaction."
}"""

Token usage so far: 52996 prompt tokens, 2479 completion tokens

Cost so far: $0.60433

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "Foundation models (FMs) like GPT, CLIP, and ViTs achieve state-of-the-art results but require task-specific adaptation for challenging out-of-domain tasks such as medical or satellite imagery. This adaptation process faces two primary hurdles: computational complexity and data availability. Privacy concerns and regulations prevent data owners (e.g., hospitals or banks) from sharing sensitive datasets with the Learning Service Provider (LSP). Simultaneously, proprietary restrictions prevent the LSP from sharing the FM weights with data owners. This creates a 'double-blind' privacy constraint where (i) the LSP must not learn anything about local datasets (Data Privacy) and (ii) data owners must not learn anything about the original FM (Model Privacy). Existing parameter-efficient fine-tuning (PEFT) methods like LoRA typically require backpropagation through the FM backbone, which is computationally expensive and often incompatible with these privacy constraints.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "Visually defines the 'double-blind' scenario where the LSP (Server) and Data Owners (Clients) collaborate to adapt an FM without accessing each other's proprietary assets or sensitive data."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Section 1",
    "Section 3"
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
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with bullets on the left and the conceptual figure on the right is ideal for a problem motivation slide. It allows the text to define the 'double-blind' constraints while Figure 1 provides the visual context of the LSP-Client interaction."
}

Scene context:
{
  "scene_id": 1,
  "title": "The Challenge of Double-Blind Adaptation",
  "summary": "Foundation Models (FMs) require task-specific adaptation, but privacy barriers exist: Learning Service Providers (LSPs) must protect proprietary models, while data owners must keep sensitive data confidential. This creates a 'double-blind' constraint where neither party can access the other's assets.",
  "paper_section": "Introduction",
  "narrative_role": "problem",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
  "title": "The Double-Blind Adaptation Challenge",
  "audio_content": "Adapting foundation models is vital, but privacy barriers create a double-blind challenge where neither the proprietary model nor the sensitive training data can be shared.",
  "bullets": [
    "FMs require task-specific adaptation for out-of-domain data",
    "Data Privacy: LSPs cannot access sensitive client datasets",
    "Model Privacy: Clients cannot access proprietary model weights"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "The double-blind privacy constraint between LSP and Data Owners."
  },
  "source": ["Figure 1", "Section 1", "Section 3"],
  "time_cost": "7",
  "prompt": "A slide showing the double-blind privacy problem. On the left, bullet points describe the conflict between model and data privacy. On the right, Figure 1 illustrates the conceptual framework where the LSP and clients collaborate without sharing assets."
}"""

Token usage so far: 64098 prompt tokens, 2716 completion tokens

Cost so far: $0.72246

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "The Double-Blind Adaptation Challenge",
  "audio_content": "Adapting foundation models is vital, but privacy barriers create a double-blind challenge where neither the proprietary model nor the sensitive training data can be shared.",
  "bullets": [
    "FMs require task-specific adaptation for out-of-domain data",
    "Data Privacy: LSPs cannot access sensitive client datasets",
    "Model Privacy: Clients cannot access proprietary model weights"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 1",
    "caption": "The double-blind privacy constraint between LSP and Data Owners."
  },
  "source": [
    "Figure 1",
    "Section 1",
    "Section 3"
  ],
  "time_cost": "7",
  "prompt": "A slide showing the double-blind privacy problem. On the left, bullet points describe the conflict between model and data privacy. On the right, Figure 1 illustrates the conceptual framework where the LSP and clients collaborate without sharing assets."
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
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": "7"
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
    "title": "The Double-Blind Adaptation Challenge",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 1",
      "caption": "The double-blind privacy constraint between LSP and Data Owners."
    },
    "bullets": [
      "FMs require task-specific adaptation for out-of-domain data",
      "Model Privacy: Clients cannot access proprietary model weights",
      "Data Privacy: LSPs cannot access sensitive client datasets"
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
      "audio_segment": "Adapting foundation models is vital,",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 1.75,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "but privacy barriers create a double-blind challenge",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 3.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "where neither the proprietary model",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 5.25,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "nor the sensitive training data can be shared.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 75220 prompt tokens, 3248 completion tokens

Cost so far: $0.84964

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 2,
  "title": "Introducing BlindFed",
  "summary": "BlindFed is a framework for collaborative FM adaptation using Fully Homomorphic Encryption (FHE). It enables data owners to adapt models without accessing the FM, while the LSP performs computations without seeing the raw task data.",
  "paper_section": "Abstract",
  "narrative_role": "solution",
  "time_allocation_sec": 6,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
  "extracted_content": "BlindFed is a framework designed for 'double-blind' federated adaptation of Foundation Models (FMs). It addresses two primary privacy constraints: Model Privacy (the Learning Service Provider (LSP) retains full ownership and does not share the FM with data owners) and Data Privacy (clients do not reveal their sensitive task data to the LSP or each other). The framework relies on Fully Homomorphic Encryption (FHE) and consists of three core innovations: (i) FHE-friendly architectural modifications that replace non-linear operations with polynomial approximations and utilize low-rank parallel adapters; (ii) a two-stage split learning approach that uses offline knowledge distillation on auxiliary data followed by online encrypted inference for adapter training without requiring backpropagation through the FM; and (iii) a privacy-boosting scheme using sample-level permutations and stochastic block sampling to mitigate model extraction attacks. Empirical results on image classification tasks demonstrate its feasibility, though it involves high communication and computational costs for the LSP.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "Provides a high-level visual summary of the 'double-blind' concept where neither the model nor the data is exposed to the opposing party."
    },
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation. The framework consists of three main components: (1) FHE-friendly architecture redesign, where the original foundation model (FM) is modified by approximating non-linear operations; (2) offline distillation, where the approximated blocks are fine-tuned via knowledge distillation using an auxiliary dataset; and (3) online adaptation, where clients interact the FHE-enabled FM under homomorphic encryption, performing local updates on the parallel adapter and classification head.",
      "relevance": "Details the specific workflow and three-stage process of the BlindFed solution."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Abstract",
    "1. Introduction"
  ]
}"""

Token usage so far: 85672 prompt tokens, 3730 completion tokens

Cost so far: $0.96862

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed is a framework designed for 'double-blind' federated adaptation of Foundation Models (FMs). It addresses two primary privacy constraints: Model Privacy (the Learning Service Provider (LSP) retains full ownership and does not share the FM with data owners) and Data Privacy (clients do not reveal their sensitive task data to the LSP or each other). The framework relies on Fully Homomorphic Encryption (FHE) and consists of three core innovations: (i) FHE-friendly architectural modifications that replace non-linear operations with polynomial approximations and utilize low-rank parallel adapters; (ii) a two-stage split learning approach that uses offline knowledge distillation on auxiliary data followed by online encrypted inference for adapter training without requiring backpropagation through the FM; and (iii) a privacy-boosting scheme using sample-level permutations and stochastic block sampling to mitigate model extraction attacks. Empirical results on image classification tasks demonstrate its feasibility, though it involves high communication and computational costs for the LSP.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "Provides a high-level visual summary of the 'double-blind' concept where neither the model nor the data is exposed to the opposing party."
    },
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation. The framework consists of three main components: (1) FHE-friendly architecture redesign, where the original foundation model (FM) is modified by approximating non-linear operations; (2) offline distillation, where the approximated blocks are fine-tuned via knowledge distillation using an auxiliary dataset; and (3) online adaptation, where clients interact the FHE-enabled FM under homomorphic encryption, performing local updates on the parallel adapter and classification head.",
      "relevance": "Details the specific workflow and three-stage process of the BlindFed solution."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Abstract",
    "1. Introduction"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 2,
  "title": "Introducing BlindFed",
  "summary": "BlindFed is a framework for collaborative FM adaptation using Fully Homomorphic Encryption (FHE). It enables data owners to adapt models without accessing the FM, while the LSP performs computations without seeing the raw task data.",
  "paper_section": "Abstract",
  "narrative_role": "solution",
  "time_allocation_sec": 6,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.15, "w": 0.9, "h": 0.55},
    "bullets": {"x": 0.05, "y": 0.75, "w": 0.9, "h": 0.2}
  },
  "has_figure": true,
  "style_rationale": "The 'full_fig_with_callouts' layout is chosen to showcase the comprehensive framework overview (Figure 2) as recommended for methodology content, allowing the wide pipeline diagram to be the focal point while bullets summarize the core innovations."
}"""

Token usage so far: 96886 prompt tokens, 3955 completion tokens

Cost so far: $1.08751

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed is a framework designed for 'double-blind' federated adaptation of Foundation Models (FMs). It addresses two primary privacy constraints: Model Privacy (the Learning Service Provider (LSP) retains full ownership and does not share the FM with data owners) and Data Privacy (clients do not reveal their sensitive task data to the LSP or each other). The framework relies on Fully Homomorphic Encryption (FHE) and consists of three core innovations: (i) FHE-friendly architectural modifications that replace non-linear operations with polynomial approximations and utilize low-rank parallel adapters; (ii) a two-stage split learning approach that uses offline knowledge distillation on auxiliary data followed by online encrypted inference for adapter training without requiring backpropagation through the FM; and (iii) a privacy-boosting scheme using sample-level permutations and stochastic block sampling to mitigate model extraction attacks. Empirical results on image classification tasks demonstrate its feasibility, though it involves high communication and computational costs for the LSP.",
  "key_figures": [
    {
      "ref": "Figure 1",
      "caption": "Conceptual illustration of BlindFed framework for double-blind federated adaptation of a foundation model.",
      "relevance": "Provides a high-level visual summary of the 'double-blind' concept where neither the model nor the data is exposed to the opposing party."
    },
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation. The framework consists of three main components: (1) FHE-friendly architecture redesign, where the original foundation model (FM) is modified by approximating non-linear operations; (2) offline distillation, where the approximated blocks are fine-tuned via knowledge distillation using an auxiliary dataset; and (3) online adaptation, where clients interact the FHE-enabled FM under homomorphic encryption, performing local updates on the parallel adapter and classification head.",
      "relevance": "Details the specific workflow and three-stage process of the BlindFed solution."
    }
  ],
  "key_tables": [],
  "key_equations": [],
  "section_refs": [
    "Abstract",
    "1. Introduction"
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
      "y": 0.15,
      "w": 0.9,
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "style_rationale": "The 'full_fig_with_callouts' layout is chosen to showcase the comprehensive framework overview (Figure 2) as recommended for methodology content, allowing the wide pipeline diagram to be the focal point while bullets summarize the core innovations."
}

Scene context:
{
  "scene_id": 2,
  "title": "Introducing BlindFed",
  "summary": "BlindFed is a framework for collaborative FM adaptation using Fully Homomorphic Encryption (FHE). It enables data owners to adapt models without accessing the FM, while the LSP performs computations without seeing the raw task data.",
  "paper_section": "Abstract",
  "narrative_role": "solution",
  "time_allocation_sec": 6,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
  "title": "Introducing BlindFed",
  "audio_content": "BlindFed uses FHE and split learning to adapt foundation models while keeping both the model and data private.",
  "bullets": [
    "Protects model and data privacy via Fully Homomorphic Encryption (FHE)",
    "FHE-friendly architecture using polynomial approximations and parallel adapters",
    "Two-stage split learning: offline distillation followed by online encrypted inference"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 2",
    "caption": "Overview of the BlindFed framework and its three-stage process."
  },
  "source": ["Abstract", "Figure 2", "Section 1"],
  "time_cost": "6",
  "prompt": "A wide architectural diagram showing the three stages of BlindFed: FHE-friendly redesign, offline distillation with an auxiliary dataset, and online adaptation with private datasets."
}"""

Token usage so far: 108132 prompt tokens, 4170 completion tokens

Cost so far: $1.20642

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Introducing BlindFed",
  "audio_content": "BlindFed uses FHE and split learning to adapt foundation models while keeping both the model and data private.",
  "bullets": [
    "Protects model and data privacy via Fully Homomorphic Encryption (FHE)",
    "FHE-friendly architecture using polynomial approximations and parallel adapters",
    "Two-stage split learning: offline distillation followed by online encrypted inference"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 2",
    "caption": "Overview of the BlindFed framework and its three-stage process."
  },
  "source": [
    "Abstract",
    "Figure 2",
    "Section 1"
  ],
  "time_cost": "6",
  "prompt": "A wide architectural diagram showing the three stages of BlindFed: FHE-friendly redesign, offline distillation with an auxiliary dataset, and online adaptation with private datasets."
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
      "y": 0.15,
      "w": 0.9,
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "total_time_sec": "6"
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
    "title": "Introducing BlindFed",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 2",
      "caption": "Overview of the BlindFed framework and its three-stage process."
    },
    "bullets": [
      "Protects model and data privacy via Fully Homomorphic Encryption (FHE)",
      "FHE-friendly architecture using polynomial approximations and parallel adapters",
      "Two-stage split learning: offline distillation followed by online encrypted inference"
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
      "audio_segment": "BlindFed uses FHE and split learning to adapt foundation models while keeping both the model and data private.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 1.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "It protects model and data privacy via Fully Homomorphic Encryption.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 3.0,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "The framework employs an FHE-friendly architecture using polynomial approximations and parallel adapters.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 4.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "And it utilizes two-stage split learning, starting with offline distillation followed by online encrypted inference.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 119236 prompt tokens, 4739 completion tokens

Cost so far: $1.33453

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 3,
  "title": "FHE-Friendly Architecture Redesign",
  "summary": "To support encrypted inference, standard non-linear operations like Softmax, GELU, and LayerNorm are replaced with low-degree polynomial approximations, such as Taylor series and quadratic functions, making the FM compatible with FHE schemes like CKKS.",
  "paper_section": "Proposed BlindFed Framework",
  "narrative_role": "methodology",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "extracted_content": "To enable encrypted inference using Fully Homomorphic Encryption (FHE) schemes like CKKS, the Foundation Model (FM) must be redesigned because FHE only supports polynomial operations (addition and multiplication). The BlindFed framework replaces standard non-linear transformer operations with low-degree polynomial approximations: Softmax is approximated using a Taylor series expansion for the exponential function; GELU is replaced by a quadratic function (0.125x² + 0.25x + 0.5); and the division steps in LayerNorm and Softmax are implemented via Goldschmidt’s algorithm. Furthermore, the architecture is modified to use parallel adapters (LoSA) instead of sequential ones (LoRA) because sequential adapters would require backpropagation through the FM, which is computationally infeasible when data remains encrypted. This redesign allows the server to perform encrypted forward passes while the client trains the adapter on plaintext intermediate representations.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign. Each transformer block’s non-linear operations – GELU activations, Softmax attention, and the division step in LayerNorm – are replaced with low-degree polynomial approximations (denoted “Quad” for GELU and “ASoftmax” for Softmax). A lightweight parallel adapter and classification head are then trained on the client side.",
      "relevance": "This figure provides the visual blueprint for the architectural changes described in this scene, showing exactly which components are replaced."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results. Latency is computed per a batch of samples, when batch size is set to 8. One-epoch accuracy refers to the accuracy we obtain when performing one full pass over the data for only one epoch. This experiment is carried on the Fed-ISIC2019(center=0) dataset.",
      "relevance": "Demonstrates the trade-off between the degree of the polynomial approximation (d) and the resulting model accuracy and latency."
    },
    {
      "ref": "Table 6",
      "caption": "Approximation of the reciprocal (inverse function). Latency is computed per a batch of samples (aggregate over L transformer blocks), when batch size is set to 8. One-epoch accuracy refers to the accuracy we obtain when performing one full pass over the data for only one epoch. This experiment is carried on the Fed-ISIC2019 (center=0) dataset.",
      "relevance": "Shows the effectiveness of using Goldschmidt’s algorithm to approximate the division operation required for LayerNorm in an FHE context."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \\frac{x^i}{i!} \\approx \\sum_{i=0}^{d} \\frac{x^i}{i!}",
      "relevance": "Defines the Taylor series approximation used to replace the exponential function in Softmax."
    },
    {
      "ref": "Equation 4",
      "content": "GELU(x) \\approx Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "The specific quadratic polynomial used to replace the GELU activation function."
    },
    {
      "ref": "Equation 5",
      "content": "\\frac{1}{x} = \\frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1+(1-x)^{2^i}) \\approx \\prod_{i=0}^{d} (1+(1-x)^{2^i})",
      "relevance": "Goldschmidt’s algorithm used to approximate division, which is necessary for LayerNorm and Softmax normalization."
    }
  ],
  "section_refs": [
    "Section 4.1",
    "Section D.4"
  ]
}"""

Token usage so far: 129680 prompt tokens, 5655 completion tokens

Cost so far: $1.46645

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "To enable encrypted inference using Fully Homomorphic Encryption (FHE) schemes like CKKS, the Foundation Model (FM) must be redesigned because FHE only supports polynomial operations (addition and multiplication). The BlindFed framework replaces standard non-linear transformer operations with low-degree polynomial approximations: Softmax is approximated using a Taylor series expansion for the exponential function; GELU is replaced by a quadratic function (0.125x\u00b2 + 0.25x + 0.5); and the division steps in LayerNorm and Softmax are implemented via Goldschmidt\u2019s algorithm. Furthermore, the architecture is modified to use parallel adapters (LoSA) instead of sequential ones (LoRA) because sequential adapters would require backpropagation through the FM, which is computationally infeasible when data remains encrypted. This redesign allows the server to perform encrypted forward passes while the client trains the adapter on plaintext intermediate representations.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign. Each transformer block\u2019s non-linear operations \u2013 GELU activations, Softmax attention, and the division step in LayerNorm \u2013 are replaced with low-degree polynomial approximations (denoted \u201cQuad\u201d for GELU and \u201cASoftmax\u201d for Softmax). A lightweight parallel adapter and classification head are then trained on the client side.",
      "relevance": "This figure provides the visual blueprint for the architectural changes described in this scene, showing exactly which components are replaced."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results. Latency is computed per a batch of samples, when batch size is set to 8. One-epoch accuracy refers to the accuracy we obtain when performing one full pass over the data for only one epoch. This experiment is carried on the Fed-ISIC2019(center=0) dataset.",
      "relevance": "Demonstrates the trade-off between the degree of the polynomial approximation (d) and the resulting model accuracy and latency."
    },
    {
      "ref": "Table 6",
      "caption": "Approximation of the reciprocal (inverse function). Latency is computed per a batch of samples (aggregate over L transformer blocks), when batch size is set to 8. One-epoch accuracy refers to the accuracy we obtain when performing one full pass over the data for only one epoch. This experiment is carried on the Fed-ISIC2019 (center=0) dataset.",
      "relevance": "Shows the effectiveness of using Goldschmidt\u2019s algorithm to approximate the division operation required for LayerNorm in an FHE context."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \frac{x^i}{i!} \u0007pprox \\sum_{i=0}^{d} \frac{x^i}{i!}",
      "relevance": "Defines the Taylor series approximation used to replace the exponential function in Softmax."
    },
    {
      "ref": "Equation 4",
      "content": "GELU(x) \u0007pprox Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "The specific quadratic polynomial used to replace the GELU activation function."
    },
    {
      "ref": "Equation 5",
      "content": "\frac{1}{x} = \frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1+(1-x)^{2^i}) \u0007pprox \\prod_{i=0}^{d} (1+(1-x)^{2^i})",
      "relevance": "Goldschmidt\u2019s algorithm used to approximate division, which is necessary for LayerNorm and Softmax normalization."
    }
  ],
  "section_refs": [
    "Section 4.1",
    "Section D.4"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 3,
  "title": "FHE-Friendly Architecture Redesign",
  "summary": "To support encrypted inference, standard non-linear operations like Softmax, GELU, and LayerNorm are replaced with low-degree polynomial approximations, such as Taylor series and quadratic functions, making the FM compatible with FHE schemes like CKKS.",
  "paper_section": "Proposed BlindFed Framework",
  "narrative_role": "methodology",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.2, "w": 0.4, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the architecture diagram (Figure 3) on the left is the most effective way to visualize the specific component replacements described in the text. The bullets on the right provide the mathematical context for the 'Quad' and 'ASoftmax' labels seen in the figure."
}"""

Token usage so far: 141385 prompt tokens, 5888 completion tokens

Cost so far: $1.59049

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "To enable encrypted inference using Fully Homomorphic Encryption (FHE) schemes like CKKS, the Foundation Model (FM) must be redesigned because FHE only supports polynomial operations (addition and multiplication). The BlindFed framework replaces standard non-linear transformer operations with low-degree polynomial approximations: Softmax is approximated using a Taylor series expansion for the exponential function; GELU is replaced by a quadratic function (0.125x\u00b2 + 0.25x + 0.5); and the division steps in LayerNorm and Softmax are implemented via Goldschmidt\u2019s algorithm. Furthermore, the architecture is modified to use parallel adapters (LoSA) instead of sequential ones (LoRA) because sequential adapters would require backpropagation through the FM, which is computationally infeasible when data remains encrypted. This redesign allows the server to perform encrypted forward passes while the client trains the adapter on plaintext intermediate representations.",
  "key_figures": [
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign. Each transformer block\u2019s non-linear operations \u2013 GELU activations, Softmax attention, and the division step in LayerNorm \u2013 are replaced with low-degree polynomial approximations (denoted \u201cQuad\u201d for GELU and \u201cASoftmax\u201d for Softmax). A lightweight parallel adapter and classification head are then trained on the client side.",
      "relevance": "This figure provides the visual blueprint for the architectural changes described in this scene, showing exactly which components are replaced."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results. Latency is computed per a batch of samples, when batch size is set to 8. One-epoch accuracy refers to the accuracy we obtain when performing one full pass over the data for only one epoch. This experiment is carried on the Fed-ISIC2019(center=0) dataset.",
      "relevance": "Demonstrates the trade-off between the degree of the polynomial approximation (d) and the resulting model accuracy and latency."
    },
    {
      "ref": "Table 6",
      "caption": "Approximation of the reciprocal (inverse function). Latency is computed per a batch of samples (aggregate over L transformer blocks), when batch size is set to 8. One-epoch accuracy refers to the accuracy we obtain when performing one full pass over the data for only one epoch. This experiment is carried on the Fed-ISIC2019 (center=0) dataset.",
      "relevance": "Shows the effectiveness of using Goldschmidt\u2019s algorithm to approximate the division operation required for LayerNorm in an FHE context."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 3",
      "content": "e^x = \\sum_{i=0}^{\\infty} \frac{x^i}{i!} \u0007pprox \\sum_{i=0}^{d} \frac{x^i}{i!}",
      "relevance": "Defines the Taylor series approximation used to replace the exponential function in Softmax."
    },
    {
      "ref": "Equation 4",
      "content": "GELU(x) \u0007pprox Quad(x) = 0.125x^2 + 0.25x + 0.5",
      "relevance": "The specific quadratic polynomial used to replace the GELU activation function."
    },
    {
      "ref": "Equation 5",
      "content": "\frac{1}{x} = \frac{1}{1-(1-x)} = \\prod_{i=0}^{\\infty} (1+(1-x)^{2^i}) \u0007pprox \\prod_{i=0}^{d} (1+(1-x)^{2^i})",
      "relevance": "Goldschmidt\u2019s algorithm used to approximate division, which is necessary for LayerNorm and Softmax normalization."
    }
  ],
  "section_refs": [
    "Section 4.1",
    "Section D.4"
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
      "w": 0.45,
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
  "style_rationale": "A two-column layout with the architecture diagram (Figure 3) on the left is the most effective way to visualize the specific component replacements described in the text. The bullets on the right provide the mathematical context for the 'Quad' and 'ASoftmax' labels seen in the figure."
}

Scene context:
{
  "scene_id": 3,
  "title": "FHE-Friendly Architecture Redesign",
  "summary": "To support encrypted inference, standard non-linear operations like Softmax, GELU, and LayerNorm are replaced with low-degree polynomial approximations, such as Taylor series and quadratic functions, making the FM compatible with FHE schemes like CKKS.",
  "paper_section": "Proposed BlindFed Framework",
  "narrative_role": "methodology",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "title": "FHE-Friendly Architecture Redesign",
  "audio_content": "To enable encrypted inference, we replace non-linearities with polynomial approximations and switch to parallel adapters, avoiding backpropagation through the FM.",
  "bullets": [
    "Polynomial approximations replace non-linear GELU and Softmax operations",
    "Goldschmidt’s algorithm enables FHE-compatible division for LayerNorm",
    "Parallel adapters (LoSA) eliminate the need for encrypted backpropagation"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Redesigning transformer blocks with polynomial 'Quad' and 'ASoftmax' components."
  },
  "source": [
    "Section 4.1",
    "Figure 3"
  ],
  "time_cost": "8",
  "prompt": "A slide showing Figure 3 from the paper on the left, illustrating the replacement of GELU and Softmax with polynomial approximations. On the right, bullet points explain the use of Taylor series, quadratic functions, and parallel adapters for FHE compatibility."
}"""

Token usage so far: 153138 prompt tokens, 6146 completion tokens

Cost so far: $1.71576

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "FHE-Friendly Architecture Redesign",
  "audio_content": "To enable encrypted inference, we replace non-linearities with polynomial approximations and switch to parallel adapters, avoiding backpropagation through the FM.",
  "bullets": [
    "Polynomial approximations replace non-linear GELU and Softmax operations",
    "Goldschmidt\u2019s algorithm enables FHE-compatible division for LayerNorm",
    "Parallel adapters (LoSA) eliminate the need for encrypted backpropagation"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Redesigning transformer blocks with polynomial 'Quad' and 'ASoftmax' components."
  },
  "source": [
    "Section 4.1",
    "Figure 3"
  ],
  "time_cost": "8",
  "prompt": "A slide showing Figure 3 from the paper on the left, illustrating the replacement of GELU and Softmax with polynomial approximations. On the right, bullet points explain the use of Taylor series, quadratic functions, and parallel adapters for FHE compatibility."
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
      "w": 0.45,
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
    "title": "FHE-Friendly Architecture Redesign",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 3",
      "caption": "Redesigning transformer blocks with polynomial 'Quad' and 'ASoftmax' components."
    },
    "bullets": [
      "Polynomial approximations replace non-linear GELU and Softmax operations",
      "Goldschmidt’s algorithm enables FHE-compatible division for LayerNorm",
      "Parallel adapters (LoSA) eliminate the need for encrypted backpropagation"
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
      "audio_segment": "To enable encrypted inference, we must first redesign the model architecture.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[0]"}
      ],
      "audio_segment": "We replace non-linearities with polynomial approximations for GELU and Softmax.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 4.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[1]"}
      ],
      "audio_segment": "Goldschmidt’s algorithm is then used to enable FHE-compatible division.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 6.0,
      "actions": [
        {"type": "fade_in", "target": "bullets[2]"}
      ],
      "audio_segment": "Finally, we switch to parallel adapters, avoiding backpropagation through the FM.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 164277 prompt tokens, 6684 completion tokens

Cost so far: $1.84329

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 4,
  "title": "Stage 1: Offline Knowledge Distillation",
  "summary": "The LSP first performs offline distillation using an auxiliary dataset. The original FM acts as a teacher to train the FHE-friendly 'student' model, ensuring the approximated blocks retain the representational power of the original foundation model.",
  "paper_section": "Two-stage Split Learning",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
  "extracted_content": "The Learning Service Provider (LSP) performs offline knowledge distillation to train an FHE-friendly 'student' model using the original foundation model as a 'teacher' on an independent auxiliary dataset ($D_{aux}$). This process is conducted in two stages: the first 15 epochs focus on distilling intermediate representations, including embeddings, attention matrices (pre-normalization), and hidden states after each block. The subsequent 15 epochs focus on prediction-layer distillation by matching logits. The objective is to ensure that the redesigned model—which replaces non-linear operations like Softmax and GELU with polynomial approximations—retains the representational power and accuracy of the original FM before any client collaboration occurs.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Shows the 'Offline Distillation' step as a core component of the server-side workflow using an auxiliary dataset."
    },
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Provides a detailed visual representation of how attention matrices and hidden representations are distilled from the teacher model to the student model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the effectiveness of the distillation process in maintaining accuracy while using polynomial approximations of varying degrees."
    },
    {
      "ref": "Table 6",
      "caption": "Approximation of the reciprocal (inverse function).",
      "relevance": "Shows the distillation results for the approximated inverse function used in LayerNorm and Softmax."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 17",
      "content": "\\mathcal{L}_a = \\frac{1}{h} \\sum_{i=1}^h ||\\mathbf{A}_i^S - \\mathbf{A}_i^T||^2",
      "relevance": "Defines the loss function for distilling attention matrices between the student and teacher models."
    },
    {
      "ref": "Equation 18",
      "content": "\\mathcal{L}_h = ||\\mathbf{H}^S - \\mathbf{H}^T||^2",
      "relevance": "Defines the loss function for distilling hidden representations."
    },
    {
      "ref": "Equation 20",
      "content": "\\mathcal{L}_p = \\mathcal{L}_{CE}(\\mathbf{z}^S/\\tau, \\mathbf{z}^T/\\tau)",
      "relevance": "Defines the logit-matching loss used in the second stage of the distillation process."
    }
  ],
  "section_refs": [
    "Section 4.2",
    "Appendix C"
  ]
}"""

Token usage so far: 174726 prompt tokens, 7377 completion tokens

Cost so far: $1.96857

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The Learning Service Provider (LSP) performs offline knowledge distillation to train an FHE-friendly 'student' model using the original foundation model as a 'teacher' on an independent auxiliary dataset ($D_{aux}$). This process is conducted in two stages: the first 15 epochs focus on distilling intermediate representations, including embeddings, attention matrices (pre-normalization), and hidden states after each block. The subsequent 15 epochs focus on prediction-layer distillation by matching logits. The objective is to ensure that the redesigned model\u2014which replaces non-linear operations like Softmax and GELU with polynomial approximations\u2014retains the representational power and accuracy of the original FM before any client collaboration occurs.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Shows the 'Offline Distillation' step as a core component of the server-side workflow using an auxiliary dataset."
    },
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Provides a detailed visual representation of how attention matrices and hidden representations are distilled from the teacher model to the student model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the effectiveness of the distillation process in maintaining accuracy while using polynomial approximations of varying degrees."
    },
    {
      "ref": "Table 6",
      "caption": "Approximation of the reciprocal (inverse function).",
      "relevance": "Shows the distillation results for the approximated inverse function used in LayerNorm and Softmax."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 17",
      "content": "\\mathcal{L}_a = \frac{1}{h} \\sum_{i=1}^h ||\\mathbf{A}_i^S - \\mathbf{A}_i^T||^2",
      "relevance": "Defines the loss function for distilling attention matrices between the student and teacher models."
    },
    {
      "ref": "Equation 18",
      "content": "\\mathcal{L}_h = ||\\mathbf{H}^S - \\mathbf{H}^T||^2",
      "relevance": "Defines the loss function for distilling hidden representations."
    },
    {
      "ref": "Equation 20",
      "content": "\\mathcal{L}_p = \\mathcal{L}_{CE}(\\mathbf{z}^S/\tau, \\mathbf{z}^T/\tau)",
      "relevance": "Defines the logit-matching loss used in the second stage of the distillation process."
    }
  ],
  "section_refs": [
    "Section 4.2",
    "Appendix C"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 4,
  "title": "Stage 1: Offline Knowledge Distillation",
  "summary": "The LSP first performs offline distillation using an auxiliary dataset. The original FM acts as a teacher to train the FHE-friendly 'student' model, ensuring the approximated blocks retain the representational power of the original foundation model.",
  "paper_section": "Two-stage Split Learning",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.25,
      "w": 0.35,
      "h": 0.6
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to showcase the detailed teacher-student distillation schematic (Figure 9) on the left, while summarizing the two-stage training process and loss objectives in bullets on the right. This provides a clear mapping between the visual architecture and the mathematical distillation steps within the short 7-second window."
}"""

Token usage so far: 186156 prompt tokens, 7649 completion tokens

Cost so far: $2.09103

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The Learning Service Provider (LSP) performs offline knowledge distillation to train an FHE-friendly 'student' model using the original foundation model as a 'teacher' on an independent auxiliary dataset ($D_{aux}$). This process is conducted in two stages: the first 15 epochs focus on distilling intermediate representations, including embeddings, attention matrices (pre-normalization), and hidden states after each block. The subsequent 15 epochs focus on prediction-layer distillation by matching logits. The objective is to ensure that the redesigned model\u2014which replaces non-linear operations like Softmax and GELU with polynomial approximations\u2014retains the representational power and accuracy of the original FM before any client collaboration occurs.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Shows the 'Offline Distillation' step as a core component of the server-side workflow using an auxiliary dataset."
    },
    {
      "ref": "Figure 9",
      "caption": "Schematic illustration of the layer-wise knowledge distillation (Equations 17 and 18).",
      "relevance": "Provides a detailed visual representation of how attention matrices and hidden representations are distilled from the teacher model to the student model."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 5",
      "caption": "Softmax approximation results.",
      "relevance": "Demonstrates the effectiveness of the distillation process in maintaining accuracy while using polynomial approximations of varying degrees."
    },
    {
      "ref": "Table 6",
      "caption": "Approximation of the reciprocal (inverse function).",
      "relevance": "Shows the distillation results for the approximated inverse function used in LayerNorm and Softmax."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 17",
      "content": "\\mathcal{L}_a = \frac{1}{h} \\sum_{i=1}^h ||\\mathbf{A}_i^S - \\mathbf{A}_i^T||^2",
      "relevance": "Defines the loss function for distilling attention matrices between the student and teacher models."
    },
    {
      "ref": "Equation 18",
      "content": "\\mathcal{L}_h = ||\\mathbf{H}^S - \\mathbf{H}^T||^2",
      "relevance": "Defines the loss function for distilling hidden representations."
    },
    {
      "ref": "Equation 20",
      "content": "\\mathcal{L}_p = \\mathcal{L}_{CE}(\\mathbf{z}^S/\tau, \\mathbf{z}^T/\tau)",
      "relevance": "Defines the logit-matching loss used in the second stage of the distillation process."
    }
  ],
  "section_refs": [
    "Section 4.2",
    "Appendix C"
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.25,
      "w": 0.35,
      "h": 0.6
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to showcase the detailed teacher-student distillation schematic (Figure 9) on the left, while summarizing the two-stage training process and loss objectives in bullets on the right. This provides a clear mapping between the visual architecture and the mathematical distillation steps within the short 7-second window."
}

Scene context:
{
  "scene_id": 4,
  "title": "Stage 1: Offline Knowledge Distillation",
  "summary": "The LSP first performs offline distillation using an auxiliary dataset. The original FM acts as a teacher to train the FHE-friendly 'student' model, ensuring the approximated blocks retain the representational power of the original foundation model.",
  "paper_section": "Two-stage Split Learning",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
  "title": "Stage 1: Offline Knowledge Distillation",
  "audio_content": "The server first distills the foundation model into an FHE-friendly student. This two-stage process matches internal features and logits to preserve accuracy before any client collaboration.",
  "bullets": [
    "Teacher-student distillation using auxiliary datasets",
    "Stage I: Distill attention and hidden states",
    "Stage II: Match logits for prediction accuracy"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 9",
    "caption": "Schematic of layer-wise knowledge distillation from teacher to student"
  },
  "source": ["Figure 9", "Section 4.2"],
  "time_cost": "7",
  "prompt": "A slide showing a schematic diagram of knowledge distillation on the left, where a teacher model transfers attention matrices and hidden representations to a student model. On the right, bullet points explain the two-stage distillation process using auxiliary data."
}"""

Token usage so far: 197632 prompt tokens, 7880 completion tokens

Cost so far: $2.21272

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Stage 1: Offline Knowledge Distillation",
  "audio_content": "The server first distills the foundation model into an FHE-friendly student. This two-stage process matches internal features and logits to preserve accuracy before any client collaboration.",
  "bullets": [
    "Teacher-student distillation using auxiliary datasets",
    "Stage I: Distill attention and hidden states",
    "Stage II: Match logits for prediction accuracy"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 9",
    "caption": "Schematic of layer-wise knowledge distillation from teacher to student"
  },
  "source": [
    "Figure 9",
    "Section 4.2"
  ],
  "time_cost": "7",
  "prompt": "A slide showing a schematic diagram of knowledge distillation on the left, where a teacher model transfers attention matrices and hidden representations to a student model. On the right, bullet points explain the two-stage distillation process using auxiliary data."
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
      "w": 0.5,
      "h": 0.7
    },
    "bullets": {
      "x": 0.6,
      "y": 0.25,
      "w": 0.35,
      "h": 0.6
    }
  },
  "has_figure": true,
  "total_time_sec": "7"
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
    "title": "Stage 1: Offline Knowledge Distillation",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 9",
      "caption": "Schematic of layer-wise knowledge distillation from teacher to student"
    },
    "bullets": [
      "Teacher-student distillation using auxiliary datasets",
      "Stage I: Distill attention and hidden states",
      "Stage II: Match logits for prediction accuracy"
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
      "audio_segment": "The server first distills the foundation model into an FHE-friendly student.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 1.75,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "This two-stage process uses auxiliary datasets for teacher-student distillation.",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 3.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "Stage one matches internal features like attention and hidden states...",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 5.25,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "...and matches logits to preserve accuracy before any client collaboration.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 208747 prompt tokens, 8431 completion tokens

Cost so far: $2.34040

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 5,
  "title": "Stage 2: Online Encrypted Inference",
  "summary": "During adaptation, clients encrypt their data and interact with the server block-by-block. Clients decrypt and re-encrypt intermediate representations to manage multiplicative depth, ensuring the server never sees the plaintext data.",
  "paper_section": "Encrypted Inference",
  "narrative_role": "methodology",
  "time_allocation_sec": 9,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
  "extracted_content": "The online adaptation stage uses an interactive protocol to handle the high multiplicative depth of Foundation Models, which exceeds the limits of current FHE schemes. Instead of evaluating the entire network at once, BlindFed performs encrypted inference one transformer block at a time. For each block, the server computes the encrypted output, which the client then decrypts and re-encrypts before returning it to the server for the next block. This process ensures that the server never accesses the client's private key or plaintext data. After the final block, the client passes decrypted representations through a local classification head, and the server computes the final batch loss entirely within the encrypted domain to facilitate local learning updates.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Illustrates the 'Online Adaptation' phase where clients interact with the FHE-enabled FM on the server."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Shows the flow of encrypted intermediate representations between the server's attention blocks and the client's parallel adapter."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Provides the specific performance metrics (time and memory) for the encrypted inference process described in this section."
    }
  ],
  "key_equations": [
    {
      "ref": "Encrypted intermediate representation",
      "content": "E(F(E(b_l)))",
      "relevance": "Describes the client-side operation of decrypting (F) and re-encrypting (E) the block output (b_l) to reset multiplicative depth."
    }
  ],
  "section_refs": [
    "Section 4.2.1"
  ]
}"""

Token usage so far: 219205 prompt tokens, 8898 completion tokens

Cost so far: $2.45899

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "The online adaptation stage uses an interactive protocol to handle the high multiplicative depth of Foundation Models, which exceeds the limits of current FHE schemes. Instead of evaluating the entire network at once, BlindFed performs encrypted inference one transformer block at a time. For each block, the server computes the encrypted output, which the client then decrypts and re-encrypts before returning it to the server for the next block. This process ensures that the server never accesses the client's private key or plaintext data. After the final block, the client passes decrypted representations through a local classification head, and the server computes the final batch loss entirely within the encrypted domain to facilitate local learning updates.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Illustrates the 'Online Adaptation' phase where clients interact with the FHE-enabled FM on the server."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Shows the flow of encrypted intermediate representations between the server's attention blocks and the client's parallel adapter."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Provides the specific performance metrics (time and memory) for the encrypted inference process described in this section."
    }
  ],
  "key_equations": [
    {
      "ref": "Encrypted intermediate representation",
      "content": "E(F(E(b_l)))",
      "relevance": "Describes the client-side operation of decrypting (F) and re-encrypting (E) the block output (b_l) to reset multiplicative depth."
    }
  ],
  "section_refs": [
    "Section 4.2.1"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 5,
  "title": "Stage 2: Online Encrypted Inference",
  "summary": "During adaptation, clients encrypt their data and interact with the server block-by-block. Clients decrypt and re-encrypt intermediate representations to manage multiplicative depth, ensuring the server never sees the plaintext data.",
  "paper_section": "Encrypted Inference",
  "narrative_role": "methodology",
  "time_allocation_sec": 9,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.75},
    "bullets": {"x": 0.55, "y": 0.2, "w": 0.4, "h": 0.75}
  },
  "has_figure": true,
  "style_rationale": "The two-column layout with the figure on the left is chosen to visually anchor the complex block-by-block encrypted inference process shown in Figure 3, while the bullets on the right summarize the key privacy-preserving steps."
}"""

Token usage so far: 230402 prompt tokens, 9120 completion tokens

Cost so far: $2.57762

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "The online adaptation stage uses an interactive protocol to handle the high multiplicative depth of Foundation Models, which exceeds the limits of current FHE schemes. Instead of evaluating the entire network at once, BlindFed performs encrypted inference one transformer block at a time. For each block, the server computes the encrypted output, which the client then decrypts and re-encrypts before returning it to the server for the next block. This process ensures that the server never accesses the client's private key or plaintext data. After the final block, the client passes decrypted representations through a local classification head, and the server computes the final batch loss entirely within the encrypted domain to facilitate local learning updates.",
  "key_figures": [
    {
      "ref": "Figure 2",
      "caption": "Overview of the proposed BlindFed framework for double-blind federated adaptation.",
      "relevance": "Illustrates the 'Online Adaptation' phase where clients interact with the FHE-enabled FM on the server."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign.",
      "relevance": "Shows the flow of encrypted intermediate representations between the server's attention blocks and the client's parallel adapter."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 7",
      "caption": "Computational and memory overhead for encrypted inference and encryption using FHE with the Tile Tensors framework.",
      "relevance": "Provides the specific performance metrics (time and memory) for the encrypted inference process described in this section."
    }
  ],
  "key_equations": [
    {
      "ref": "Encrypted intermediate representation",
      "content": "E(F(E(b_l)))",
      "relevance": "Describes the client-side operation of decrypting (F) and re-encrypting (E) the block output (b_l) to reset multiplicative depth."
    }
  ],
  "section_refs": [
    "Section 4.2.1"
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
      "w": 0.45,
      "h": 0.75
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.75
    }
  },
  "has_figure": true,
  "style_rationale": "The two-column layout with the figure on the left is chosen to visually anchor the complex block-by-block encrypted inference process shown in Figure 3, while the bullets on the right summarize the key privacy-preserving steps."
}

Scene context:
{
  "scene_id": 5,
  "title": "Stage 2: Online Encrypted Inference",
  "summary": "During adaptation, clients encrypt their data and interact with the server block-by-block. Clients decrypt and re-encrypt intermediate representations to manage multiplicative depth, ensuring the server never sees the plaintext data.",
  "paper_section": "Encrypted Inference",
  "narrative_role": "methodology",
  "time_allocation_sec": 9,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
  "title": "Stage 2: Online Encrypted Inference",
  "audio_content": "Adaptation happens block-by-block. Clients decrypt and re-encrypt intermediate outputs to reset multiplicative depth, ensuring the server never sees plaintext data while computing the final encrypted loss.",
  "bullets": [
    "Block-by-block inference manages FHE multiplicative depth",
    "Clients decrypt and re-encrypt intermediate outputs to reset noise",
    "Server computes batch loss entirely in the encrypted domain"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Interactive encrypted inference flow between server and client"
  },
  "source": ["Figure 3", "Section 4.2.1"],
  "time_cost": "9",
  "prompt": "A slide showing a technical diagram of encrypted inference. On the left, Figure 3 from the paper illustrates the flow of encrypted intermediate representations between a server's attention blocks and a client's parallel adapter. On the right, three concise bullet points explain the block-by-block processing, the client-side re-encryption to manage multiplicative depth, and the encrypted loss computation."
}"""

Token usage so far: 241636 prompt tokens, 9390 completion tokens

Cost so far: $2.69806

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Stage 2: Online Encrypted Inference",
  "audio_content": "Adaptation happens block-by-block. Clients decrypt and re-encrypt intermediate outputs to reset multiplicative depth, ensuring the server never sees plaintext data while computing the final encrypted loss.",
  "bullets": [
    "Block-by-block inference manages FHE multiplicative depth",
    "Clients decrypt and re-encrypt intermediate outputs to reset noise",
    "Server computes batch loss entirely in the encrypted domain"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 3",
    "caption": "Interactive encrypted inference flow between server and client"
  },
  "source": [
    "Figure 3",
    "Section 4.2.1"
  ],
  "time_cost": "9",
  "prompt": "A slide showing a technical diagram of encrypted inference. On the left, Figure 3 from the paper illustrates the flow of encrypted intermediate representations between a server's attention blocks and a client's parallel adapter. On the right, three concise bullet points explain the block-by-block processing, the client-side re-encryption to manage multiplicative depth, and the encrypted loss computation."
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
      "w": 0.45,
      "h": 0.75
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.75
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

"""{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Stage 2: Online Encrypted Inference",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 3",
      "caption": "Interactive encrypted inference flow between server and client"
    },
    "bullets": [
      "Block-by-block inference manages FHE multiplicative depth",
      "Clients decrypt and re-encrypt intermediate outputs to reset noise",
      "Server computes batch loss entirely in the encrypted domain"
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
      "audio_segment": "Adaptation happens block-by-block.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 2.25,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "Clients decrypt and re-encrypt intermediate outputs to reset multiplicative depth,",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 4.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "ensuring the server never sees plaintext data",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 6.75,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "while computing the final encrypted loss.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 252792 prompt tokens, 9925 completion tokens

Cost so far: $2.82567

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 6,
  "title": "Local Learning and Secure Aggregation",
  "summary": "Clients receive intermediate representations to train local low-rank parallel adapters and classification heads. These local updates are then combined using MPC-based secure aggregation to form a global adapted model.",
  "paper_section": "Local Learning",
  "narrative_role": "methodology",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "extracted_content": "BlindFed utilizes a low-rank parallel adapter method for local learning, which is essential because it does not require backpropagation through the Foundation Model (FM). Clients receive intermediate representations in plaintext after each transformer block during the encrypted inference phase, allowing them to perform local updates on their parallel adapters and classification heads. The parallel adapter design incorporates down-projection and up-projection matrices with a GELU activation and a learnable scaling factor. To maintain privacy during the global update, BlindFed employs Secure Multi-Party Computation (MPC) for secure aggregation. This allows the server to compute the average of client updates (via FedAvg) to form the global adapter and classification head without ever seeing the individual local updates from the data owners.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "Shows how the parallel adapters are structured alongside the transformer blocks and how they are updated on the client side."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign. Each transformer block’s non-linear operations – GELU activations, Softmax attention, and the division step in LayerNorm – are replaced with low-degree polynomial approximations (denoted “Quad” for GELU and “ASoftmax” for Softmax). A lightweight parallel adapter and classification head are then trained on the client side.",
      "relevance": "Visualizes the separation between the server-side FHE-friendly blocks and the client-side parallel adapter and classifier head."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 6",
      "content": "h_\\ell = g_\\ell(b_\\ell + h_{\\ell-1}) + h_{\\ell-1}",
      "relevance": "Defines the output of the low-rank parallel adapter corresponding to attention block l."
    },
    {
      "ref": "Equation 7",
      "content": "g_\\ell(z) = \\alpha W^u_\\ell \\text{GELU}(W^d_\\ell z)",
      "relevance": "Describes the adapter function using down-projection (W^d) and up-projection (W^u) matrices."
    }
  ],
  "section_refs": [
    "Section 4.2.2",
    "Section 4.2.3"
  ]
}"""

Token usage so far: 263219 prompt tokens, 10489 completion tokens

Cost so far: $2.94686

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed utilizes a low-rank parallel adapter method for local learning, which is essential because it does not require backpropagation through the Foundation Model (FM). Clients receive intermediate representations in plaintext after each transformer block during the encrypted inference phase, allowing them to perform local updates on their parallel adapters and classification heads. The parallel adapter design incorporates down-projection and up-projection matrices with a GELU activation and a learnable scaling factor. To maintain privacy during the global update, BlindFed employs Secure Multi-Party Computation (MPC) for secure aggregation. This allows the server to compute the average of client updates (via FedAvg) to form the global adapter and classification head without ever seeing the individual local updates from the data owners.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "Shows how the parallel adapters are structured alongside the transformer blocks and how they are updated on the client side."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign. Each transformer block\u2019s non-linear operations \u2013 GELU activations, Softmax attention, and the division step in LayerNorm \u2013 are replaced with low-degree polynomial approximations (denoted \u201cQuad\u201d for GELU and \u201cASoftmax\u201d for Softmax). A lightweight parallel adapter and classification head are then trained on the client side.",
      "relevance": "Visualizes the separation between the server-side FHE-friendly blocks and the client-side parallel adapter and classifier head."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 6",
      "content": "h_\\ell = g_\\ell(b_\\ell + h_{\\ell-1}) + h_{\\ell-1}",
      "relevance": "Defines the output of the low-rank parallel adapter corresponding to attention block l."
    },
    {
      "ref": "Equation 7",
      "content": "g_\\ell(z) = \u0007lpha W^u_\\ell \text{GELU}(W^d_\\ell z)",
      "relevance": "Describes the adapter function using down-projection (W^d) and up-projection (W^u) matrices."
    }
  ],
  "section_refs": [
    "Section 4.2.2",
    "Section 4.2.3"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 6,
  "title": "Local Learning and Secure Aggregation",
  "summary": "Clients receive intermediate representations to train local low-rank parallel adapters and classification heads. These local updates are then combined using MPC-based secure aggregation to form a global adapted model.",
  "paper_section": "Local Learning",
  "narrative_role": "methodology",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.15, "w": 0.45, "h": 0.8},
    "bullets": {"x": 0.55, "y": 0.2, "w": 0.4, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is best for this methodology slide. Figure 4 is a vertical diagram showing the parallel adapter structure, which pairs naturally with bulleted text explaining the local learning and secure aggregation processes."
}"""

Token usage so far: 274531 prompt tokens, 10711 completion tokens

Cost so far: $3.06664

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed utilizes a low-rank parallel adapter method for local learning, which is essential because it does not require backpropagation through the Foundation Model (FM). Clients receive intermediate representations in plaintext after each transformer block during the encrypted inference phase, allowing them to perform local updates on their parallel adapters and classification heads. The parallel adapter design incorporates down-projection and up-projection matrices with a GELU activation and a learnable scaling factor. To maintain privacy during the global update, BlindFed employs Secure Multi-Party Computation (MPC) for secure aggregation. This allows the server to compute the average of client updates (via FedAvg) to form the global adapter and classification head without ever seeing the individual local updates from the data owners.",
  "key_figures": [
    {
      "ref": "Figure 4",
      "caption": "Illustration of the parallel adapter design.",
      "relevance": "Shows how the parallel adapters are structured alongside the transformer blocks and how they are updated on the client side."
    },
    {
      "ref": "Figure 3",
      "caption": "FHE-friendly architecture redesign. Each transformer block\u2019s non-linear operations \u2013 GELU activations, Softmax attention, and the division step in LayerNorm \u2013 are replaced with low-degree polynomial approximations (denoted \u201cQuad\u201d for GELU and \u201cASoftmax\u201d for Softmax). A lightweight parallel adapter and classification head are then trained on the client side.",
      "relevance": "Visualizes the separation between the server-side FHE-friendly blocks and the client-side parallel adapter and classifier head."
    }
  ],
  "key_tables": [],
  "key_equations": [
    {
      "ref": "Equation 6",
      "content": "h_\\ell = g_\\ell(b_\\ell + h_{\\ell-1}) + h_{\\ell-1}",
      "relevance": "Defines the output of the low-rank parallel adapter corresponding to attention block l."
    },
    {
      "ref": "Equation 7",
      "content": "g_\\ell(z) = \u0007lpha W^u_\\ell \text{GELU}(W^d_\\ell z)",
      "relevance": "Describes the adapter function using down-projection (W^d) and up-projection (W^u) matrices."
    }
  ],
  "section_refs": [
    "Section 4.2.2",
    "Section 4.2.3"
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
      "y": 0.15,
      "w": 0.45,
      "h": 0.8
    },
    "bullets": {
      "x": 0.55,
      "y": 0.2,
      "w": 0.4,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with the figure on the left is best for this methodology slide. Figure 4 is a vertical diagram showing the parallel adapter structure, which pairs naturally with bulleted text explaining the local learning and secure aggregation processes."
}

Scene context:
{
  "scene_id": 6,
  "title": "Local Learning and Secure Aggregation",
  "summary": "Clients receive intermediate representations to train local low-rank parallel adapters and classification heads. These local updates are then combined using MPC-based secure aggregation to form a global adapted model.",
  "paper_section": "Local Learning",
  "narrative_role": "methodology",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "title": "Local Learning & Secure Aggregation",
  "audio_content": "Clients train local parallel adapters using intermediate representations, bypassing backpropagation through the foundation model. These local updates are then securely aggregated via MPC to update the global model.",
  "bullets": [
    "Train low-rank parallel adapters without backpropagation through the FM.",
    "Clients update local adapters using plaintext intermediate representations.",
    "MPC-based secure aggregation protects individual updates during global averaging."
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 4",
    "caption": "Structure of the low-rank parallel adapter design."
  },
  "source": [
    "Section 4.2.2",
    "Section 4.2.3",
    "Figure 4"
  ],
  "time_cost": "8",
  "prompt": "A slide showing a diagram of parallel adapters on the left and bullet points on the right. The diagram illustrates how adapters are placed alongside transformer blocks for local client-side training."
}"""

Token usage so far: 285872 prompt tokens, 10953 completion tokens

Cost so far: $3.18731

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Local Learning & Secure Aggregation",
  "audio_content": "Clients train local parallel adapters using intermediate representations, bypassing backpropagation through the foundation model. These local updates are then securely aggregated via MPC to update the global model.",
  "bullets": [
    "Train low-rank parallel adapters without backpropagation through the FM.",
    "Clients update local adapters using plaintext intermediate representations.",
    "MPC-based secure aggregation protects individual updates during global averaging."
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 4",
    "caption": "Structure of the low-rank parallel adapter design."
  },
  "source": [
    "Section 4.2.2",
    "Section 4.2.3",
    "Figure 4"
  ],
  "time_cost": "8",
  "prompt": "A slide showing a diagram of parallel adapters on the left and bullet points on the right. The diagram illustrates how adapters are placed alongside transformer blocks for local client-side training."
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
      "y": 0.15,
      "w": 0.45,
      "h": 0.8
    },
    "bullets": {
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

"""```json
{
  "style": "Slides",
  "expected_build_steps": 4,
  "elements": {
    "title": "Local Learning & Secure Aggregation",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 4",
      "caption": "Structure of the low-rank parallel adapter design."
    },
    "bullets": [
      "Train low-rank parallel adapters without backpropagation through the FM.",
      "Clients update local adapters using plaintext intermediate representations.",
      "MPC-based secure aggregation protects individual updates during global averaging."
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
      "audio_segment": "Clients train local parallel adapters",
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
      "audio_segment": "bypassing backpropagation through the foundation model",
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
      "audio_segment": "using intermediate representations.",
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
      "audio_segment": "These local updates are then securely aggregated via MPC to update the global model.",
      "visual_emphasis": []
    }
  ]
}
```"""

Token usage so far: 296991 prompt tokens, 11487 completion tokens

Cost so far: $3.31452

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 7,
  "title": "Boosting Model Privacy",
  "summary": "To prevent model extraction attacks, BlindFed introduces sample-level permutation and Stochastic Block Sampling (SBS). These techniques ensure clients cannot easily map input-output pairs of individual transformer blocks.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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

"""```json
{
  "extracted_content": "BlindFed introduces two primary mechanisms to mitigate model extraction attacks that could occur because intermediate representations are exposed in plaintext to clients during the block-by-block encrypted inference process. \n\n1. **Sample-level Permutation**: The server applies a random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations before sending them to the client. This prevents the client from linking specific input-output pairs $(b_{\\ell-1}, b_\\ell)$ for any training sample. Proposition 1 establishes that even if relative permutations between blocks are revealed to facilitate adapter computation, uniquely recovering the individual permutation matrices is computationally infeasible (requiring $n!$ trials).\n\n2. **Stochastic Block Sampling (SBS)**: To counter attacks that exploit feature similarity between consecutive blocks, the server returns only a subset of block outputs in each forward pass. SBS follows a structured rule: if block $\\ell$ is sampled, block $\\ell+1$ is deterministically skipped. This ensures that any two representations seen by the client are separated by at least one layer, which significantly reduces feature similarity and breaks the diagonal alignment required for similarity-based extraction attacks. Empirical results in Table 1 show that adding SBS provides these privacy gains with minimal impact on the final model accuracy.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the structured sampling process (state transition) used to ensure that consecutive transformer blocks are never exposed to the client simultaneously."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations: (i) between block outputs b1 and b3, and (ii) between block outputs b9 and b12.",
      "relevance": "Provides visual evidence that the similarity-based attack vector is neutralized when blocks are separated by at least one layer, as the diagonal similarity pattern disappears."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN)...",
      "relevance": "Shows the performance of the 'BlindFed + SBS' variant, demonstrating that the privacy-boosting sampling technique does not significantly degrade accuracy."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "H_\\ell = g_\\ell(B_\\ell + H_{\\ell-1}) + H_{\\ell-1}",
      "relevance": "The reformulated adapter output equation that allows the client to perform local updates correctly even when the input batches are permuted."
    },
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n × n permutation matrices. Given only A^−1B, B^−1C, and C^−1A, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the theoretical security guarantee for the sample-level permutation defense."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2"
  ]
}
```"""

Token usage so far: 307424 prompt tokens, 12278 completion tokens

Cost so far: $3.44258

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

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE)
affiliation_2_logo: affiliation_2.png (Michigan State University (MSU), USA)

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
    "conference_logo": {
      "x": 0.8,
      "y": 0.05,
      "w": 0.15,
      "h": 0.1
    },
    "affiliation_logos": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.35,
      "h": 0.1
    },
    "title": {
      "x": 0.05,
      "y": 0.25,
      "w": 0.9,
      "h": 0.2
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.08
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.6,
      "w": 0.8,
      "h": 0.12
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.06
    }
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum impact, followed by a clear hierarchy for authors and their respective institutional details. The venue is placed at the bottom to anchor the design."
}"""

Token usage so far: 10707 prompt tokens, 417 completion tokens

Cost so far: $0.11958

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 7,
  "title": "Boosting Model Privacy",
  "summary": "To prevent model extraction attacks, BlindFed introduces sample-level permutation and Stochastic Block Sampling (SBS). These techniques ensure clients cannot easily map input-output pairs of individual transformer blocks.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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

"""```json
{
  "extracted_content": "BlindFed introduces two primary mechanisms to mitigate model extraction attacks that could occur because intermediate representations are exposed in plaintext to clients during the block-by-block encrypted inference process. \n\n1. **Sample-level Permutation**: The server applies a random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations before sending them to the client. This prevents the client from linking specific input-output pairs $(b_{\\ell-1}, b_\\ell)$ for any training sample. Proposition 1 establishes that even if relative permutations between blocks are revealed to facilitate adapter computation, uniquely recovering the individual permutation matrices is computationally infeasible (requiring $n!$ trials).\n\n2. **Stochastic Block Sampling (SBS)**: To counter attacks that exploit feature similarity between consecutive blocks, the server returns only a subset of block outputs in each forward pass. SBS follows a structured rule: if block $\\ell$ is sampled, block $\\ell+1$ is deterministically skipped. This ensures that any two representations seen by the client are separated by at least one layer, which significantly reduces feature similarity and breaks the diagonal alignment required for similarity-based extraction attacks. Empirical results in Table 1 show that adding SBS provides these privacy gains with minimal impact on the final model accuracy.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the structured sampling process (state transition) used to ensure that consecutive transformer blocks are never exposed to the client simultaneously."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations: (i) between block outputs b1 and b3, and (ii) between block outputs b9 and b12.",
      "relevance": "Provides visual evidence that the similarity-based attack vector is neutralized when blocks are separated by at least one layer, as the diagonal similarity pattern disappears."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN)...",
      "relevance": "Shows the performance of the 'BlindFed + SBS' variant, demonstrating that the privacy-boosting sampling technique does not significantly degrade accuracy."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "H_\\ell = g_\\ell(B_\\ell + H_{\\ell-1}) + H_{\\ell-1}",
      "relevance": "The reformulated adapter output equation that allows the client to perform local updates correctly even when the input batches are permuted."
    },
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n × n permutation matrices. Given only A^−1B, B^−1C, and C^−1A, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the theoretical security guarantee for the sample-level permutation defense."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2"
  ]
}
```"""

Token usage so far: 21140 prompt tokens, 1208 completion tokens

Cost so far: $0.24764

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

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE)
affiliation_2_logo: affiliation_2.png (Michigan State University (MSU), USA)

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
    "conference_logo": {
      "x": 0.8,
      "y": 0.05,
      "w": 0.15,
      "h": 0.1
    },
    "affiliation_logos": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.35,
      "h": 0.1
    },
    "title": {
      "x": 0.05,
      "y": 0.25,
      "w": 0.9,
      "h": 0.2
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.08
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.6,
      "w": 0.8,
      "h": 0.12
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.06
    }
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum impact, followed by a clear hierarchy for authors and their respective institutional details. The venue is placed at the bottom to anchor the design."
}"""

Token usage so far: 10707 prompt tokens, 417 completion tokens

Cost so far: $0.11958

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 7,
  "title": "Boosting Model Privacy",
  "summary": "To prevent model extraction attacks, BlindFed introduces sample-level permutation and Stochastic Block Sampling (SBS). These techniques ensure clients cannot easily map input-output pairs of individual transformer blocks.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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

"""```json
{
  "extracted_content": "BlindFed introduces two primary mechanisms to mitigate model extraction attacks that could occur because intermediate representations are exposed in plaintext to clients during the block-by-block encrypted inference process. \n\n1. **Sample-level Permutation**: The server applies a random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations before sending them to the client. This prevents the client from linking specific input-output pairs $(b_{\\ell-1}, b_\\ell)$ for any training sample. Proposition 1 establishes that even if relative permutations between blocks are revealed to facilitate adapter computation, uniquely recovering the individual permutation matrices is computationally infeasible (requiring $n!$ trials).\n\n2. **Stochastic Block Sampling (SBS)**: To counter attacks that exploit feature similarity between consecutive blocks, the server returns only a subset of block outputs in each forward pass. SBS follows a structured rule: if block $\\ell$ is sampled, block $\\ell+1$ is deterministically skipped. This ensures that any two representations seen by the client are separated by at least one layer, which significantly reduces feature similarity and breaks the diagonal alignment required for similarity-based extraction attacks. Empirical results in Table 1 show that adding SBS provides these privacy gains with minimal impact on the final model accuracy.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the structured sampling process (state transition) used to ensure that consecutive transformer blocks are never exposed to the client simultaneously."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations: (i) between block outputs b1 and b3, and (ii) between block outputs b9 and b12.",
      "relevance": "Provides visual evidence that the similarity-based attack vector is neutralized when blocks are separated by at least one layer, as the diagonal similarity pattern disappears."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN)...",
      "relevance": "Shows the performance of the 'BlindFed + SBS' variant, demonstrating that the privacy-boosting sampling technique does not significantly degrade accuracy."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "H_\\ell = g_\\ell(B_\\ell + H_{\\ell-1}) + H_{\\ell-1}",
      "relevance": "The reformulated adapter output equation that allows the client to perform local updates correctly even when the input batches are permuted."
    },
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n × n permutation matrices. Given only A^−1B, B^−1C, and C^−1A, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the theoretical security guarantee for the sample-level permutation defense."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2"
  ]
}
```"""

Token usage so far: 21140 prompt tokens, 1208 completion tokens

Cost so far: $0.24764

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

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE)
affiliation_2_logo: affiliation_2.png (Michigan State University (MSU), USA)

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
    "conference_logo": {
      "x": 0.8,
      "y": 0.05,
      "w": 0.15,
      "h": 0.1
    },
    "affiliation_logos": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.35,
      "h": 0.1
    },
    "title": {
      "x": 0.05,
      "y": 0.25,
      "w": 0.9,
      "h": 0.2
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.08
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.6,
      "w": 0.8,
      "h": 0.12
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.06
    }
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum impact, followed by a clear hierarchy for authors and their respective institutional details. The venue is placed at the bottom to anchor the design."
}"""

Token usage so far: 10707 prompt tokens, 417 completion tokens

Cost so far: $0.11958

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 7,
  "title": "Boosting Model Privacy",
  "summary": "To prevent model extraction attacks, BlindFed introduces sample-level permutation and Stochastic Block Sampling (SBS). These techniques ensure clients cannot easily map input-output pairs of individual transformer blocks.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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

"""```json
{
  "extracted_content": "BlindFed introduces two primary mechanisms to mitigate model extraction attacks that could occur because intermediate representations are exposed in plaintext to clients during the block-by-block encrypted inference process. \n\n1. **Sample-level Permutation**: The server applies a random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations before sending them to the client. This prevents the client from linking specific input-output pairs $(b_{\\ell-1}, b_\\ell)$ for any training sample. Proposition 1 establishes that even if relative permutations between blocks are revealed to facilitate adapter computation, uniquely recovering the individual permutation matrices is computationally infeasible (requiring $n!$ trials).\n\n2. **Stochastic Block Sampling (SBS)**: To counter attacks that exploit feature similarity between consecutive blocks, the server returns only a subset of block outputs in each forward pass. SBS follows a structured rule: if block $\\ell$ is sampled, block $\\ell+1$ is deterministically skipped. This ensures that any two representations seen by the client are separated by at least one layer, which significantly reduces feature similarity and breaks the diagonal alignment required for similarity-based extraction attacks. Empirical results in Table 1 show that adding SBS provides these privacy gains with minimal impact on the final model accuracy.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the structured sampling process (state transition) used to ensure that consecutive transformer blocks are never exposed to the client simultaneously."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations: (i) between block outputs b1 and b3, and (ii) between block outputs b9 and b12.",
      "relevance": "Provides visual evidence that the similarity-based attack vector is neutralized when blocks are separated by at least one layer, as the diagonal similarity pattern disappears."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN)...",
      "relevance": "Shows the performance of the 'BlindFed + SBS' variant, demonstrating that the privacy-boosting sampling technique does not significantly degrade accuracy."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "H_\\ell = g_\\ell(B_\\ell + H_{\\ell-1}) + H_{\\ell-1}",
      "relevance": "The reformulated adapter output equation that allows the client to perform local updates correctly even when the input batches are permuted."
    },
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n × n permutation matrices. Given only A^−1B, B^−1C, and C^−1A, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the theoretical security guarantee for the sample-level permutation defense."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2"
  ]
}
```"""

Token usage so far: 21140 prompt tokens, 1208 completion tokens

Cost so far: $0.24764

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed introduces two primary mechanisms to mitigate model extraction attacks that could occur because intermediate representations are exposed in plaintext to clients during the block-by-block encrypted inference process. \n\n1. **Sample-level Permutation**: The server applies a random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations before sending them to the client. This prevents the client from linking specific input-output pairs $(b_{\\ell-1}, b_\\ell)$ for any training sample. Proposition 1 establishes that even if relative permutations between blocks are revealed to facilitate adapter computation, uniquely recovering the individual permutation matrices is computationally infeasible (requiring $n!$ trials).\n\n2. **Stochastic Block Sampling (SBS)**: To counter attacks that exploit feature similarity between consecutive blocks, the server returns only a subset of block outputs in each forward pass. SBS follows a structured rule: if block $\\ell$ is sampled, block $\\ell+1$ is deterministically skipped. This ensures that any two representations seen by the client are separated by at least one layer, which significantly reduces feature similarity and breaks the diagonal alignment required for similarity-based extraction attacks. Empirical results in Table 1 show that adding SBS provides these privacy gains with minimal impact on the final model accuracy.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the structured sampling process (state transition) used to ensure that consecutive transformer blocks are never exposed to the client simultaneously."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations: (i) between block outputs b1 and b3, and (ii) between block outputs b9 and b12.",
      "relevance": "Provides visual evidence that the similarity-based attack vector is neutralized when blocks are separated by at least one layer, as the diagonal similarity pattern disappears."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN)...",
      "relevance": "Shows the performance of the 'BlindFed + SBS' variant, demonstrating that the privacy-boosting sampling technique does not significantly degrade accuracy."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "H_\\ell = g_\\ell(B_\\ell + H_{\\ell-1}) + H_{\\ell-1}",
      "relevance": "The reformulated adapter output equation that allows the client to perform local updates correctly even when the input batches are permuted."
    },
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n \u00d7 n permutation matrices. Given only A^\u22121B, B^\u22121C, and C^\u22121A, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the theoretical security guarantee for the sample-level permutation defense."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 7,
  "title": "Boosting Model Privacy",
  "summary": "To prevent model extraction attacks, BlindFed introduces sample-level permutation and Stochastic Block Sampling (SBS). These techniques ensure clients cannot easily map input-output pairs of individual transformer blocks.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
  "layout_template": "two_col_fig_left",
  "background_color": "#FFFFFF",
  "layout_regions": {
    "title": {"x": 0.05, "y": 0.05, "w": 0.9, "h": 0.1},
    "figure": {"x": 0.05, "y": 0.2, "w": 0.45, "h": 0.7},
    "bullets": {"x": 0.55, "y": 0.2, "w": 0.4, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "A two-column layout is chosen to present the conceptual state-transition diagram of Stochastic Block Sampling (Figure 5) on the left, providing a visual anchor for the two primary privacy-boosting techniques described in the bullets on the right. This layout is efficient for the short 7-second time allocation."
}"""

Token usage so far: 32656 prompt tokens, 1444 completion tokens

Cost so far: $0.36988

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed introduces two primary mechanisms to mitigate model extraction attacks that could occur because intermediate representations are exposed in plaintext to clients during the block-by-block encrypted inference process. \n\n1. **Sample-level Permutation**: The server applies a random permutation matrix $\\Pi_\\ell$ to each batch of intermediate representations before sending them to the client. This prevents the client from linking specific input-output pairs $(b_{\\ell-1}, b_\\ell)$ for any training sample. Proposition 1 establishes that even if relative permutations between blocks are revealed to facilitate adapter computation, uniquely recovering the individual permutation matrices is computationally infeasible (requiring $n!$ trials).\n\n2. **Stochastic Block Sampling (SBS)**: To counter attacks that exploit feature similarity between consecutive blocks, the server returns only a subset of block outputs in each forward pass. SBS follows a structured rule: if block $\\ell$ is sampled, block $\\ell+1$ is deterministically skipped. This ensures that any two representations seen by the client are separated by at least one layer, which significantly reduces feature similarity and breaks the diagonal alignment required for similarity-based extraction attacks. Empirical results in Table 1 show that adding SBS provides these privacy gains with minimal impact on the final model accuracy.",
  "key_figures": [
    {
      "ref": "Figure 5",
      "caption": "Stochastic block sampling strategy.",
      "relevance": "Illustrates the structured sampling process (state transition) used to ensure that consecutive transformer blocks are never exposed to the client simultaneously."
    },
    {
      "ref": "Figure 7",
      "caption": "Heatmap visualization of the similarity (L2 distance) between non-consecutive block outputs or hidden representations: (i) between block outputs b1 and b3, and (ii) between block outputs b9 and b12.",
      "relevance": "Provides visual evidence that the similarity-based attack vector is neutralized when blocks are separated by at least one layer, as the diagonal similarity pattern disappears."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN)...",
      "relevance": "Shows the performance of the 'BlindFed + SBS' variant, demonstrating that the privacy-boosting sampling technique does not significantly degrade accuracy."
    }
  ],
  "key_equations": [
    {
      "ref": "Equation 8",
      "content": "H_\\ell = g_\\ell(B_\\ell + H_{\\ell-1}) + H_{\\ell-1}",
      "relevance": "The reformulated adapter output equation that allows the client to perform local updates correctly even when the input batches are permuted."
    },
    {
      "ref": "Proposition 1",
      "content": "Let A, B, and C be n \u00d7 n permutation matrices. Given only A^\u22121B, B^\u22121C, and C^\u22121A, it is computationally infeasible to uniquely recover the individual matrices A, B, and C without additional information.",
      "relevance": "Provides the theoretical security guarantee for the sample-level permutation defense."
    }
  ],
  "section_refs": [
    "Section 4.3",
    "Section 4.3.1",
    "Section 4.3.2"
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
      "w": 0.45,
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
  "style_rationale": "A two-column layout is chosen to present the conceptual state-transition diagram of Stochastic Block Sampling (Figure 5) on the left, providing a visual anchor for the two primary privacy-boosting techniques described in the bullets on the right. This layout is efficient for the short 7-second time allocation."
}

Scene context:
{
  "scene_id": 7,
  "title": "Boosting Model Privacy",
  "summary": "To prevent model extraction attacks, BlindFed introduces sample-level permutation and Stochastic Block Sampling (SBS). These techniques ensure clients cannot easily map input-output pairs of individual transformer blocks.",
  "paper_section": "Model Privacy Boosting",
  "narrative_role": "methodology",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "NeurIPS-2024-Dual-Prototype-Evolving-for_Media"
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
  "title": "Boosting Model Privacy",
  "audio_content": "To prevent model extraction, BlindFed uses sample-level permutations and stochastic block sampling, ensuring layer-wise privacy with minimal impact on accuracy.",
  "bullets": [
    "**Sample-level Permutation** shuffles batches to hide block-specific input-output mappings.",
    "**Stochastic Block Sampling (SBS)** skips layers to neutralize similarity-based extraction attacks.",
    "**Proposition 1** guarantees that recovering individual permutations is computationally infeasible."
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Stochastic block sampling (SBS) state transition strategy"
  },
  "source": ["Section 4.3", "Figure 5", "Proposition 1"],
  "time_cost": "7",
  "prompt": "A slide showing Figure 5 (the SBS state transition diagram) on the left. On the right, three bullet points explain how sample-level permutation and stochastic block sampling protect the model from extraction attacks, referencing the theoretical guarantee of Proposition 1."
}"""

Token usage so far: 44215 prompt tokens, 1698 completion tokens

Cost so far: $0.49309

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Boosting Model Privacy",
  "audio_content": "To prevent model extraction, BlindFed uses sample-level permutations and stochastic block sampling, ensuring layer-wise privacy with minimal impact on accuracy.",
  "bullets": [
    "**Sample-level Permutation** shuffles batches to hide block-specific input-output mappings.",
    "**Stochastic Block Sampling (SBS)** skips layers to neutralize similarity-based extraction attacks.",
    "**Proposition 1** guarantees that recovering individual permutations is computationally infeasible."
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 5",
    "caption": "Stochastic block sampling (SBS) state transition strategy"
  },
  "source": [
    "Section 4.3",
    "Figure 5",
    "Proposition 1"
  ],
  "time_cost": "7",
  "prompt": "A slide showing Figure 5 (the SBS state transition diagram) on the left. On the right, three bullet points explain how sample-level permutation and stochastic block sampling protect the model from extraction attacks, referencing the theoretical guarantee of Proposition 1."
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
      "w": 0.45,
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
  "total_time_sec": "7"
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
    "title": "Boosting Model Privacy",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 5",
      "caption": "Stochastic block sampling (SBS) state transition strategy"
    },
    "bullets": [
      "**Sample-level Permutation** shuffles batches to hide block-specific input-output mappings.",
      "**Stochastic Block Sampling (SBS)** skips layers to neutralize similarity-based extraction attacks.",
      "**Proposition 1** guarantees that recovering individual permutations is computationally infeasible."
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
      "audio_segment": "To prevent model extraction,",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 1.75,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "BlindFed uses sample-level permutations",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 3.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "and stochastic block sampling,",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 5.25,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "ensuring layer-wise privacy with minimal impact on accuracy.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 55355 prompt tokens, 2241 completion tokens

Cost so far: $0.62078

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 8,
  "title": "Empirical Performance Results",
  "summary": "Experiments on CIFAR-10, CIFAR-100, and SVHN show that BlindFed achieves accuracy comparable to LoRA and full fine-tuning, significantly outperforming standard linear probing while maintaining strict double-blind privacy.",
  "paper_section": "Experiments and Results",
  "narrative_role": "result",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
  "extracted_content": "BlindFed's empirical evaluation across CIFAR-10, CIFAR-100, and SVHN demonstrates that it achieves accuracy closely matching full fine-tuning and LoRA while strictly adhering to double-blind privacy constraints. In centralized settings, BlindFed reaches 94.28% accuracy on CIFAR-10 and 92.32% on SVHN, significantly outperforming linear probing (92.26% and 59.38% respectively). In federated scenarios with varying data heterogeneity (Dirichlet alpha = 100 to 0.01), BlindFed maintains robust performance, often outperforming LoRA in highly heterogeneous cases (alpha=0.01). The addition of Stochastic Block Sampling (SBS) for enhanced privacy has a negligible impact on accuracy, and in some instances, slightly improves generalization. Scalability results on CIFAR-10 show that BlindFed remains effective as the number of clients increases from 10 to 50, consistently outperforming linear probing. Efficiency metrics reveal that BlindFed operates with a latency only ~4% higher than linear probing while requiring significantly less GPU memory than full fine-tuning or LoRA.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visualizes the trade-off between performance and efficiency, showing BlindFed's near-optimal latency and low memory footprint."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN) in both centralized and federated learning scenarios.",
      "relevance": "Provides the core accuracy results proving BlindFed is comparable to non-private baselines like LoRA and superior to linear probing."
    },
    {
      "ref": "Table 2",
      "caption": "Performance comparison of our method with baseline approaches on the Fed-ISIC2019 dataset with five clients (K = 5), using two auxiliary datasets: Fed-ISIC2019 (center=0) as an in-distribution (InD) dataset and Tiny-ImageNet as an out-of-distribution (OOD) dataset.",
      "relevance": "Shows the framework's effectiveness on medical imaging tasks and its robustness to different auxiliary datasets used during distillation."
    },
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K ∈ {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Demonstrates that BlindFed scales effectively to a larger number of clients without significant performance degradation."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Section D.2"
  ]
}"""

Token usage so far: 65816 prompt tokens, 2980 completion tokens

Cost so far: $0.74756

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed's empirical evaluation across CIFAR-10, CIFAR-100, and SVHN demonstrates that it achieves accuracy closely matching full fine-tuning and LoRA while strictly adhering to double-blind privacy constraints. In centralized settings, BlindFed reaches 94.28% accuracy on CIFAR-10 and 92.32% on SVHN, significantly outperforming linear probing (92.26% and 59.38% respectively). In federated scenarios with varying data heterogeneity (Dirichlet alpha = 100 to 0.01), BlindFed maintains robust performance, often outperforming LoRA in highly heterogeneous cases (alpha=0.01). The addition of Stochastic Block Sampling (SBS) for enhanced privacy has a negligible impact on accuracy, and in some instances, slightly improves generalization. Scalability results on CIFAR-10 show that BlindFed remains effective as the number of clients increases from 10 to 50, consistently outperforming linear probing. Efficiency metrics reveal that BlindFed operates with a latency only ~4% higher than linear probing while requiring significantly less GPU memory than full fine-tuning or LoRA.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visualizes the trade-off between performance and efficiency, showing BlindFed's near-optimal latency and low memory footprint."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN) in both centralized and federated learning scenarios.",
      "relevance": "Provides the core accuracy results proving BlindFed is comparable to non-private baselines like LoRA and superior to linear probing."
    },
    {
      "ref": "Table 2",
      "caption": "Performance comparison of our method with baseline approaches on the Fed-ISIC2019 dataset with five clients (K = 5), using two auxiliary datasets: Fed-ISIC2019 (center=0) as an in-distribution (InD) dataset and Tiny-ImageNet as an out-of-distribution (OOD) dataset.",
      "relevance": "Shows the framework's effectiveness on medical imaging tasks and its robustness to different auxiliary datasets used during distillation."
    },
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K \u2208 {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Demonstrates that BlindFed scales effectively to a larger number of clients without significant performance degradation."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Section D.2"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 8,
  "title": "Empirical Performance Results",
  "summary": "Experiments on CIFAR-10, CIFAR-100, and SVHN show that BlindFed achieves accuracy comparable to LoRA and full fine-tuning, significantly outperforming standard linear probing while maintaining strict double-blind privacy.",
  "paper_section": "Experiments and Results",
  "narrative_role": "result",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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

"""```json
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
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "style_rationale": "The 'full_fig_with_callouts' layout is ideal for presenting Table 1, which contains the core accuracy results. Given the table's width (comparing centralized and multiple federated scenarios), a full-width figure region ensures maximum legibility, while the bullets below provide a concise summary of accuracy, robustness, and efficiency."
}
```"""

Token usage so far: 77306 prompt tokens, 3264 completion tokens

Cost so far: $0.87098

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed's empirical evaluation across CIFAR-10, CIFAR-100, and SVHN demonstrates that it achieves accuracy closely matching full fine-tuning and LoRA while strictly adhering to double-blind privacy constraints. In centralized settings, BlindFed reaches 94.28% accuracy on CIFAR-10 and 92.32% on SVHN, significantly outperforming linear probing (92.26% and 59.38% respectively). In federated scenarios with varying data heterogeneity (Dirichlet alpha = 100 to 0.01), BlindFed maintains robust performance, often outperforming LoRA in highly heterogeneous cases (alpha=0.01). The addition of Stochastic Block Sampling (SBS) for enhanced privacy has a negligible impact on accuracy, and in some instances, slightly improves generalization. Scalability results on CIFAR-10 show that BlindFed remains effective as the number of clients increases from 10 to 50, consistently outperforming linear probing. Efficiency metrics reveal that BlindFed operates with a latency only ~4% higher than linear probing while requiring significantly less GPU memory than full fine-tuning or LoRA.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visualizes the trade-off between performance and efficiency, showing BlindFed's near-optimal latency and low memory footprint."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 1",
      "caption": "Comparison of accuracy achieved by our proposed method against baseline approaches on three datasets (CIFAR-10, CIFAR-100, and SVHN) in both centralized and federated learning scenarios.",
      "relevance": "Provides the core accuracy results proving BlindFed is comparable to non-private baselines like LoRA and superior to linear probing."
    },
    {
      "ref": "Table 2",
      "caption": "Performance comparison of our method with baseline approaches on the Fed-ISIC2019 dataset with five clients (K = 5), using two auxiliary datasets: Fed-ISIC2019 (center=0) as an in-distribution (InD) dataset and Tiny-ImageNet as an out-of-distribution (OOD) dataset.",
      "relevance": "Shows the framework's effectiveness on medical imaging tasks and its robustness to different auxiliary datasets used during distillation."
    },
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K \u2208 {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Demonstrates that BlindFed scales effectively to a larger number of clients without significant performance degradation."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Section D.2"
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
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
    }
  },
  "has_figure": true,
  "style_rationale": "The 'full_fig_with_callouts' layout is ideal for presenting Table 1, which contains the core accuracy results. Given the table's width (comparing centralized and multiple federated scenarios), a full-width figure region ensures maximum legibility, while the bullets below provide a concise summary of accuracy, robustness, and efficiency."
}

Scene context:
{
  "scene_id": 8,
  "title": "Empirical Performance Results",
  "summary": "Experiments on CIFAR-10, CIFAR-100, and SVHN show that BlindFed achieves accuracy comparable to LoRA and full fine-tuning, significantly outperforming standard linear probing while maintaining strict double-blind privacy.",
  "paper_section": "Experiments and Results",
  "narrative_role": "result",
  "time_allocation_sec": 8,
  "reference_style_examples": [
    "Deng_Pos3R_6D_Pose_Estimation_for_Unseen_Objects_Made_Easy_CVPR_2025_paper"
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
  "title": "High Accuracy with Double-Blind Privacy",
  "audio_content": "BlindFed matches LoRA's accuracy and outperforms linear probing, remaining robust across heterogeneous data while strictly maintaining double-blind privacy.",
  "bullets": [
    "Matches LoRA accuracy across CIFAR and SVHN datasets",
    "Significantly outperforms linear probing in federated settings",
    "Maintains robust performance under high data heterogeneity"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Table 1",
    "caption": "Accuracy comparison of BlindFed against baselines in centralized and federated scenarios."
  },
  "source": ["Table 1", "Section 5.3"],
  "time_cost": "8",
  "prompt": "A high-resolution table showing accuracy results for CIFAR-10, CIFAR-100, and SVHN, comparing BlindFed to full fine-tuning, LoRA, and linear probing across different Dirichlet alpha values."
}"""

Token usage so far: 88844 prompt tokens, 3494 completion tokens

Cost so far: $0.99326

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "High Accuracy with Double-Blind Privacy",
  "audio_content": "BlindFed matches LoRA's accuracy and outperforms linear probing, remaining robust across heterogeneous data while strictly maintaining double-blind privacy.",
  "bullets": [
    "Matches LoRA accuracy across CIFAR and SVHN datasets",
    "Significantly outperforms linear probing in federated settings",
    "Maintains robust performance under high data heterogeneity"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Table 1",
    "caption": "Accuracy comparison of BlindFed against baselines in centralized and federated scenarios."
  },
  "source": [
    "Table 1",
    "Section 5.3"
  ],
  "time_cost": "8",
  "prompt": "A high-resolution table showing accuracy results for CIFAR-10, CIFAR-100, and SVHN, comparing BlindFed to full fine-tuning, LoRA, and linear probing across different Dirichlet alpha values."
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
      "h": 0.55
    },
    "bullets": {
      "x": 0.05,
      "y": 0.75,
      "w": 0.9,
      "h": 0.2
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
    "title": "High Accuracy with Double-Blind Privacy",
    "figure": {
      "type": "paper_figure",
      "ref": "Table 1",
      "caption": "Accuracy comparison of BlindFed against baselines in centralized and federated scenarios."
    },
    "bullets": [
      "Matches LoRA accuracy across CIFAR and SVHN datasets",
      "Significantly outperforms linear probing in federated settings",
      "Maintains robust performance under high data heterogeneity"
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
      "audio_segment": "BlindFed",
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
      "audio_segment": "matches LoRA's accuracy",
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
      "audio_segment": "and outperforms linear probing,",
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
      "audio_segment": "remaining robust across heterogeneous data while strictly maintaining double-blind privacy.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 99961 prompt tokens, 4019 completion tokens

Cost so far: $1.12018

**Question**


You are an expert at reading academic papers and extracting key content for presentation slides.

Given the following high-level scene description:
{
  "scene_id": 9,
  "title": "Efficiency and Scalability",
  "summary": "While FHE introduces computational overhead, BlindFed remains efficient in terms of trainable parameters and GPU memory. It demonstrates scalability across varying numbers of clients and heterogeneous data distributions.",
  "paper_section": "Conclusions",
  "narrative_role": "conclusion",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "extracted_content": "BlindFed demonstrates strong efficiency and scalability for federated adaptation of foundation models. It achieves a favorable balance between performance and resource usage, requiring significantly fewer trainable parameters than full fine-tuning and maintaining a memory footprint comparable to linear probing. In empirical tests, BlindFed's latency was only 4% higher than linear probing in the CIFAR-10/SVHN setting. Scalability was verified with up to 50 clients, where BlindFed consistently outperformed linear probing across varying levels of data heterogeneity (Dirichlet alpha from 100 to 0.01). While the use of Fully Homomorphic Encryption (FHE) introduces a high communication cost (e.g., 17.33 MB per encrypted intermediate representation) and computational complexity for the server, the framework remains feasible for thin clients and practical for adapting large models with limited local data.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visually demonstrates that BlindFed maintains low parameter counts, latency, and memory usage compared to other fine-tuning methods."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K ∈ {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Shows the performance of BlindFed as the number of clients increases, proving its scalability."
    },
    {
      "ref": "Table 4",
      "caption": "Comparison of the efficiency of our method with baseline approaches in terms of the number of parameters, latency and the memory requirement across four datasets (CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019).",
      "relevance": "Provides the specific metrics for parameter count, latency, and GPU memory that support the efficiency claims."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Scalability Results",
    "Communication Overhead",
    "Section 6",
    "Appendix D.2"
  ]
}"""

Token usage so far: 110382 prompt tokens, 4589 completion tokens

Cost so far: $1.24149

**Question**


You are an expert presentation designer for academic video summaries.

Given the following content summary extracted from a paper:
{
  "extracted_content": "BlindFed demonstrates strong efficiency and scalability for federated adaptation of foundation models. It achieves a favorable balance between performance and resource usage, requiring significantly fewer trainable parameters than full fine-tuning and maintaining a memory footprint comparable to linear probing. In empirical tests, BlindFed's latency was only 4% higher than linear probing in the CIFAR-10/SVHN setting. Scalability was verified with up to 50 clients, where BlindFed consistently outperformed linear probing across varying levels of data heterogeneity (Dirichlet alpha from 100 to 0.01). While the use of Fully Homomorphic Encryption (FHE) introduces a high communication cost (e.g., 17.33 MB per encrypted intermediate representation) and computational complexity for the server, the framework remains feasible for thin clients and practical for adapting large models with limited local data.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visually demonstrates that BlindFed maintains low parameter counts, latency, and memory usage compared to other fine-tuning methods."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K \u2208 {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Shows the performance of BlindFed as the number of clients increases, proving its scalability."
    },
    {
      "ref": "Table 4",
      "caption": "Comparison of the efficiency of our method with baseline approaches in terms of the number of parameters, latency and the memory requirement across four datasets (CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019).",
      "relevance": "Provides the specific metrics for parameter count, latency, and GPU memory that support the efficiency claims."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Scalability Results",
    "Communication Overhead",
    "Section 6",
    "Appendix D.2"
  ]
}

Scene context from high-level plan:
{
  "scene_id": 9,
  "title": "Efficiency and Scalability",
  "summary": "While FHE introduces computational overhead, BlindFed remains efficient in terms of trainable parameters and GPU memory. It demonstrates scalability across varying numbers of clients and heterogeneous data distributions.",
  "paper_section": "Conclusions",
  "narrative_role": "conclusion",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
    "bullets": {"x": 0.05, "y": 0.2, "w": 0.4, "h": 0.7},
    "figure": {"x": 0.5, "y": 0.2, "w": 0.45, "h": 0.7}
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with bullets on the left and Figure 10 on the right is ideal for this conclusion scene. It allows for a concise summary of the efficiency and scalability results while providing immediate visual evidence of the low parameter count and latency compared to other fine-tuning methods."
}"""

Token usage so far: 121660 prompt tokens, 4819 completion tokens

Cost so far: $1.36117

**Question**


You are an expert at writing concise, impactful presentation content for academic video summaries.

Given the following content extracted from the paper:
{
  "extracted_content": "BlindFed demonstrates strong efficiency and scalability for federated adaptation of foundation models. It achieves a favorable balance between performance and resource usage, requiring significantly fewer trainable parameters than full fine-tuning and maintaining a memory footprint comparable to linear probing. In empirical tests, BlindFed's latency was only 4% higher than linear probing in the CIFAR-10/SVHN setting. Scalability was verified with up to 50 clients, where BlindFed consistently outperformed linear probing across varying levels of data heterogeneity (Dirichlet alpha from 100 to 0.01). While the use of Fully Homomorphic Encryption (FHE) introduces a high communication cost (e.g., 17.33 MB per encrypted intermediate representation) and computational complexity for the server, the framework remains feasible for thin clients and practical for adapting large models with limited local data.",
  "key_figures": [
    {
      "ref": "Figure 10",
      "caption": "Comparison of the efficiency of different adaptation methods in terms of the number of parameters, latency, and memory usage across three datasets: CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019.",
      "relevance": "Visually demonstrates that BlindFed maintains low parameter counts, latency, and memory usage compared to other fine-tuning methods."
    }
  ],
  "key_tables": [
    {
      "ref": "Table 3",
      "caption": "Scalability analysis of the proposed method to baseline approaches on the CIFAR-10 dataset, with varying number of clients K \u2208 {10, 20, 50} under a Dirichlet concentration parameter of 1.0 for data partitioning.",
      "relevance": "Shows the performance of BlindFed as the number of clients increases, proving its scalability."
    },
    {
      "ref": "Table 4",
      "caption": "Comparison of the efficiency of our method with baseline approaches in terms of the number of parameters, latency and the memory requirement across four datasets (CIFAR-10/SVHN, CIFAR-100, and Fed-ISIC2019).",
      "relevance": "Provides the specific metrics for parameter count, latency, and GPU memory that support the efficiency claims."
    }
  ],
  "key_equations": [],
  "section_refs": [
    "Section 5.3",
    "Scalability Results",
    "Communication Overhead",
    "Section 6",
    "Appendix D.2"
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
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "style_rationale": "A two-column layout with bullets on the left and Figure 10 on the right is ideal for this conclusion scene. It allows for a concise summary of the efficiency and scalability results while providing immediate visual evidence of the low parameter count and latency compared to other fine-tuning methods."
}

Scene context:
{
  "scene_id": 9,
  "title": "Efficiency and Scalability",
  "summary": "While FHE introduces computational overhead, BlindFed remains efficient in terms of trainable parameters and GPU memory. It demonstrates scalability across varying numbers of clients and heterogeneous data distributions.",
  "paper_section": "Conclusions",
  "narrative_role": "conclusion",
  "time_allocation_sec": 7,
  "reference_style_examples": [
    "Unsqueeze [CLS] Bottleneck to Learn Rich Representations"
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
  "title": "Efficiency and Scalability",
  "audio_content": "BlindFed matches linear probing's memory footprint with minimal latency. It scales to 50 clients, even with highly heterogeneous data.",
  "bullets": [
    "Memory footprint comparable to linear probing",
    "Minimal latency overhead (4% in CIFAR-10/SVHN)",
    "Scales to 50 clients with heterogeneous data"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 10",
    "caption": "Efficiency comparison across datasets"
  },
  "source": ["Figure 10", "Table 3", "Table 4"],
  "time_cost": "7",
  "prompt": "A two-column slide with bullet points on the left summarizing efficiency and scalability, and Figure 10 on the right showing bar charts for parameter count, latency, and memory usage."
}"""

Token usage so far: 132973 prompt tokens, 5035 completion tokens

Cost so far: $1.48078

**Question**


You are an expert presentation designer finalizing a video slide.

The following content has been drafted for this scene:
{
  "title": "Efficiency and Scalability",
  "audio_content": "BlindFed matches linear probing's memory footprint with minimal latency. It scales to 50 clients, even with highly heterogeneous data.",
  "bullets": [
    "Memory footprint comparable to linear probing",
    "Minimal latency overhead (4% in CIFAR-10/SVHN)",
    "Scales to 50 clients with heterogeneous data"
  ],
  "figure": {
    "type": "paper_figure",
    "ref": "Figure 10",
    "caption": "Efficiency comparison across datasets"
  },
  "source": [
    "Figure 10",
    "Table 3",
    "Table 4"
  ],
  "time_cost": "7",
  "prompt": "A two-column slide with bullet points on the left summarizing efficiency and scalability, and Figure 10 on the right showing bar charts for parameter count, latency, and memory usage."
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
      "w": 0.4,
      "h": 0.7
    },
    "figure": {
      "x": 0.5,
      "y": 0.2,
      "w": 0.45,
      "h": 0.7
    }
  },
  "has_figure": true,
  "total_time_sec": "7"
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
    "title": "Efficiency and Scalability",
    "figure": {
      "type": "paper_figure",
      "ref": "Figure 10",
      "caption": "Efficiency comparison across datasets"
    },
    "bullets": [
      "Memory footprint comparable to linear probing",
      "Minimal latency overhead (4% in CIFAR-10/SVHN)",
      "Scales to 50 clients with heterogeneous data"
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
      "audio_segment": "BlindFed is designed for high efficiency and robust scalability.",
      "visual_emphasis": []
    },
    {
      "step_index": 1,
      "time_offset_sec": 1.75,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[0]"
        }
      ],
      "audio_segment": "It matches linear probing's memory footprint,",
      "visual_emphasis": []
    },
    {
      "step_index": 2,
      "time_offset_sec": 3.5,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[1]"
        }
      ],
      "audio_segment": "while maintaining minimal latency overhead.",
      "visual_emphasis": []
    },
    {
      "step_index": 3,
      "time_offset_sec": 5.25,
      "actions": [
        {
          "type": "fade_in",
          "target": "bullets[2]"
        }
      ],
      "audio_segment": "Furthermore, it scales effectively to 50 clients, even with highly heterogeneous data.",
      "visual_emphasis": []
    }
  ]
}"""

Token usage so far: 144074 prompt tokens, 5568 completion tokens

Cost so far: $1.60778

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

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE)
affiliation_2_logo: affiliation_2.png (Michigan State University (MSU), USA)

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
    "conference_logo": {
      "x": 0.8,
      "y": 0.05,
      "w": 0.15,
      "h": 0.1
    },
    "affiliation_logos": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.35,
      "h": 0.1
    },
    "title": {
      "x": 0.05,
      "y": 0.25,
      "w": 0.9,
      "h": 0.2
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.08
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.6,
      "w": 0.8,
      "h": 0.12
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.06
    }
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum impact, followed by a clear hierarchy for authors and their respective institutional details. The venue is placed at the bottom to anchor the design."
}"""

Token usage so far: 10707 prompt tokens, 417 completion tokens

Cost so far: $0.11958

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

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE)
affiliation_2_logo: affiliation_2.png (Michigan State University (MSU), USA)

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
    "conference_logo": {
      "x": 0.8,
      "y": 0.05,
      "w": 0.15,
      "h": 0.1
    },
    "affiliation_logos": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.35,
      "h": 0.1
    },
    "title": {
      "x": 0.05,
      "y": 0.25,
      "w": 0.9,
      "h": 0.2
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.08
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.6,
      "w": 0.8,
      "h": 0.12
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.06
    }
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum impact, followed by a clear hierarchy for authors and their respective institutional details. The venue is placed at the bottom to anchor the design."
}"""

Token usage so far: 10707 prompt tokens, 417 completion tokens

Cost so far: $0.11958

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

You are an expert presentation designer for academic video summaries.

You are designing the TITLE PAGE layout for a paper presentation video.

Paper metadata:
{
  "paper_title": "A Framework for Double-Blind Federated Adaptation of Foundation Models",
  "authors": [
    {
      "name": "Nurbek Tastan",
      "affiliation_id": 1
    },
    {
      "name": "Karthik Nandakumar",
      "affiliation_id": 2
    }
  ],
  "affiliations": [
    {
      "id": 1,
      "name": "Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE",
      "email_domain": "mbzuai.ac.ae"
    },
    {
      "id": 2,
      "name": "Michigan State University (MSU), USA",
      "email_domain": "msu.edu"
    }
  ],
  "venue": ""
}

Available logos:
conference_logo: conference.png
affiliation_1_logo: affiliation_1.png (Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE)
affiliation_2_logo: affiliation_2.png (Michigan State University (MSU), USA)

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
    "conference_logo": {
      "x": 0.8,
      "y": 0.05,
      "w": 0.15,
      "h": 0.1
    },
    "affiliation_logos": {
      "x": 0.05,
      "y": 0.05,
      "w": 0.35,
      "h": 0.1
    },
    "title": {
      "x": 0.05,
      "y": 0.25,
      "w": 0.9,
      "h": 0.2
    },
    "authors": {
      "x": 0.1,
      "y": 0.5,
      "w": 0.8,
      "h": 0.08
    },
    "affiliations": {
      "x": 0.1,
      "y": 0.6,
      "w": 0.8,
      "h": 0.12
    },
    "venue": {
      "x": 0.2,
      "y": 0.85,
      "w": 0.6,
      "h": 0.06
    }
  },
  "style_rationale": "This layout uses a balanced top-row approach for logos, placing the affiliation logos on the left and the conference logo on the right to frame the slide. The title is given a large central area for maximum impact, followed by a clear hierarchy for authors and their respective institutional details. The venue is placed at the bottom to anchor the design."
}"""

Token usage so far: 10707 prompt tokens, 417 completion tokens

Cost so far: $0.11958

