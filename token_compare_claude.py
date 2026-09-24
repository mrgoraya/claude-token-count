"""
token_compare_claude.py
-----------------------
Proves how many tokens you save by converting a PDF to clean Markdown (markitdown)
BEFORE sending it to Claude — using Claude's OWN token counter, so the numbers are real.

What it does:
  1. Sends the PDF to Claude's count_tokens endpoint  -> real input tokens for the PDF
  2. Converts the PDF to Markdown with markitdown
  3. Sends that Markdown to count_tokens             -> real input tokens for the text
  4. Prints both counts, the % saved, and the $ difference

Setup (run once):
  pip install anthropic markitdown[all]
  export ANTHROPIC_API_KEY=sk-ant-...        # your key (never show this on screen!)

Run:
  python token_compare_claude.py your_file.pdf
"""

import base64
import os
import sys
from anthropic import Anthropic
from markitdown import MarkItDown

# ---------- terminal colours (no extra packages needed) ----------
# Colours are switched off automatically when the output is piped to a file
# or when NO_COLOR is set, so the text stays clean.
USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

CYAN, ORANGE, WHITE = "38;5;43", "38;5;209", "1;38;5;231"
MUTED, DIM, GREEN = "38;5;109", "38;5;240", "1;38;5;48"


def c(code: str, text) -> str:
    """Wrap text in an ANSI colour, or return it unchanged if colour is off."""
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else str(text)


def bar(value: int, maximum: int, width: int = 42) -> str:
    """A proportional block bar."""
    filled = round(width * value / maximum) if maximum else 0
    return "\u2588" * max(filled, 1)

# ---------- CONFIG (edit these) ----------
MODEL = "claude-sonnet-5"          # the model you actually use
PRICE_PER_MTOK_INPUT = 2.00        # <-- Claude Sonnet 5 input price per 1M tokens (check claude.com/pricing)
INSTRUCTION = "Summarize this document."   # same instruction for both, so it's a fair comparison
# -----------------------------------------

client = Anthropic()   # reads ANTHROPIC_API_KEY from your environment


def count_tokens(content_blocks) -> int:
    """Ask Claude how many INPUT tokens this message would use."""
    result = client.messages.count_tokens(
        model=MODEL,
        messages=[{"role": "user", "content": content_blocks}],
    )
    return result.input_tokens


def main(pdf_path: str):
    # 1) BEFORE — the raw PDF, exactly how Claude would receive it if you upload the file
    with open(pdf_path, "rb") as f:
        pdf_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

    pdf_blocks = [
        {"type": "document",
         "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_b64}},
        {"type": "text", "text": INSTRUCTION},
    ]
    pdf_tokens = count_tokens(pdf_blocks)

    # 2) AFTER — convert the same PDF to clean Markdown
    result = MarkItDown().convert(pdf_path)
    markdown_text = getattr(result, "markdown", None) or result.text_content

    md_blocks = [{"type": "text", "text": markdown_text + "\n\n" + INSTRUCTION}]
    md_tokens = count_tokens(md_blocks)

    # 3) Compare
    report(pdf_path, pdf_tokens, md_tokens, len(markdown_text))


def report(pdf_path: str, pdf_tokens: int, md_tokens: int, md_chars: int) -> None:
    saved = pdf_tokens - md_tokens
    pct = (saved / pdf_tokens * 100) if pdf_tokens else 0.0
    cost_pdf = pdf_tokens / 1_000_000 * PRICE_PER_MTOK_INPUT
    cost_md = md_tokens / 1_000_000 * PRICE_PER_MTOK_INPUT
    saved_cost = cost_pdf - cost_md
    peak = max(pdf_tokens, md_tokens)

    line = c(DIM, "\u2500" * 62)

    print()
    print(c(WHITE, "  TOKEN COST  \u2014  PDF  vs  MARKDOWN"))
    print(line)
    print(c(MUTED, "  File   ") + c(WHITE, os.path.basename(pdf_path)))
    print(c(MUTED, "  Model  ") + c(WHITE, MODEL))
    print()

    print(c(ORANGE, "  PDF sent to Claude"))
    print("  " + c(ORANGE, bar(pdf_tokens, peak))
          + c(WHITE, f"  {pdf_tokens:,} tokens")
          + c(MUTED, f"   ${cost_pdf:.5f}"))
    print()

    print(c(CYAN, "  Markdown (markitdown)"))
    print("  " + c(CYAN, bar(md_tokens, peak))
          + c(WHITE, f"  {md_tokens:,} tokens")
          + c(MUTED, f"   ${cost_md:.5f}"))
    print()
    print(line)

    if saved > 0:
        print("  " + c(GREEN, f"SAVED  {saved:,} tokens")
              + c(GREEN, f"   {pct:.1f}%"))
        print(c(MUTED, f"  ${saved_cost:.5f} per document")
              + c(DIM, "  \u00b7  ")
              + c(WHITE, f"${saved_cost * 1000:,.2f} per 1,000 documents"))
    else:
        print("  " + c(ORANGE, f"NO SAVING \u2014 markdown used {-saved:,} MORE tokens"))
        print(c(MUTED, "  (honest result \u2014 happens with already-clean, text-light PDFs)"))

    print(c(DIM, f"  markdown extracted: {md_chars:,} characters"))
    print(line)
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python token_compare_claude.py <file.pdf>")
        sys.exit(1)
    main(sys.argv[1])
