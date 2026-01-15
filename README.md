## AIPowered Text Summarizer & Enhancer

### A lightweight Python command-line tool that uses a Generative AI model to:
- Summarise a block of text into 2–3 concise sentences
- Rephrase the original text in a user-defined tone (e.g. professional, casual, persuasive, Shakespearean)

This project was built as part of a software development exercise to demonstrate practical AI integration, prompt design, and basic software engineering practices.

--------------------------------------------------------------------------------
## Features

- 📄 Read input text from a `.txt` file or use a built-in fallback example
- ✍️ Generate a concise AI-powered summary (2–3 sentences)
- 🎭 Rephrase text using a **custom, user-specified tone**
- 🧠 Demonstrates prompt engineering and contextual tone adjustment
- ⚙️ Simple CLI interface with clear console output
- 🛡️ Environment-variable-based API key handling (no hardcoded secrets)

--------------------------------------------------------------------------------
## Project Structure

|-- summarizer.py

|-- input.txt

|-- requirements.txt

|-- AI-Powered Text Tool - Technical Approach & AI Utilisation Report.md

|-- README.md

|-- .gitignore

--------------------------------------------------------------------------------
## Requirements
- Python 3.9+
- A valid Google Gemini API key

Install dependencies:
pip install -r requirements.txt

--------------------------------------------------------------------------------
## Environment Setup
Create a .env file in the project root:
GEMINI_API_KEY=your_api_key_here

The API key is loaded via environment variables to avoid hardcoding sensitive credentials.

--------------------------------------------------------------------------------
## Usage
Run with a text file and specified tone:
python summarizer.py --input input.txt --tone professional

Run with a custom or creative tone:
python summarizer.py --tone Shakespearean

If no input file is provided, the script will use a built-in sample paragraph.

--------------------------------------------------------------------------------
## Example Output
The script prints:
1) Original text
2) AI-generated summary (2–3 sentences)
3) Rephrased version in the specified tone

When a common tone is used (e.g. professional), the script also automatically demonstrates a unique tone (Shakespearean) to showcase contextual tone adjustment.

--------------------------------------------------------------------------------
### AI Model
- Provider: Google Gemini
- Model: models/gemini-flash-latest

The model was selected for its speed, cost efficiency, and suitability for rapid prototyping.

--------------------------------------------------------------------------------
## Notes on Error Handling
The script includes basic validation and error handling, including:
- Empty or overly short input text
- Missing API keys
- API-level errors such as unavailable models or quota issues

Additional considerations and lessons learned are discussed in the accompanying technical report.

--------------------------------------------------------------------------------
## Author
Developed as part of a software engineering traineeship application to demonstrate:
- Practical AI integration
- Prompt design and iteration
- Clean project structure and documentation
