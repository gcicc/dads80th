# Data Management — Timeline & Trips

## Overview

The timeline and trips are now **data-driven**. Instead of hardcoding HTML in Quarto files, all events and trips are stored in JSON data files. This makes it easy to:

- **Add new events** as you discover them
- **Track evidence** for each event (photos, emails, documents, etc.)
- **Fill in missing information** systematically
- **Integrate with the lifemap** showing where events happened

---

## File Structure

```
data/
├── addresses.json          # Addresses and geographic landmarks (existing)
├── timeline_events.json    # All major life events (NEW)
├── trips.json             # Travel and vacations (NEW)
└── family.json            # Family tree data (existing)

scripts/
└── generate_timeline.py   # Python script to analyze timeline (NEW)
```

---

## Timeline Events (`data/timeline_events.json`)

### What goes in timeline_events.json?

**Major life milestones:**
- Births and deaths
- Marriages
- Career changes and retirements
- Relocations
- Military service
- Community achievements
- Family celebrations

### Event Structure

```json
{
  "id": "event_unique_id",
  "date": "1946-03-29",                    // ISO date if you have it
  "year_display": "~1946",                 // How to display (can be ~, range, etc.)
  "year_range": [1974, 1975],              // If unsure, give range
  "title": "Event Title",
  "description": "Longer description here...",
  "type": "birth|death|marriage|career|relocation|military|community|celebration|property|business",
  "location": "City, State",
  "phase": "childhood|military|early-marriage|shore-years|retirement|golden",
  "icon": "🎂",
  "sources": [
    {
      "type": "birth_record|military_record|news_article|family_memory|correspondence|photo|...",
      "description": "What this source is",
      "evidence": "Where it's located or what needs to be done"
    }
  ]
}
```

### How to Add a New Event

**Step 1:** Open `data/timeline_events.json`

**Step 2:** Add a new object to the `events` array:

```json
{
  "id": "graduation",
  "date": "1968",
  "year_display": "1968",
  "title": "Graduates from [School]",
  "description": "Victor graduates from [School Name].",
  "type": "career",
  "location": "[City, State]",
  "phase": "early-marriage",
  "icon": "🎓",
  "sources": [
    {
      "type": "family_memory",
      "description": "Victor's recollection",
      "evidence": "[COLLECT: Do you have your diploma? What was that like?]"
    }
  ]
}
```

**Step 3:** Run the analysis script to check your data:

```bash
python scripts/generate_timeline.py
```

This will show:
- Total event count
- What evidence is still missing
- Any formatting errors

---

## Trips (`data/trips.json`)

### What goes in trips.json?

**Travel and vacation records:**
- Military deployments
- Vacations
- Visits to family
- Business trips
- Special trips (honeymoon, pilgrimage, etc.)

### Trip Structure

```json
{
  "id": "italy_trip",
  "date_start": "2010-06-01",              // Trip start date (optional)
  "date_end": "2010-06-15",                // Trip end date (optional)
  "year_display": "Summer 2010",           // How to display
  "title": "Trip to Italy",
  "description": "Victor and Yvonne visit Italy...",
  "type": "vacation|military_deployment|business_trip|family_visit|pilgrimage|wedding|event|other",
  "location_start": "Bayonne, NJ",
  "location_end": "Italy",
  "phase": "retirement",                   // Which life phase
  "icon": "🇮🇹",
  "evidence": [
    {
      "type": "photo|email|correspondence|news_article|family_memory|...",
      "description": "Photo from the trip",
      "source": "Family photo albums or Lit-Project/images/"
    },
    {
      "type": "family_memory",
      "description": "Trip stories and memories",
      "source": "Vic or Yvonne"
    }
  ]
}
```

### How to Add a Trip

**Example: Adding a Caribbean Cruise**

```json
{
  "id": "caribbean_cruise_2015",
  "date_start": "2015-03-01",
  "date_end": "2015-03-08",
  "year_display": "March 2015",
  "title": "Caribbean Cruise",
  "description": "Victor and Yvonne take a week-long Caribbean cruise.",
  "type": "vacation",
  "location_start": "New Jersey",
  "location_end": "Caribbean",
  "phase": "retirement",
  "icon": "🚢",
  "evidence": [
    {
      "type": "photo",
      "description": "Cruise ship photos",
      "source": "P1020477.JPG or similar — check Gmail attachment P1020477"
    },
    {
      "type": "family_memory",
      "description": "Memories from the trip",
      "source": "[COLLECT: What was your favorite port? Any memorable moments?]"
    }
  ]
}
```

