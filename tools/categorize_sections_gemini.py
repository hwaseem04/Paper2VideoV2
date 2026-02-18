"""
Categorize and reorganize paper sections into standard categories using Gemini.
Reads from section_summary_extraction_chatgpt and outputs to categorised_section_summary_extraction_gemini.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))
from llms.gemini import GEMINI


CATEGORIZATION_PROMPT_TEMPLATE = """You are analyzing a research paper that has been divided into sections with summaries. Your task is to reorganize these sections into a standard structure.

CURRENT SECTIONS:
{sections_json}

STANDARD CATEGORIES (in order):
1. abstract - Paper abstract/summary
2. introduction - Introduction, motivation, background
3. method - Methodology, approach, proposed method, related work if it's foundational to the method
4. experiments - Experimental setup, datasets, implementation details
5. results - Results, findings, analysis, discussion
6. conclusion - Conclusion, future work, limitations
7. supplementary - Supplementary material (if exists)

YOUR TASK:
1. Analyze each section's content and determine which standard category it belongs to
2. If multiple sections belong to the same category, MERGE them by combining their content
3. If a section contains both experiments AND results, SPLIT it into two separate entries
4. DO NOT modify the actual content/text - only reorganize and categorize
5. If a section doesn't fit any category, assign it to the most appropriate one

OUTPUT FORMAT:
Return ONLY a JSON object mapping standard categories to their content. Example:
{{
  "abstract": "content from abstract section",
  "introduction": "content from introduction section",
  "method": "merged content from 'related work' + 'proposed method' sections",
  "experiments": "content from experimental setup",
  "results": "content extracted from results section",
  "conclusion": "content from conclusion",
  "supplementary": "content from supplementary if exists"
}}

IMPORTANT:
- Only include categories that have content
- Preserve the exact text content from the original sections
- When merging, concatenate the content as key-value pairs in the order they appear (for e.g., "related work" content followed by "proposed method" content under "method")
- When splitting, intelligently separate experiment details from results
- Return ONLY the JSON object, no explanations or markdown formatting"""


def categorize_sections(paper_data, gemini_client):
    """
    Use Gemini to categorize and reorganize sections into standard structure.

    Args:
        paper_data: Dictionary with paper sections
        gemini_client: GEMINI client instance

    Returns:
        Dictionary with categorized sections
    """
    paper_name = paper_data.get("paper_name", "Unknown")
    sections = paper_data.get("sections", {})

    if not sections:
        print(f"  WARNING: No sections found in paper")
        return {}

    # Format sections for the prompt
    sections_json = json.dumps(sections, indent=2)
    prompt = CATEGORIZATION_PROMPT_TEMPLATE.format(sections_json=sections_json)

    print(f"  Categorizing {len(sections)} sections...")

    # Query Gemini
    _, response = gemini_client.query(
        prompt=prompt
    )

    # Parse response
    try:
        categorized = json.loads(response.strip())

        if not isinstance(categorized, dict):
            print(f"  ERROR: Response is not a dictionary")
            return {}

        print(f"  ✓ Reorganized into {len(categorized)} standard categories:")
        for category in categorized.keys():
            print(f"    - {category}")

        return categorized

    except json.JSONDecodeError as e:
        print(f"  ERROR: Failed to parse JSON response: {e}")
        print(f"  Response preview: {response[:200]}...")
        return {}


def process_all_papers(input_dir, output_dir):
    """
    Process all papers from input_dir and save categorized versions to output_dir.

    Args:
        input_dir: Directory containing paper JSONs with sections
        output_dir: Directory to save categorized JSONs
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize Gemini client
    print("Initializing Gemini client...")
    gemini_client = GEMINI(config_path=Path("config.yml"))
    print(f"Using model: {gemini_client.model}\n")

    # Get all JSON files
    json_files = sorted(list(input_path.glob('*.json')))

    # Filter out empty JSON files
    valid_files = []
    for json_file in json_files:
        with open(json_file) as f:
            data = json.load(f)
            if data and data != {}:  # Not empty
                valid_files.append(json_file)

    print(f"Found {len(valid_files)} non-empty JSON files to process")
    print(f"(Skipped {len(json_files) - len(valid_files)} empty files)\n")

    # Process each paper
    results = {}
    for i, json_file in enumerate(valid_files, 1):
        print(f"\n[{i}/{len(valid_files)}] Processing: {json_file.name}")
        print("-" * 80)

        try:
            # Read paper data
            with open(json_file) as f:
                paper_data = json.load(f)

            # Categorize sections
            categorized_sections = categorize_sections(paper_data, gemini_client)

            if not categorized_sections:
                print(f"  ✗ Skipping due to errors")
                results[json_file.name] = "ERROR: No categorized sections"
                continue

            # Create output data
            output_data = {
                "paper_name": paper_data.get("paper_name", json_file.stem),
                "num_sections": len(categorized_sections),
                "sections": categorized_sections,
                "method": "gemini_categorized"
            }

            # Save to output file
            output_file = output_path / json_file.name
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)

            print(f"  ✓ Saved to: {output_file.name}")
            results[json_file.name] = len(categorized_sections)

        except Exception as e:
            print(f"  ✗ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()
            results[json_file.name] = f"ERROR: {str(e)}"

    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    successful = 0
    for filename, result in results.items():
        if isinstance(result, int):
            print(f"✓ {filename}: {result} categories")
            successful += 1
        else:
            print(f"✗ {filename}: {result}")

    print(f"\nSuccessfully processed: {successful}/{len(valid_files)}")
    print(f"Output saved to: {output_path}")

    # Print token usage
    print("\n" + "=" * 80)
    print("TOKEN USAGE")
    print("=" * 80)
    gemini_client._post_process()


if __name__ == "__main__":
    input_directory = "data_reference/section_summary_extraction_chatgpt"
    output_directory = "data_reference/categorised_section_summary_extraction_gemini"

    process_all_papers(input_directory, output_directory)
