# User Preference Classifier (LLM-based)

This project uses GPT-4 to extract structured user preferences—like tone of communication, food habits, work routines, and behavioral traits—from freeform natural language input. It produces a JSON-style profile that downstream AI agents or personalization engines can use to tailor experiences to each user.

---

##  Highlights

-  **Few-shot GPT-4 prompt design** for nuanced extraction
-  **Structured JSON output** for easy downstream use
-  **Implicit signal detection** (e.g., inferring late-night productivity or tone preference)
-  **Plug-and-play module** for chatbots, recommendation systems, and personalization engines

---

##  Example Input

```
I usually skip breakfast but love spicy Indian food. I prefer direct, casual emails and work late nights.
```

##  Corresponding Output

```json
{
  "eats_breakfast": false,
  "likes_spicy_food": true,
  "communication_tone": "casual",
  "preferred_language": "English",
  "works_best_at_night": true,
  "available_on_weekends": null,
  "fitness_oriented": null,
  "likes_remote_work": null,
  "prefers_voice_over_text": null
}
```

---

##  Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/user-preference-classifier.git
cd user-preference-classifier
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set OpenAI API Key

```bash
export OPENAI_API_KEY=your-key-here
```

### Step 4: Run the Classifier

```bash
python src/main.py --input data/example_inputs.txt --output output/extracted_profiles.jsonl
```

---

##  Use Cases

- Personalized AI agents and assistants
- Recommendation engines in ecommerce or entertainment
- Mental health and wellness apps
- Adaptive learning platforms
- User behavior modeling in SaaS tools

---

##  Project Structure

```
user-preference-classifier/
├── data/                 # Input samples
├── output/               # Extracted JSONL profiles
├── prompts/              # Few-shot prompt for GPT-4
├── src/                  # Core logic (main, schema, extractor)
├── README.md
├── requirements.txt
```

---
