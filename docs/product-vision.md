# Product Vision: Living Biography Platform

**Date:** 2026-02-08
**Context:** Emerged during dads80th 80th birthday sprint session
**Status:** Vision captured; prototype is the Vic book; commercialization deferred

---

## The Concept

A **living family biography** that transforms from a researched narrative into a family-authored autobiography over time.

### Three Layers

1. **"We Heard..."** — The researched biography. Third person, factual, based on public records, emails, census data, dossiers. Explicitly presented as a *first draft* that invites correction.

2. **"Your Turn"** — Warm, specific prompts addressed to individual family members by name. Embedded in the narrative at the point of relevance. Designed to trigger recall and make people *want* to respond.

3. **"In Their Own Words"** — As contributions come in, the narrative evolves. Third person becomes first person. Biography becomes autobiography. Gaps get filled. Facts get corrected.

### The Book IS the Interface

The product isn't a separate app. The book itself is the interface:
- Reader browses chapters on a website (Quarto → GitHub Pages)
- At contextually relevant points, they see prompts and submission forms
- They can contribute via text, photos, or **voice recordings** (transcribed via Whisper or similar)
- Submissions queue up for LLM-assisted integration
- An **editor-in-chief** (the organizer) reviews diffs and approves before publication
- The book updates on a cadence (weekly, or on-demand)

### "Correct the Record"

Fact-checking as participation. Every claim gets three simple choices:
- **TRUE** — Yes, that's right
- **FALSE** — No, that's wrong
- **I DON'T KNOW** — Not sure / don't remember

Each block of related claims gets a single text box to clarify — "Set the record straight." These blocks are embedded **inline throughout chapters** (not just in an appendix), so the reader encounters them naturally while reading.

### "Tell Us a Story"

Story solicitation prompts woven throughout the narrative — fun, specific, designed to trigger recall:
- *"What kind of trouble did you get into on the block?"*
- *"Who made the first move? Be honest."*
- *"What's your Atlantic City system?"*

The prompts are playful, not clinical. They invite the kind of stories people tell at the dinner table — not interview answers.

---

## User Roles & Design Philosophy

### Two User Types

