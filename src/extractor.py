import os
import openai
import json
from pathlib import Path
from .schema import PREFERENCE_FIELDS

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt(prompt_path: str) -> str:
    return Path(prompt_path).read_text()

def call_gpt4(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that extracts structured user preferences."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response['choices'][0]['message']['content']

def extract_preferences(user_input: str, base_prompt: str) -> dict:
    full_prompt = base_prompt.replace("{{USER_INPUT}}", user_input)
    output = call_gpt4(full_prompt)
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw_output": output}
