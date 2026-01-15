# AI-Powered Text Tool - Technical Approach & AI Utilisation Report

## 1. Overview (What the script does)
This prototype is a command-line Python tool that:
- Accepts an input text either from a `.txt` file or a built-in fallback paragraph.
- Uses a Generative AI model (OpenAI API) to:
  1) Summarise the input into **2–3 concise sentences**
  2) Rephrase the original text in a **user-specified tone**
- Prints the **original text**, **summary**, and **tone-adjusted rephrase** to the console.

The tool is designed for content creators who need quick summarisation and multiple rewrites in different styles for different platforms.

---

## 2. Contextual Tone Adjustment (The crucial 10%)
### 2.1 Feature description
A key feature is allowing the user to specify a **custom tone** using a CLI argument:
- Examples: `professional`, `casual`, `persuasive`, `humorous`
- Unique/challenging examples: `Shakespearean`, `pirate-speak`

This ensures the user can control the output style rather than receiving a generic rewrite.

### 2.2 Implementation detail
The tone is dynamically injected into the rephrasing prompt using a dedicated function:


def build_rephrase_prompt(text: str, tone: str) -> str:
    return (
        "You are a writing assistant for content creators.\n"
        "Task: Rephrase the text while preserving the original meaning and factual content.\n"
        f"Tone: {tone}\n"
        "Guidelines:\n"
        "- Do not add new facts.\n"
        "- Keep it roughly similar length (within +/- 20%).\n"
        "- Make it coherent and natural.\n\n"
        f"TEXT:\n{text}"
    )
## 3. AI Model & Integration

The tool integrates with the Google Gemini API using the official google-genai Python SDK.

A lightweight and fast model (models/gemini-flash-latest) was selected to balance response quality, speed, and cost efficiency for rapid prototyping.

## 4. Prompt Design & Refinement

Two distinct prompts are used:

Summarisation prompt
Explicitly constrains output to 2–3 sentences to ensure concise and focused results.

Rephrasing prompt
Dynamically injects the user-defined tone and includes guardrails (e.g. no new facts, similar length) to reduce hallucination risk.

Prompt iteration focused on:

Preventing unnecessary expansion of the text

Ensuring tone changes affect writing style rather than altering meaning

## 5. Error Handling Considerations

The script includes basic validation and error handling, such as:

Rejecting empty or overly short input text

Detecting missing API keys via environment variables

Handling API-level errors (e.g. unavailable models or quota limits)

In a production system, additional strategies such as retry logic, rate-limit handling, and input chunking for long texts would be considered.

## 6. Tools Used
AI Tools

Google Gemini API

Non-AI Tools

Python 3

google-genai

python-dotenv

Git & GitHub