1. **The Subject + Significant Other / Primary Caregiver** — The primary users. The person whose story is being told, and whoever helps them navigate. They:
   - Read their own story (Reminiscence Mode)
   - Respond to "Correct the Record" claims (TRUE/FALSE/I DON'T KNOW)
   - Tell stories prompted by "Tell Us a Story" blocks
   - Browse photos and timeline

2. **Relatives & Friends** — Contributors. They:
   - Read the story of someone they love
   - Add their own perspective via story prompts and contributions
   - Fact-check claims they have knowledge of
   - Submit tribute messages, photos, voice recordings

### Design for Older Users

The interface MUST work for people in their 70s and 80s:

- **Large, readable text** — minimum 18px body, generous line height
- **High contrast** — dark text on light backgrounds, no low-contrast gray-on-gray
- **Simple navigation** — chapter list always visible, "Next Chapter" / "Previous Chapter" buttons prominent, no hamburger menus
- **One action per screen** — don't ask them to do multiple things at once
- **Obvious interactive elements** — TRUE/FALSE/I DON'T KNOW as large, tappable buttons (not tiny checkboxes)
- **Text boxes with generous space** — big enough that they don't feel constrained
- **Voice-first alternative** — for users who can't type easily, a "Record Your Answer" button (transcribed via Whisper)
- **No login required** — family link with token, no accounts to manage
- **Works on iPad** — many older users browse on tablets
- **Minimal scrolling per interaction** — fact-check + text box should fit in one viewport
- **Warm, personal visual design** — feels like a family album, not a medical form

### Caregiver Considerations

- The caregiver (spouse, adult child) may navigate for the subject
- "Read to me" mode (text-to-speech) for subjects with vision issues
- Session memory — pick up where you left off
- No time pressure — save progress automatically
- Gentle tone throughout — never feels like a test

---

## The Alzheimer's / Memory Preservation Angle

### Two Modes, One Platform

**Reminiscence Mode (for the person):**
- The person reads their own story
- Prompts trigger recall: "Do you remember the restaurant? What was the signature dish?"
- Responses are captured — every visit is gentle cognitive exercise
- The book *knows them* and meets them where they are

**Preservation Mode (for the family):**
- The family is racing the clock
- They submit questions, record conversations, feed in photos
- The platform captures everything and structures it into narrative
- When memories fade, the book holds what was saved

### Why This Matters

- **Urgency:** Stories lost to Alzheimer's are lost forever. This captures them while people can still speak.
- **Engagement:** Reading your own life story is a known reminiscence therapy technique.
- **Voice-first:** Voice input (transcribed to text) lowers the barrier for elderly users who can't type easily.
- **Legacy:** The artifact outlasts the memory. Grandchildren can read their grandparent's stories in their own words.

---

## Gamification: Progress Visualization

The primary gamification mechanic is **watching the book come alive**. No points, no scores, no competition — just the visible, tangible growth of a family's story.

### Core Metrics (visible to all users)

| Metric | What It Shows | Example |
|--------|--------------|---------|
| **Book Completion** | Overall % of the story that's been told | *"Vic's story is 64% told"* |
| **Chapter Health** | Per-chapter progress bar — how rich is each chapter? | Ch5 at 12% (almost empty), Ch1 at 85% (well-told) |
| **Claims Verified** | How many TRUE/FALSE/I DON'T KNOW have been answered | *"47 of 67 facts checked"* |
| **Own Words** | % of narrative that's now first-person (autobiography vs. biography) | *"38% of the book is now in the family's own words"* |
| **Stories Collected** | Count of stories submitted across all chapters | *"The family has shared 31 stories so far"* |
| **Contributors** | Who has contributed, to which chapters | Contributor avatars on each chapter header |
| **Gaps Remaining** | Named gaps that still need filling | *"3 biggest gaps: the restaurant, VVA founding year, courtship story"* |

### How Progress Drives Engagement

- **The homepage shows the book growing.** Each visit, something may have changed — a new story, a corrected fact, a photo. The book is alive.
- **Empty chapters are visually obvious.** Ch5 (restaurant) at 12% with a thin progress bar creates natural pull — "we need to fill this."
- **Contributions trigger visible change.** When you submit a story, the progress bar moves. When you verify a claim, the counter ticks up. Immediate feedback.
- **The biography → autobiography meter is the north star.** The ultimate goal is 100% "In Their Own Words." Every contribution moves the needle.

### Subject-Specific Progress (Reminiscence Mode)

- *"Memories shared: 23"* — how many stories the subject has told
- *"Memory of the Day"* — a random completed story resurfaced for re-reading (therapeutic)
- *"New since your last visit"* — highlights what family added since last session
- **No failures, no pressure** — every interaction is progress, every visit is a win

### Contributor-Specific Progress

- *"You've contributed to 4 of 10 chapters"* — personal progress toward "Family Historian"
- *"Your story about the restaurant unlocked new content in Chapter 5"* — contributions have visible impact
- *"Chapter 6 needs your help — only 2 of 4 claims verified"* — gentle direction, not guilt

### What We Explicitly Avoid

- **No scores or points** — this is a family project, not a game
- **No competition** — leaderboards create tension in families
- **No streaks or guilt** — "You missed 3 days!" is harmful, especially for Alzheimer's users
- **No time pressure** — the book waits for you, always
- **No complexity** — progress bars, counters, contributor names. That's it.

### MVP Implementation (Vic's Book)

For the Quarto prototype, progress visualization can be approximated with:
- Static progress bars in CSS (updated manually per render cycle)
- A "Book Status" section on the homepage showing chapter completion
- Contributor acknowledgment on each chapter page
- Claims-verified counters (hardcoded, updated as responses come in)

Future product: JavaScript-driven real-time counters, database-backed progress tracking, push notifications ("Rich just added a story to Chapter 7!").

---

## Architecture (Conceptual)

```
[Quarto Website]  ←  renders from  ←  [Chapter .qmd files]
       ↑                                       ↑
       |                                [LLM Revision Engine]
  [Reader/Family]                              ↑
       |                              [Editor-in-Chief Approval]
       ↓                                       ↑
  [Submission Layer]  →  [Queue]  →  [LLM Draft Integration]
  (text, voice, photo)
       ↓
  [Whisper Transcription] (for voice)
```

### MVP Stack (for Vic's book)
- **Rendering:** Quarto → HTML (GitHub Pages)
- **Submissions:** Google Form or JotForm (per chapter), or markdown templates
- **Transcription:** Manual for now; Whisper API later
- **Integration:** Claude Code session (Greg runs it manually)
- **Approval:** Greg reviews and commits

### Future Stack (product)
- **Frontend:** Quarto or Next.js with embedded submission UI
- **Submissions:** Database-backed (Supabase, Firebase, or similar)
- **Transcription:** Whisper API (automatic)
- **Integration:** Scheduled Claude API pipeline
- **Approval:** Web-based editorial dashboard
- **Hosting:** Vercel / Netlify / GitHub Pages

---

## Broader Pattern: The Eidetic Engine

This product is one instance of a pattern Greg is applying across domains:

| Domain | Data | Engine | Output |
|--------|------|--------|--------|
| **Family legacy** | Dossiers, emails, records, photos, oral history | Biographical narrative engine | Living biography (dads80th) |
| **Finance** | Market data, portfolio, fundamentals | Decision framework engine | gfinance2 |
| **Autobiography** | Life experiences, interviews, dossiers | Autobiography engine | Lit-Project |
| **Consulting** | Client data, discovery interviews | Optimization engine | llc-consulting |

Common thread: **rich, heterogeneous data that most people can't synthesize → an engine that structures it into a first draft → infrastructure for continuous enrichment → a living artifact.**

---

## Commercialization (Deferred)

### Approach
Personal first, then maybe. The Vic book is the proof of concept. If family members actually engage, contribute, and the book transforms, the model is validated.

### Potential Buyers
- Adult children organizing milestone events (birthdays, anniversaries, memorials)
- Family historians
- Alzheimer's / dementia caregivers
- Memory care facilities (as a therapeutic tool)
- Funeral homes (as a pre-need service)

### Pricing Models (speculative)
- One-time setup fee + hosting
- Subscription (ongoing LLM revision + hosting)
- White-label for institutions (care facilities, funeral homes)

### Cost Analysis (required per CLAUDE.md before building)
Deferred until commercialization decision. The Vic prototype runs on Claude Code Max (covered) + free GitHub Pages hosting.

---

## Next Steps

1. **Ship the Vic book** — 80th birthday sprint (4 weeks)
2. **Collect family contributions** — validate the engagement model
3. **Deploy to GitHub Pages** — make it accessible
4. **Evaluate** — did it work? Did family engage? Did the book improve?
5. **Decide** — is this a product, or just a great family project?
