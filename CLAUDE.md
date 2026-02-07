# CLAUDE.md — dads80th

Victor Cicconetti's 80th birthday celebration content + family dossier research.
Inherits from `../CLAUDE.md` (global).

## Project Context

**Owner:** Greg Cicconetti
**Purpose:** Create meaningful 80th birthday celebration content (tribute document, family history, event materials). Secondary: feed family dossier data to Lit-Project autobiography.
**Timeline:** TIME-SENSITIVE — Victor born ~March 1946 → 80th birthday ~March 2026.

## Tech Stack

- **Python 3.11+** for family tree visualization and document generation
- **Quarto** for birthday tribute document and family history compilation
- **Data sources:** Family dossiers (already gathered), Lit-Project sources, public records

## Project-Specific Rules

- Family dossier data contains sensitive personal information. Never output to public/shared locations.
- Content should be celebratory and respectful — this is a family tribute.
- Cross-reference with `../Lit-Project/` for shared family data. Dossiers are canonical here; Lit-Project references them.

## Phases

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Organize dossier data, define deliverables | Current |
| 1 | Birthday tribute document (narrative + family tree) | Next |
| 2 | Event materials (photo montage, timeline, readings) | Planned |
| 3 | Lit-Project integration (export relevant data) | Future |

## Gmail Sources

Gmail data mined via gmail-organizer MCP (2026-02-06). Full results in `docs/gmail-intel.md`.

- **Vic direct:** `from:viccicconetti@yahoo.com OR to:viccicconetti@yahoo.com` (~50 msgs, 2014–2026)
- **Vic subject:** `subject:victor OR subject:vic` (birthday events, voicemails, tribute coordination)
- **Tribute thread:** `subject:"sshhh its a surprise"` (80th tribute book invitation, Feb 2026)
- **75th birthday:** `subject:"Victor's Birthday Video"` + JotForm confirmations (Mar 2021)
- **Secondary email:** medflyboy@gmail.com (Google Chat transcripts, 2012)
- **Last Gmail sync:** 2026-02-06

### Key Assets Identified
- Family photo attachment (P1020477.JPG, Sep 2017) — retrievable via download_attachment
- Research Fellow promotion announcement (Jul 2018) — full career summary
- Vic's "My party" thank-you email (Apr 2021) — his voice in his own words
- 75th birthday video (Vimeo link) — Kathy Pacifico / Keri Urban production

## Key Commands

```bash
quarto render reports/templates/tribute.qmd  # Render birthday tribute
```
