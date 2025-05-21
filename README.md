# 🧠 User Preference Classifier (LLM-based)

This project uses a GPT-4-based prompt-engineered pipeline to extract structured user preferences (like food habits, tone preferences, and work routines) from freeform natural language input. The result is a machine-readable JSON profile suitable for personalized AI agents, recommender systems, or customer support bots.

## ✅ Features
- 🔍 Few-shot learning with GPT-4
- 🧾 Structured output in JSON format
- 🧠 Implicit signal capture
- ⚙️ Easy integration into any personalization engine

## 📦 Example Input and Output
Input:
"I usually skip breakfast but love spicy Indian food. I prefer direct, casual emails and work late nights."

Output:
{
  "eats_breakfast": false,
  "likes_spicy_food": true,
  "communication_tone": "casual",
  "preferred_language": "English",
  "works_best_at_night": true
}

## 🚀 Getting Started
### 1. Clone the Repo
```bash
git clone https://github.com/your-username/user-preference-classifier.git
cd user-preference-classifier
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Set OpenAI API Key
```bash
export OPENAI_API_KEY=your-key-here
```
### 4. Run the Classifier
```bash
python src/main.py --input data/example_inputs.txt --output output/extracted_profiles.jsonl
```