---

## Integrating Photos & Evidence

### Photo Evidence

When you have a photo of an event or trip:

1. **Save it** to `images/{era}/` (e.g., `images/retirement/cruise-2015.jpg`)
2. **Link it** in the `evidence` field:
   ```json
   {
     "type": "photo",
     "description": "Caribbean cruise photo",
     "source": "images/retirement/cruise-2015.jpg"
   }
   ```

### Email or Letter Evidence

If you have an email or letter that confirms an event:

```json
{
  "type": "correspondence",
  "description": "Email from Yvonne about the trip",
  "source": "docs/emails/caribbean-cruise-2015.txt"
}
```

### News Article Evidence

```json
{
  "type": "news_article",
  "description": "Asbury Park Press 40th anniversary announcement",
  "source": "Red Bank Register (1987) — 'Man with Many Missions' profile"
}
```

---

## Workflow: Adding Evidence as You Collect It

### When you find something new...

**Example: You find Victor's discharge papers**

1. Open `data/timeline_events.json`
2. Search for `"id": "honorable_discharge"`
3. Update the `evidence` field:

```json
"sources": [
  {
    "type": "military_record",
    "description": "Discharge papers document this deployment",
    "evidence": "[FOUND: Scanned and saved as docs/military/discharge-1969.pdf]"
  }
]
```

4. Run the script to verify:
```bash
python scripts/generate_timeline.py
```

The missing evidence count should decrease.

---

## Filling In Undated Events

Some events have dates, but others don't. To find undated events:

1. Run: `python scripts/generate_timeline.py`
2. Look for events with `"date": null` and `"year_range": null`
3. Collect the information from Vic, Yvonne, or family records
4. Update the JSON with the date or range

**Example:**

Before:
```json
{
  "id": "bistro_founded",
  "date": null,
  "year_display": "[YEAR?]",
  "title": "Co-found Bistro-by-the-Sea"
}
```

After (when you learn it was ~1985–1995):
```json
{
  "id": "bistro_founded",
  "date": "1985-01-01",
  "year_display": "~1985",
  "year_range": [1985, 1995],
  "title": "Co-found Bistro-by-the-Sea"
}
```

---

## Rendering the Book

Once you've updated the timeline or trips data:

```bash
quarto render --to html
```

The Quarto files will read from the JSON and regenerate the timeline and lifemap.

---

## Using the Lifemap with Timeline Data

The `appendices/lifemap.qmd` currently shows all addresses and landmarks from `data/addresses.json`.

**Future enhancement:** Add trip markers to the lifemap showing:
- Where trips started and ended
- Icons for different trip types (vacation, military, business, etc.)
- Popup information with photos and stories

---

## Tracking Missing Information

The Python script summarizes what's still missing. As of 2026-02-19:

**18 items need evidence or collection:**
- Birth/death records (certificates, obituaries)
- Property records (deeds, mortgages)
- Family memories (stories, dates, details)
- Photos and correspondence

**To see the current missing list:**
```bash
python scripts/generate_timeline.py | grep "^\[*\]"
```

---

## Checklist: Adding New Information

- [ ] Find the event in `timeline_events.json` or create a new one
- [ ] Add or update the date (if you have it)
- [ ] Add source information
- [ ] Link to any photos or documents
- [ ] Update the evidence field with what still needs to be done
- [ ] Run `python scripts/generate_timeline.py` to verify
- [ ] Commit to git with a message like: "Add evidence for [event]"
- [ ] Render the book: `quarto render --to html`

---

## Questions?

If you're unsure about the format, look at existing events in `timeline_events.json` and copy the structure.

For dates: Use ISO format (`YYYY-MM-DD`) if exact, or ranges (`"year_range": [1974, 1975]`) if approximate.

For locations: Use standard U.S. format (`"City, State"`) or full addresses for clarity.
