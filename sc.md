# Video 3 — Script (Roman Urdu)
### Working title: "I Measured the 'PDF to Markdown Saves 90% Tokens' Claim. It's Not 90%."

**Target length:** ~8:20
**One job:** viewer learns that converting PDFs to clean Markdown cuts token cost — sees a **real, measured** number (62.2%), understands **why** it works, and hears honestly when it doesn't.

---

## READ BEFORE YOU FILM
- Spoken lines are Roman Urdu — say them naturally, don't read stiffly. Tech terms (token, PDF, Markdown, markitdown, API, script) stay in English.
- **Run the whole demo end-to-end ONCE before filming** and write down your real numbers. (Full steps: see the Demo Guide file.)
- **NEVER show your API key on screen.** Use an environment variable; blur it if it ever appears.
- **You are on zsh.** Square brackets must be quoted: `pip install "markitdown[all]"`. Without quotes zsh fails with `no matches found`. Test every command in the exact terminal you'll film in.
- Boya mic clipped + selected + tested. Quiet room. Time-lapse any installs. **Film the hook LAST** — you'll say it better once you know the whole video.
- **[SAY]** = spoken (Roman Urdu). **[SHOW]** = on screen. **[ANIMATION]** = generate with the given prompt (Claude Code) and drop the screen-recording in here.

