# Token Counter — PDF vs Markdown

Does converting a PDF to Markdown really save AI tokens? This script answers that with
**Claude's own token counter**, so the numbers are real rather than estimated.

It takes one PDF and reports:

- how many input tokens the **PDF** costs when sent to Claude
- how many input tokens the same document costs as **Markdown**
- the difference, as tokens, percent, and dollars

```
  TOKEN COST  —  PDF  vs  MARKDOWN
──────────────────────────────────────────────────────────────
  File   demo_heavy_report.pdf
  Model  claude-sonnet-5

  PDF sent to Claude
  ██████████████████████████████████████████  123,724 tokens   $0.24745

  Markdown (markitdown)
  ████████████████  46,814 tokens   $0.09363

──────────────────────────────────────────────────────────────
  SAVED  76,910 tokens   62.2%
  $0.15382 per document  ·  $153.82 per 1,000 documents
  markdown extracted: 147,868 characters
──────────────────────────────────────────────────────────────
```

## Setup

Requires Python 3.9+ and an [Anthropic API key](https://console.anthropic.com/).

```bash
git clone <this-repo>
cd token-counter-practice

python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install "markitdown[all]" anthropic    # quotes are required in zsh

export ANTHROPIC_API_KEY=sk-ant-...        # Windows: set ANTHROPIC_API_KEY=...
```

The venv activation and the API key are **per terminal session** — open a new tab and you
need both again.

## Usage

```bash
python token_compare_claude.py your_file.pdf
```

Two sample documents are included so you can try it immediately:

```bash
python token_compare_claude.py demo_heavy_report.pdf   # 50-page text report
python token_compare_claude.py demo_with_images.pdf    # 3 pages with charts and a table
```

Set your model and its input price at the top of `token_compare_claude.py`:

```python
MODEL = "claude-sonnet-5"
PRICE_PER_MTOK_INPUT = 2.00   # see claude.com/pricing
```

**Running this is free.** The `count_tokens` endpoint is not billed, and no document is ever
sent to the model for processing — only measured.

## Why the saving happens

When you send a PDF, Claude does two things: it reads the extracted text, **and** it looks at
a rendered image of every page. Markdown only carries the text.

On the included 50-page report:

| | tokens |
|---|---|
| Markdown (text only) | 46,814 |
| PDF page images (50 × ~1,538) | ~76,910 |
| **PDF total** | **123,724** |

The text is identical in both cases. The entire difference is the page images, at roughly
1,500 tokens per page. So the saving is not "removing waste" — it is **removing the pictures**.

That also sets a ceiling on how much you can possibly save:

```
saving % = image_tokens_per_page / (image_tokens_per_page + text_tokens_per_page)
```

A densely written page (~3,000 characters) caps out around 62%. To reach the widely repeated
"90%", a page would need roughly 540 characters — which means the page is mostly picture, and
converting it destroys the document.

## Honest limitations

`markitdown` extracts **text only**. Its PDF path has no image handling at all, which has
consequences worth knowing before you trust a number:

- **Images are silently dropped.** Charts, diagrams and figures disappear with no placeholder.
  Captions survive, pointing at figures that no longer exist.
- **Tables can be silently corrupted.** Tables are reconstructed by clustering word positions;
  when that guess fails, rows collapse into plain text and a data row can be promoted into the
  header. Nothing warns you.
- **Scanned / image-only PDFs produce a fake result.** There is no text to extract, so the
  script will report a huge "saving" while the content is simply gone. Check the
  `markdown extracted: N characters` line — if it is tiny, the number is meaningless.

Run the script on `demo_with_images.pdf` and compare it with `demo_with_images.md` to see all
three effects at once. You will get a much larger percentage than the text report — on the
document where conversion costs you the most. That is the real lesson: **the biggest savings
show up exactly where Markdown is the worst choice.**

Use it for long, text-heavy documents. Do not use it for chart-heavy decks, scanned pages, or
anything where the layout carries meaning, such as forms and invoices. When the visuals matter,
sending the PDF and paying the image tokens is the correct decision.

## How it works

1. Reads the PDF, base64-encodes it, and sends it to `messages.count_tokens` as a `document`
   block — exactly how Claude would receive it if you uploaded the file.
2. Converts the same PDF to Markdown with `markitdown`, in memory.
3. Sends that Markdown to `count_tokens` as a plain text block.
4. Compares the two counts, using the same instruction text in both so the comparison is fair.

Two separate measurements. Nothing is combined, and nothing is ever answered by the model.
