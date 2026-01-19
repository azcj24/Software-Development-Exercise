#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass

from dotenv import load_dotenv
from google import genai


DEFAULT_TEXT = """
Content creators often work with long articles, research reports, or product notes and need a fast way to extract the key points.
They also frequently rewrite their content to match different audiences and platforms, such as LinkedIn, newsletters, or short-form video scripts.
A lightweight tool that can summarise text clearly and rephrase it in a specified tone helps creators iterate faster while keeping the original meaning.
""".strip()


@dataclass
class AIOutputs:
    summary: str
    rephrased: str


def read_input_text(path: str | None) -> str:
    if not path:
        return DEFAULT_TEXT
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def validate_text(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("Input text is empty.")
    wc = len(text.split())
    if wc < 30:
        raise ValueError(
            f"Input text is too short ({wc} words). Provide at least ~30 words."
        )


def build_summary_prompt(text: str) -> str:
    return (
        "Summarise the text into 2–3 concise sentences. "
        "Keep the key points and avoid extra commentary.\n\n"
        f"TEXT:\n{text}"
    )


def build_rephrase_prompt(text: str, tone: str) -> str:
    return (
        "Rephrase the text while preserving the original meaning and factual content.\n"
        f"Tone: {tone}\n"
        "Guidelines:\n"
        "- Do not add new facts.\n"
        "- Keep it roughly similar length (within +/- 20%).\n"
        "- Make it coherent and natural.\n\n"
        f"TEXT:\n{text}"
    )


def call_gemini(client: genai.Client, model: str, prompt: str) -> str:
    try:
        resp = client.models.generate_content(
            model=model,
            contents=prompt,
        )
    except Exception as e:
        raise RuntimeError(f"Gemini API call failed: {e}") from e

    text = getattr(resp, "text", None)
    if not text:
        raise RuntimeError("Gemini returned empty response.")
    return text.strip()


def generate_outputs(text: str, tone: str, model: str) -> AIOutputs:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "Missing API key. Set GEMINI_API_KEY (recommended) in .env or env vars."
        )

    client = genai.Client(api_key=api_key)

    summary = call_gemini(client, model, build_summary_prompt(text))
    rephrased = call_gemini(client, model, build_rephrase_prompt(text, tone))
    return AIOutputs(summary=summary, rephrased=rephrased)


def print_results(text: str, tone: str, outputs: AIOutputs) -> None:
    print("\n" + "=" * 80)
    print("ORIGINAL TEXT")
    print("=" * 80)
    print(text)

    print("\n" + "=" * 80)
    print("SUMMARY (2–3 sentences)")
    print("=" * 80)
    print(outputs.summary)

    print("\n" + "=" * 80)
    print(f"REPHRASED TEXT (Tone: {tone})")
    print("=" * 80)
    print(outputs.rephrased)
    print()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="AI Text Summarizer & Enhancer (Gemini).")
    p.add_argument("--input", type=str, default=None, help="Path to .txt file input.")
    p.add_argument("--tone", type=str, default="professional", help="Tone for rephrasing.")
    # ✅ 这里把默认模型换成更通用的
    p.add_argument("--model", type=str, default="models/gemini-flash-latest", help="Gemini model name.")

    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        text = read_input_text(args.input)
        validate_text(text)

        outputs = generate_outputs(text=text, tone=args.tone, model=args.model)
        print_results(text=text, tone=args.tone, outputs=outputs)

        # Auto demo: Shakespearean
        common = {"professional", "formal", "casual", "humorous", "persuasive"}
        if args.tone.lower() in common:
            demo_tone = "Shakespearean"
            demo_outputs = generate_outputs(text=text, tone=demo_tone, model=args.model)
            print_results(text=text, tone=demo_tone, outputs=demo_outputs)

        return 0
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
