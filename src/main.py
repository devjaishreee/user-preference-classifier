import argparse
from pathlib import Path
import json
from .extractor import load_prompt, extract_preferences

def process_file(input_path: str, output_path: str, prompt_path: str):
    base_prompt = load_prompt(prompt_path)
    input_lines = Path(input_path).read_text().splitlines()

    results = []
    for line in input_lines:
        if not line.strip():
            continue
        preferences = extract_preferences(line.strip(), base_prompt)
        results.append(preferences)

    with open(output_path, "w") as f:
        for profile in results:
            f.write(json.dumps(profile, indent=2) + "\n")

    print(f"✅ Extracted {len(results)} profiles to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM-based user preference extractor")
    parser.add_argument("--input", required=True, help="Path to input text file")
    parser.add_argument("--output", required=True, help="Path to output JSONL file")
    parser.add_argument("--prompt", default="prompts/base_prompt.txt", help="Few-shot prompt template")

    args = parser.parse_args()
    process_file(args.input, args.output, args.prompt)
