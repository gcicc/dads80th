# 80th Birthday Sprint — Parallel Workstreams

**Deadline:** ~March 2026 (4 weeks)
**Approach:** Each workstream owns specific files. No overlapping edits. Run in separate Positron/Claude Code instances.

---

## WS1: PHOTO — Curate & Place Images
**Owner:** Greg + Claude instance
**Effort:** 2–3 sessions

### What
- Survey `../Lit-Project/images/` (212+ photos) and select 30–50 for the book
- Copy selected photos into `images/{heritage,military,family,career,recent}/`
- Add Quarto image layout blocks to chapters (lightbox for HTML, static for PDF)
- Download P1020477.JPG from Gmail via MCP attachment tool

### Files Owned
```
images/**/*          (all contents)
```

### Files It Edits (coordinated inserts only)
- Chapters: adds `![caption](../images/...)` blocks at marked `<!-- PHOTO: -->` insertion points
- _Rule:_ only add image blocks, never change narrative text

### Depends On
- Lit-Project images accessible at `../Lit-Project/images/`
- Chapter text stable (don't rewrite chapters while placing photos)

### Output
- `images/` populated with curated, print-ready photos
- Each chapter has 2–5 placed images with captions

---

## WS2: FAMILY-DATA — Collect Contributions
**Owner:** Greg (human task — sending templates, collecting responses)
**Effort:** Ongoing over 2–3 weeks

### What
- Send `contributions/*.md` templates to family members
- Chase responses (email, text, phone calls)
- Optionally set up a JotForm (Rich can help) or Google Form as alternative intake
- As responses come in, save them to `contributions/responses/`

### Files Owned
```
contributions/**/*
```

### Depends On
- Templates already created (done)
- Contact info for: Yvonne, Rich, [other son], [daughter], grandkids, Kathy, Mike Jr., Mary Ann, Michael Sr., veterans

### Output
- Raw responses in `contributions/responses/{person-name}.md`
- Greg triages which responses go into which chapters

### Handoff To
- WS5 (Chapter Polish) weaves responses into narrative

---

## WS3: VIZ — R Family Tree & Interactive Timeline
**Owner:** Claude instance (R-focused)
**Effort:** 1–2 sessions

### What
- Build R-based family tree using `DiagrammeR` (static/PDF) and `visNetwork` (interactive/HTML)
- Build interactive timeline using R (`timevis` or `plotly`) for HTML, formatted table for PDF
- Both read from existing data files, render via `{r}` code blocks in Quarto

### Files Owned
```
appendices/family-tree.qmd    (full rewrite OK)
appendices/timeline.qmd       (full rewrite OK)
src/family_tree_r.R            (new — R equivalent of family_tree.py)
```

### Files It Reads (no edits)
```
data/family.json
docs/timeline.csv
```

### Depends On
- R packages: `DiagrammeR`, `visNetwork`, `timevis` or `plotly`, `jsonlite`
- `data/family.json` and `docs/timeline.csv` stable

### Output
- Interactive family tree in HTML book (clickable nodes, hover details)
- Interactive timeline in HTML book (scroll, hover)
- Static equivalents in PDF

---

## WS4: PRINT — PDF Production & Blurb Prep
**Owner:** Claude instance
**Effort:** 1–2 sessions (after content is mostly stable)

### What
- Configure Blurb-specific page geometry (8×10" or 10×8" + bleed)
- Tune PDF rendering: page breaks, orphans/widows, image placement
- `keep-tex: true` for LaTeX-level fixes
- Review print proof, adjust
- Set up a Blurb-ready PDF export profile in `_quarto.yml`

### Files Owned
```
_quarto.yml          (PDF format section only)
css/tribute-print.css (new — print-specific overrides)
_quarto-blurb.yml    (new — alternate config for Blurb dimensions)
```

### Depends On
- Chapters mostly finalized (text + photos placed)
- Run AFTER WS1 (photos) and WS5 (polish) are substantially done

### Output
- Print-ready PDF at Blurb dimensions
- `_quarto-blurb.yml` for final production render

---

## WS5: POLISH — Chapter Content Enrichment
**Owner:** Claude instance
**Effort:** 2–3 sessions

### What
- Weave family contributions (from WS2) into chapter narratives
- Transform third-person biography → first-person autobiography where Vic/Yvonne provided quotes
- Enrich thin chapters (especially Ch5-Restaurant, Ch9-Voices) with collected material
- Add "In His Own Words" / "In Her Own Words" sidebar blocks
- Final editorial pass: tone, flow, consistency

### Files Owned
```
chapters/*.qmd        (all chapter files — narrative text)
index.qmd
```

### Depends On
- Contributions from WS2 (at least some responses in)
- Photos from WS1 placed (so polish pass doesn't conflict with image placement)

### Output
- Chapters enriched with family voices
- Biography → autobiography transformation where material allows
- All `[OWNER INPUT NEEDED]` markers either filled or clearly flagged as "still waiting"

---

## WS6: DEPLOY — GitHub Pages & Sharing
**Owner:** Greg + Claude instance
**Effort:** 1 session

### What
- Push repo to GitHub (if not already)
- Set up GitHub Actions for Quarto → GitHub Pages auto-deploy
- Configure custom domain (optional)
- Mobile-responsive testing
- Share URL with family (for contribution solicitation and eventual reading)

### Files Owned
```
.github/workflows/publish.yml  (new)
.nojekyll                       (new)
```

### Depends On
- Book renders cleanly to HTML (done ✓)
- Repo on GitHub

### Output
- Live URL family can visit
- Auto-deploys on push to main

---

## Execution Order & Dependencies

```
Week 1:  WS2 (send templates)  |  WS3 (R viz)  |  WS6 (deploy)
         ─────────────────────────────────────────────────────────
         All three are independent. Start immediately.

Week 2:  WS1 (photos)  |  WS2 (chase responses)  |  WS3 (finish)
         ─────────────────────────────────────────────────────────
         WS1 needs Greg to review Lit-Project photos.
         WS3 should be done by end of Week 2.

Week 3:  WS5 (polish with contributions)  |  WS1 (finish photos)
         ─────────────────────────────────────────────────────────
         WS5 starts once some WS2 responses are in.

Week 4:  WS4 (print production)  |  WS5 (final pass)
         ─────────────────────────────────────────────────────────
         WS4 runs last, once content is stable.
         Order proof from Blurb (3–5 day shipping).
```

---

## How to Launch a Workstream

Open a new Positron terminal. Start Claude Code. Say:

> "Read WORKSTREAMS.md. I'm working on WS[N]. Read the files you own and get started."

Each instance sees the same repo but only touches its own files.

---

## Conflict Rules

1. **Never edit a file you don't own** without coordinating
2. **Chapters are owned by WS5** (polish) — WS1 (photos) only adds image blocks at marked points
3. **`_quarto.yml` has shared ownership** — WS4 owns the PDF section, WS3 can add to the HTML section if needed, coordinate via comments
4. **`data/` and `docs/` are read-only** for all workstreams — edits go through the main session
5. **Git:** each workstream works on its own branch if possible, or commits with `[WS#]` prefix
