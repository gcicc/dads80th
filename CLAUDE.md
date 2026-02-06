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

## Key Commands

```bash
quarto render reports/templates/tribute.qmd  # Render birthday tribute
```