### Retention rules this script follows
1. **No slow build-up.** The real number appears in the first 10 seconds. Withholding it doesn't create curiosity — it creates exits.
2. **Two open loops planted in the hook** (*why* it isn't 90%, and the case where the trick fails) and closed in Scenes 3 and 6. Say them out loud; don't assume the viewer infers them.
3. **Nothing on screen is static for more than ~8 seconds.** Terminal → animation → your face → side-by-side. Every scene changes visual mode at least once.
4. **A participation beat before the reveal** (Scene 5). Asking for a guess buys you the 30 seconds that usually leak right before a payoff.
5. **The honest counter-example moved earlier** (5:40, not 6:30) — it's your best content and it should land while people are still watching.

---

## THE SCRIPT

### Scene 1 — COLD OPEN (0:00–0:30) — teen shots
*(Film this LAST. Jab poori video ban chuki ho, tab hook confident nikalta hai.)*

#### SHOT 1 — Terminal (0:00–0:03)
**[SHOW]** Sab se pehli cheez jo screen par aati hai. **Koi intro nahi, koi logo nahi, salaam bhi abhi nahi.**
```bash
cd ~/Demo/token-counter-practice
source venv/bin/activate
export ANTHROPIC_API_KEY=sk-ant-...
python token_compare_claude.py demo_heavy_report.pdf
```
- Record se pehle terminal font bara karein (Cmd + `+`, ~18–20pt) — phone par parha jana chahiye.
- **Cmd+Shift+5** → Record Selected Portion → terminal window → command chalaein → stop.
- Editing mein sirf wo 2–3 second rakhein jahan `SAVED  76,910 tokens  (62.2%)` saaf dikhe.
- **Command type hote hue mat dikhaein.** Hook mein intezaar nahi hona chahiye.

**[SAY]**
- "Ye ek hi document par 62 percent token saving hai — aur ye number main ne guess nahi kiya, measure kiya hai."

#### SHOT 2 — Claim animation (0:03–0:13)
**[ANIMATION — "90% claim"]** — generate this, fullscreen browser mein record karein (Cmd+Ctrl+F, phir Cmd+Shift+5, phir page reload taake auto-play ho):
```
Build an animation, 16:9 filling 1920x1080, for the opening hook of a YouTube video.
TOTAL RUNTIME MUST BE EXACTLY 10 SECONDS. It auto-plays on load.
It presents a popular claim, then casts doubt on it and sets up a test.
All on-screen lines are Roman Urdu — render them exactly as written, do not translate.

EDITABLE VARIABLES AT THE VERY TOP:
  claimNumber   = 90
  claimLine     = "Ye claim kiya jata hai:"
  savingLine    = "90% tokens save kar sakte hain"
  costLine      = "Matlab 90% cost bhi bach jati hai"
  questionLine  = "Sach hai ya nahi?"
  closingLine   = "Chaliye measure karte hain"
All percentages on screen come from claimNumber.

STYLE:
- Dark background #0F2C3F. Cyan #17D0B0 and teal #13B7A3. White #FFFFFF, muted #9FB4BC.
- Warm red-orange #F2704B reserved for the doubt beat only.
- Big, bold, legible sans-serif — readable when the video is small.
- A voiceover runs over this, so keep text minimal: one line at a time, never two competing.
- Smooth, eased, premium motion. Confident at first, unsettled later.

EXACT TIMELINE — build to these marks:

BEAT 1 — the claim, presented confidently (0.0s – 4.5s)
0.0s – 0.8s   claimLine fades in small at the top, muted.
0.8s – 2.2s   A huge "90%" scales up in the centre in bold cyan, with a soft glow — it should
              look like a confident, hype-style claim.
2.2s – 3.2s   savingLine fades in beneath it in white. At the same time, a row of small cyan
              token pills across the screen rapidly drains away — most of them vanish,
              leaving only a few, visually showing the 90% disappearing.
3.2s – 4.5s   costLine replaces savingLine, and a dollar figure beside the "90%" ticks
              downward fast, as if cost is collapsing.

BEAT 2 — the doubt (4.5s – 7.2s)
4.5s – 5.2s   Everything stops. The motion freezes for a moment — a deliberate, noticeable
              pause, like a record scratch.
5.2s – 6.2s   The huge "90%" desaturates from cyan to muted grey and begins to flicker and
              wobble slightly, as if unreliable. The glow dies.
6.2s – 7.2s   A large red-orange question mark drops in over the "90%", landing with weight.

BEAT 3 — the test (7.2s – 10.0s)
7.2s – 8.3s   questionLine fades in, white and bold, below the wobbling number.
8.3s – 10.0s  closingLine fades in beneath it in cyan and holds to the end.

The emotional arc is the point: the first half should feel like every hype video the viewer
has already seen, and the freeze at 4.5s should feel like someone pressing pause on it.
Make that stop abrupt — if the transition is smooth, the hook does not work.
```
**[SAY]** over the animation:
- "Aap ne YouTube par ye zaroor suna hoga: 'PDF ko Markdown mein convert karo, 90 percent tokens bachao.' Main ne wo claim test kiya — Claude ke apne token counter se."

> **Sync note:** animation ka freeze (4.5s) aur aap ka "Main ne wo claim test kiya" — dono ek saath aane chahiye. Yahi shot ki jaan hai.

#### SHOT 3 — Aap camera par (0:13–0:30)
**[SHOW]** Pehli baar aap ka chehra. Boya mic, quiet room, achhi light.
**[SAY]**
- "Asli number 90 nahi nikla. Lekin jo wajah main ne dhoondi, wo us claim se zyada kaam ki hai — kyunke ye batati hai ke aap asal mein paise **kis cheez** ke de rahe hain."
- "Aur aakhir mein wo case bhi dikhaunga jahan ye trick bilkul kaam nahi karti — balke aap ko jhoota number dikhati hai."

> **Teen ghaltiyan jo hook maar deti hain:** (1) shuru mein "assalam-o-alaikum, kaise hain aap sab" — 3 second zaya; (2) terminal shot 4–5 second tak chalana — log number parh chuke hote hain; (3) channel intro animation. Pehle 3 second mein number screen par hona chahiye.

---

### Scene 2 — AAP KIS CHEEZ KE PAISE DETE HAIN (0:30–1:05)
*(Deliberately short. This used to be 65 seconds and it was the biggest drop-off risk in the video.)*
**[SAY]**
- "Teen line mein base clear kar lete hain, phir seedha demo par."
- "AI aap ka text chhote tukdon mein torta hai — un ko **token** kehte hain. Aap ka bill inhi tokens par banta hai. Zyada tokens, zyada paisa. Bas."

**[ANIMATION — "text into tokens"]**
```
Build a single self-contained HTML file (inline CSS/JS, no libraries), 16:9 / 1920x1080,
dark background #0F2C3F, that animates a sentence breaking into tokens for a YouTube explainer.

- Show one example sentence, big, white, centered. Put the sentence as an editable variable
  at the top (e.g. "AI agents can use tools.").
- On play, the sentence splits into individual token chunks: each token becomes a rounded pill
  with a cyan (#17D0B0) / teal (#13B7A3) background, and the pills gently separate with a smooth
  staggered animation.
- Under the pills, a number counts up to the total token count, ending on a label like "8 tokens".
- Then a line fades in below in muted white (#9FB4BC): "More tokens = more cost."
- Press spacebar or click to replay.
Keep the motion smooth and premium. Editable variables (sentence, colors) at the top.
```
**[SAY]** over the animation:
- "Ek chhota sa jumla — aath tokens. Ab zara socheye 50 page ki ek report."

---

### Scene 3 — PDF KE SAATH ASAL MEIN HOTA KYA HAI (1:05–2:40) ← the "aha" moment
*(This is the scene that makes your video different from every other one on this topic. They all say "PDF is heavy". None of them say why.)*
**[SAY]**
- "Ab wo baat jo mujhe khud measure karne ke baad samajh aayi — aur jo kisi aur video mein nahi milti."
- "Jab PDF Claude ko jati hai, to Claude do kaam karta hai. **Pehla** — wo us ka text parhta hai. **Doosra** — wo har page ki tasveer bhi dekhta hai, jaise screenshot."
- "Matlab agar aap ki PDF 5 page ki hai, to Claude 5 snapshots bhi process karta hai — text ke **saath**, text ke bajaye nahi."
- "Aur har page ki wo tasveer taqreeban pandrah sau tokens kha jati hai. **Yahi asal kharcha hai** — text nahi, tasveerein."

**[ANIMATION 1 — "what Claude does with a PDF"]** — generate this, show it here:
```
Build a single self-contained HTML file (all CSS and JS inline, no external libraries),
16:9 filling 1920x1080, that explains in animation what happens when a PDF is sent to Claude.
This is for a YouTube explainer, so it must be readable when the video is small.

EDITABLE VARIABLES AT THE VERY TOP:
  fileName       = "report.pdf"
  pageCount      = 5
  textTokensPerPage  = 936
  imageTokensPerPage = 1538
Compute every total from these — I should only edit these four numbers.

STYLE:
- Dark background #0F2C3F. Accent cyan #17D0B0 and teal #13B7A3.
- White text #FFFFFF, muted #9FB4BC. Warm red-orange #F2704B for the image/snapshot path.
- Big, bold, legible sans-serif. Generous spacing. Premium, smooth, eased motion.
- Title at top: "What Claude does with a PDF".

LAYOUT: a PDF document icon on the LEFT labeled with fileName and "5 pages".
A "CLAUDE" panel on the RIGHT. The space between them is where the two paths travel.

ANIMATION — two clearly separated steps, auto-playing in sequence:

STEP 1 (label appears: "1 — Claude reads the text"):
- The PDF icon emits a stream of text lines that travel along an UPPER path toward Claude.
- The lines condense into a cyan pill labeled "Text" with a number counting up to
  pageCount * textTokensPerPage, shown as "4,681 tokens".
- Keep this path entirely in the upper half of the frame.

STEP 2 (label appears: "2 — Claude also looks at every page"):
- The PDF icon fans out into pageCount separate page thumbnails (simple rectangles with
  faint grey lines suggesting content, each with a subtle camera-shutter flash as it is created).
- These travel along a LOWER path toward Claude, staggered one after another.
- Each thumbnail carries a small label "~1,538 tokens".
- They condense into a red-orange pill labeled "5 page images" counting up to
  pageCount * imageTokensPerPage, shown as "7,690 tokens".
- Keep this path entirely in the lower half of the frame, clearly mirroring the upper path.

STEP 3 (both paths arrive):
- The two pills merge at the Claude panel into one total that counts up to
  pageCount * (textTokensPerPage + imageTokensPerPage) — "12,371 tokens".
- A line fades in beneath in muted white: "Text + a picture of every page."

The upper (text) and lower (image) paths must stay visually separate and symmetrical the whole
time — that separation is the entire point of the animation.

INTERACTION: press spacebar or click to replay from the start.
```

**[SAY]**
- "To sawaal ye bana: agar hum Claude ko sirf saaf text bhej dein — bina page ki tasveeron ke — to kya hoga? Jawab hai: **Markdown.**"

**[ANIMATION 2 — "what Claude does with Markdown"]** — generate this in the SAME Claude Code session as Animation 1, so the layout matches:
```
Build a single self-contained HTML file (all CSS and JS inline, no external libraries),
16:9 filling 1920x1080, that explains what happens when a Markdown file is sent to Claude
instead of a PDF. This is the companion piece to a previous animation about PDFs and MUST use
the identical layout, scale, positions, colors and timing, so the two can be cut back to back
and the difference is instantly obvious.

EDITABLE VARIABLES AT THE VERY TOP:
  fileName          = "report.md"
  pageCount         = 5
  textTokensPerPage = 936
  imageTokensPerPage = 1538   // only used to show what is SKIPPED
Compute every total from these.

STYLE: identical to the PDF animation — dark #0F2C3F, cyan #17D0B0, teal #13B7A3,
white #FFFFFF, muted #9FB4BC, red-orange #F2704B. Same fonts and sizes.
Title at top: "What Claude does with Markdown".

LAYOUT: a Markdown document icon on the LEFT labeled with fileName. A "CLAUDE" panel on the
RIGHT, in exactly the same position as in the PDF animation.

ANIMATION:

STEP 1 (label: "1 — Claude reads the text"):
- Same upper path as the PDF animation: a stream of text lines travels to Claude and condenses
  into a cyan pill counting up to pageCount * textTokensPerPage — "4,681 tokens".
- This should look and time out identically to the PDF version.

STEP 2 (label: "2 — There are no pages to look at"):
- The LOWER path stays empty, drawn as a faint dashed outline where the page thumbnails
  appeared in the PDF animation — the same positions, but hollow and muted #9FB4BC.
- Ghosted text sits in that empty lane: "No page images — 7,690 tokens skipped"
  (computed from pageCount * imageTokensPerPage), in muted grey, deliberately understated.

STEP 3:
- The total at the Claude panel counts up to only pageCount * textTokensPerPage — "4,681 tokens".
- A line fades in beneath in muted white: "Same words. No pictures."
- A softer second line in muted grey: "Layout and charts are lost — that's the trade."

The empty lower lane is the whole message: the viewer should immediately see that the bottom
half of the PDF animation is simply gone here.

INTERACTION: press spacebar or click to replay from the start.
```
**[SAY]** over Animation 2:
- "Dekhiye — wohi alfaz, lekin page ki tasveerein gayab. Yahi jagah hai jahan tokens bachte hain."
- "Aur ye free nahi hai. Is mein layout, charts, aur diagrams ki visual information chali jati hai. Text wale document ke liye ye zabardast sauda hai — charts wale document ke liye nahi. Is par aakhir mein wapas aate hain."

> **Loop closed:** the hook promised "why it isn't 90%" — this scene delivers it. Say it explicitly: *"Isi liye 90 percent nahi hota — text to dono mein jata hai, farq sirf tasveeron ka hai."*

---

### Scene 4 — THE TOOL: markitdown (2:40–3:30)
*(Keep this fast. It's a tool, not the story. Under a minute.)*
**[SAY]**
- "Iske liye main Microsoft ka **markitdown** use kar raha hoon. Open source, bilkul free, aur PDF, Word, Excel, PowerPoint — sab ko clean Markdown bana deta hai."
- "Aur ye mere apne computer par chal raha hai — kisi online website par nahi. Aap ke documents aap hi ke paas rehte hain."
**[SHOW]** terminal, zoomed:
```
pip install "markitdown[all]"
markitdown demo_heavy_report.pdf -o demo.md
```
- WARNING — **quotes zaroori hain**: zsh mein bina quotes ke `markitdown[all]` fail ho jata hai. Ye galti camera par mat karna.
- **[SHOW]** the PDF and the `.md` side by side, then scroll the markdown fast for 2 seconds.
- "Same content — ab saaf text mein. Chaliye ab asli test."

---

### Scene 5 — GUESS, PHIR MEASUREMENT (3:30–5:40) ← THE CORE
**[SAY]**
- "Main ne ek chhota script likha hai jo **Claude ke apne token counter** se poochta hai: ye PDF kitne tokens leti hai, aur wohi content Markdown mein kitne."
- "Aur ye bilkul free hai — token counting par Anthropic paise nahi leta. Main isay jitni baar chahe chala sakta hoon, zero cost."

**[SAY — participation beat, look straight at camera]**
- "Rukiye. Script chalane se pehle aap ka guess kya hai? Ye 50 page ki report — kitne percent bachenge? Abhi comment mein likh dijiye, phir dekhte hain aap ka andaza kitna sahi tha."

**[SHOW]** run it live: `python token_compare_claude.py demo_heavy_report.pdf`
**[SHOW]** the real output, zoomed:
```
  PDF sent to Claude   :    123,724 tokens   $0.24745
  Markdown (markitdown):     46,814 tokens   $0.09363
  SAVED                :     76,910 tokens   (62.2%)
```
**[SAY]**
- "Bas — 62.2 percent. Agar aap ne 90 socha tha, to aap akele nahi hain — internet yahi keh raha hai."
- "Aur dekhiye ye numbers apas mein kya kehte hain. Markdown ke 46,814 tokens — ye document ka poora text hai. Aur jo 76,910 bache — un ko 50 pages par taqseem karein to har page taqreeban **1,538 tokens**. Bilkul wohi number jo main ne animation mein dikhaya tha. Ye page ki tasveeron ka kharcha tha."

**[ANIMATION — main comparison bars]**
```
Build me a single self-contained HTML file (all CSS and JS inline, no external libraries)
that plays a smooth animated data visualization for a YouTube demo video. It compares AI token
usage before vs after converting a PDF to Markdown.

DATA — editable variables at the very top:
  pdfTokens = 123724
  mdTokens  = 46814
  pricePerMillion = 2.00   // USD per 1M input tokens (Claude Sonnet 5)

STYLE:
- 16:9, fills a 1920x1080 frame. Dark background #0F2C3F.
- Accent colors cyan #17D0B0 and teal #13B7A3. White text #FFFFFF, muted #9FB4BC.
- Big, bold, legible sans-serif. Readable when the video is small.
- Title at top: "PDF vs Markdown — token cost".

ANIMATION (smooth, eased, auto-plays on load):
1. Two vertical bars rise to heights proportional to their token counts. Left bar labeled
   "PDF sent to Claude" (tall, warm red-orange). Right bar "Markdown (markitdown)" (short, cyan).
   Ease up over ~1.2s.
2. A number above each bar counts up from 0 to its real value (comma-formatted) as the bar rises.
3. After they settle, a big cyan headline pops in: "Saved 62%" — COMPUTE the % from the numbers.
4. A line fades in below: "$X saved per document" — computed from pricePerMillion.
5. Soft glow behind the winning (markdown) bar; gentle count-up easing.

INTERACTION: press spacebar or click to replay from the start.
Compute all % and $ from the variables — I should only edit the three numbers at the top.
Keep the motion premium and smooth.
```
**[SAY]** over the animation:
- "Ab paise ki baat. Ek document par bachat hui pandrah cent — sunne mein kuch bhi nahi."
- "Lekin hazaar documents par ye **ek sau chauwan dollar** ban jata hai. Sirf input par, sirf ek model par. Aur RAG system mein hazaar documents mahine mein nahi — hafte mein poore ho jate hain."

---

### Scene 6 — SACH, POORA SACH (5:40–6:50) ← your differentiator
*(Moved 50 seconds earlier than the old script. This is your best material — it shouldn't play to an empty room.)*
**[SAY]**
- "Ab wo baatein jo hype wali videos nahi kartin. Teen cheezein."
- "**Ek** — ye hamesha 62 percent nahi hota, ye document par depend karta hai."
- **[SHOW]** run the script on a short, plain, text-only PDF (2–3 pages, no tables). "Dekhiye — is saaf PDF par bachat bohot kam hai. Wajah wohi hai: kam pages, matlab kam tasveerein, matlab bachane ko kam."
- "**Do** — aap kuch kho rahe hain. Markdown mein layout, charts aur diagrams ki visual information chali jati hai. Agar aap ka document charts par khara hai, to ye bachat aap ko mehngi par sakti hai."
- "**Teen**, aur ye sab se zaroori hai — **scan ki hui PDF par ye bilkul mat karna.** Scanned PDF mein text hota hi nahi, sirf tasveerein hoti hain. markitdown us se kuch nikaal hi nahi paata, to script aap ko 98 percent bachat dikha dega — jo **jhoot** hai. Kuch bacha nahi, content hi gaayab ho gaya."
- "Main ne ye khud check kiya, isi liye bata raha hoon. Jo videos aap ko 94 percent dikhati hain — un mein se kuch ke saath bilkul yahi hua hota hai."

> **Loop closed:** this is the "case where it doesn't work" you promised in the hook. Call it back out loud: *"Ye tha wo case jis ka main ne shuru mein wada kiya tha."*

---

### Scene 7 — TO ISE KAB USE KAREIN (6:50–7:40)
**[SAY]**
- "Simple rule: **text wale, lambe documents** — reports, papers, contracts, transcripts. Jitne zyada pages, utni zyada bachat."
- "Aur **mat** karein: charts wale decks, scanned documents, ya aisi cheezein jahan layout ka apna matlab hota hai — jaise forms aur invoices."
- "Sab se zyada faida RAG aur document Q&A systems mein hai, jahan aap wohi documents baar baar AI ko bhejte hain. Wahan ye chhoti si aadat har mahine aap ka bill kaat deti hai."

---

### Scene 8 — RECAP + CTA (7:40–8:20)
**[SAY]**
- "Jaldi se recap. PDF ke saath aap text bhi bhejte hain aur har page ki tasveer bhi — aur asal kharcha tasveeron ka hai. Markdown wo tasveerein hata deta hai. Mere 50 page ke document par is se 62 percent bacha; hazaar documents par ek sau chauwan dollar."
- "Lekin apne document par khud measure karke dekhiye — script description mein hai, free hai, aur Claude ke apne numbers deti hai."
- "Aap ka guess kitna sahi nikla? Comment mein bataiye — aur agar apni PDF par chala kar koi ajeeb number dekha, wo zaroor share kijiye."
- "Agar aap AI agents banana seekh rahe hain, meri pichli do videos dekhiye — main ye sab step by step bana raha hoon." **[SHOW/link previous videos]**
- "Subscribe kar dijiye. Milte hain agli video mein."

---

## DESCRIPTION CHAPTERS (paste into YouTube — chapters measurably help retention)
```
0:00  62% — the real measured number
0:30  Tokens: what you are actually paying for
1:05  What Claude really does with a PDF
2:40  markitdown (free, local, open source)
3:30  Guess the number, then the live measurement
5:40  The honest truth: when this fails
6:50  When to use it (and when not to)
7:40  Recap
```

## TITLE + THUMBNAIL
- **Title A (recommended):** "I Measured the 'PDF to Markdown Saves 90%' Claim. It's Not 90%."
- **Title B:** "Why Your PDF Costs 2.6x More Tokens Than Its Own Text"
- **Thumbnail:** your face + the two bars + big text **"62%"** with a small struck-through **"90%"**. The contradiction is the click — and because you deliver the number in the first 10 seconds, it is not clickbait.

---

## PRODUCTION CHECKLIST
- [ ] Ran the full demo once before filming; real numbers written down (123,724 / 46,814 / 62.2%).
- [ ] Every command tested in **zsh with quotes** — `pip install "markitdown[all]"`.
- [ ] Animation numbers MATCH the terminal output on screen (no mismatch).
- [ ] API key never visible (env var; blur if needed).
- [ ] Star demo = a **text-heavy digital** PDF (the 50-page report). Counter-example = a short clean PDF. **Never a scanned PDF.**
- [ ] Both Scene 3 animations generated in the SAME session so their layouts match.
- [ ] Hook filmed LAST; opening terminal shot cut to 2 seconds.
- [ ] Boya mic tested; quiet room; installs time-lapsed.
- [ ] English title + thumbnail, Urdu audio, tech terms English.
- [ ] Chapters pasted into the description; back-link to Video 1 & 2.
- [ ] Target ~8:20. Publish. Then Video 4.
