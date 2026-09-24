# Video 3 — Demo Guide (how to perform & test it)

This is your behind-the-scenes checklist for the token-savings demo. Do all of this
**before** you film, so on camera you're confident and the numbers are real.

---

## 1. Local vs Online — decided: use it LOCALLY

Run markitdown **on your own computer**. Do **not** deploy anything or use a random online converter. Why:
- **Authentic** — showing the real terminal + real conversion is your whole "I measure it truly" brand.
- **Private** — you're not uploading your (possibly real) PDFs to someone else's website.
- **Simple** — it's two commands. Nothing to host.
- **One environment** — your token-counting script already runs locally with your Claude key, so keep everything in one place.

*(Future idea, not for this video: you could build and host a free PDF→Markdown web tool as a gift to your audience — that's a separate project/video, not this demo.)*

---

## 2. Tools you'll use
- **markitdown** — converts the PDF to Markdown (local).
- **token_compare_claude.py** — the script I gave you; reports real Claude input tokens for PDF vs Markdown.
- **The animation HTML** — generated from the prompts in the script; screen-recorded for the "wow" moment.
- **VS Code + Terminal** — to show the commands and code.
- **Cmd+Shift+5** — screen recording. **Boya mic** — audio.
- *(Skip the OpenAI Tokenizer web page — it uses OpenAI’s tokenizer, so its counts are wrong for Claude. Scene 2’s own animation replaces it.)*

---

## 3. One-time setup (do this once, in order)
```bash
# 1. Go to the project folder — the script lives here
cd ~/Demo/token-counter-practice

# 2. Create the virtual environment (only once, ever)
python3 -m venv venv

# 3. Activate it — your prompt should now start with (venv)
source venv/bin/activate

# 4. Install both tools INSIDE the venv
pip install "markitdown[all]" anthropic      # quotes required in zsh

# 5. Set your Claude API key (NEVER hard-code it, NEVER show it on screen)
export ANTHROPIC_API_KEY=sk-ant-...
```

**Order matters.** Activate the venv *before* installing, otherwise the packages land in the
system Python and the script will not find them.

**Every new terminal needs steps 3 and 5 again** — activation and the API key are per-terminal.
If you open a fresh tab right before filming, re-run both or the script will fail on camera.

Prefer to skip activation? Call the venv's Python directly — this works from any terminal:
```bash
./venv/bin/python token_compare_claude.py demo_heavy_report.pdf
```

In `token_compare_claude.py`, check the two config lines at the top:
- `MODEL` = the model you use (e.g. "claude-sonnet-5")
- `PRICE_PER_MTOK_INPUT` = that model's input price per 1M tokens (claude.com/pricing — Sonnet 5 is $2.00)

---

## 4. Your demo PDFs (both already in the folder)
| File | Role | Result |
|---|---|---|
| `demo_heavy_report.pdf` | **The star** — 50 pages, text-heavy, digital | 62.2% saved, nothing important lost |
| `demo_with_images.pdf` | **The counter-example** — 3 pages, 2 charts, a table | ~87% "saved", but both charts gone and the table corrupted |

If you want to swap in your own document, the rule is:
- **Good result:** a messy but **text-heavy digital** PDF — report with tables/columns, annual report, research paper. More pages = bigger saving.
- **Weak result:** a short, clean, plain-text PDF. That's fine — it's an honest contrast.
- **Never a scanned/image-only PDF.** markitdown extracts no text from those, so the "saving" would be fake.

---

## 5. Rehearse the full flow (once, before filming)
```bash
# 0. Start every session with these two lines
cd ~/Demo/token-counter-practice
source venv/bin/activate
export ANTHROPIC_API_KEY=sk-ant-...

# a) Convert — so you can show the clean .md on camera
markitdown demo_heavy_report.pdf -o demo.md
#    -> open demo.md, eyeball it: clean text, no binary junk

# b) Measure the star document (real Claude token counts)
python token_compare_claude.py demo_heavy_report.pdf
#    -> 123,724 vs 46,814 tokens  =  62.2% saved

# c) Measure the counter-example for Scene 6
python token_compare_claude.py demo_with_images.pdf
#    -> ~87% "saved" — but both charts are gone and the table is broken
```
Then:
- Plug the real numbers into the **main animation** HTML (the variables at the top).
- Open the animation in your browser, press space to play — check it looks right.
- Run through the whole on-camera sequence once without recording, so you're smooth.

**Token counting is free** — `count_tokens` is not billed, so rehearse as many times as you like.

---

## 6. Recording tips
- **Time-lapse the installs** — nobody wants to watch `pip install` scroll.
- **Never show the API key.** Use the env var; if your terminal ever prints it, blur it in editing.
- **Match the numbers.** The number in your terminal, and the number in your animation, must be the same. Mismatches are exactly what sharp viewers catch.
- Record the terminal/script part with Cmd+Shift+5; record the animation by playing it fullscreen in the browser and screen-recording.
- Zoom in / increase font size in your terminal and editor so it's readable on a phone.

---

## 7. Honesty checklist (this is your differentiator)
- [ ] Show the **real** measured number, whatever it is.
- [ ] Say out loud that it **varies by document**.
- [ ] Show at least a hint of the "small saving" case so you're not just hyping.
- [ ] Don't cherry-pick a 95% result and imply it's typical.

The hype videos claim "94%!" and move on. Your edge is: you measured it, you showed the real number, and you told the truth about when it does and doesn't help. That honesty is the content.

---

## 8. Quick troubleshooting
- `markitdown` can’t read a format → make sure you installed `markitdown[all]` (the `[all]` pulls in PDF/office support).
- Script error about the API key → your `ANTHROPIC_API_KEY` isn't set in that terminal session; re-run the `export` line.
- `ModuleNotFoundError: No module named 'anthropic'` (or `markitdown`) → the venv isn't active in this terminal. Run `source venv/bin/activate` (prompt shows `(venv)`), or call `./venv/bin/python` instead.
- `zsh: no matches found: markitdown[all]` → you forgot the quotes. Use `pip install "markitdown[all]"`.
- markitdown output attribute → the script already handles both `.markdown` and `.text_content`, so you're covered.
- Scanned/image-only PDF → markitdown has no local OCR (it uses pdfminer for text). Not used in this demo — stick to normal digital PDFs.
