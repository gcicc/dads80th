#!/usr/bin/env python3
"""
Generate timeline HTML from timeline_events.json
Reads from data/timeline_events.json and outputs HTML suitable for Quarto
Usage: python scripts/generate_timeline.py
"""

import json
from pathlib import Path
from datetime import datetime

def load_json(filepath):
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def group_events_by_decade(events):
    """Group events by decade (1940s, 1950s, etc.)."""
    grouped = {}
    for event in events:
        if event.get('date'):
            year = int(event['date'].split('-')[0])
        elif event.get('year_range'):
            year = event['year_range'][0]
        else:
            year = None

        if year:
            decade = (year // 10) * 10
            decade_label = f"{decade}s"
        else:
            decade_label = "undated"

        if decade_label not in grouped:
            grouped[decade_label] = []
        grouped[decade_label].append(event)

    return grouped

def generate_timeline_visual_html(data):
    """Generate HTML for visual timeline."""
    def sort_key(e):
        if e.get('date'):
            return int(e['date'].split('-')[0])
        elif e.get('year_range'):
            return e['year_range'][0]
        else:
            return 9999

    events = sorted(data['events'], key=sort_key)
    grouped = group_events_by_decade(events)

    html_parts = []
    html_parts.append('<div class="timeline-visual">\n')

    for decade in sorted(grouped.keys(), key=lambda x: int(x[:-1]) if x != 'undated' else 9999):
        if decade != 'undated':
            html_parts.append(f'<div class="timeline-decade">{decade}</div>\n')

        for event in grouped[decade]:
            year_display = event.get('year_display', 'Unknown')
            icon = event.get('icon', '📍')
            description = event.get('description', '')
            event_id = event.get('id', '')

            html_parts.append(f'''<div class="timeline-card" data-year="{year_display}" data-event="{event_id}">
  <div class="timeline-year">{year_display}</div>
  <div class="timeline-icon">{icon}</div>
  <div class="timeline-text">{description}</div>
</div>
''')

    html_parts.append('</div>\n')
    return ''.join(html_parts)

def generate_timeline_table_html(data):
    """Generate markdown table for timeline (for PDF and editing)."""
    def sort_key(e):
        if e.get('date'):
            return int(e['date'].split('-')[0])
        elif e.get('year_range'):
            return e['year_range'][0]
        else:
            return 9999

    events = sorted(data['events'], key=sort_key)

    lines = []
    lines.append('| Year | Event | Notes |')
    lines.append('|------|-------|-------|')

    for event in events:
        year = event.get('year_display', 'Unknown')
        title = event.get('title', '')
        description = event.get('description', '')

        # For table, truncate long descriptions
        desc_short = description[:100] + '...' if len(description) > 100 else description

        lines.append(f'| {year} | {title} | {desc_short} |')

    return '\n'.join(lines)

def extract_undated_events(data):
    """Extract events that need dates filled in."""
    undated = [e for e in data['events'] if not e.get('date') and not e.get('year_range')]

    if not undated:
        return None

    lines = []
    lines.append('| Event | Year? | Source |')
    lines.append('|-------|:-----:|:------:|')

    for event in undated:
        title = event.get('title', '')
        sources = event.get('sources', [])
        source_text = sources[0].get('description', '') if sources else '[UNKNOWN]'
        lines.append(f'| {title} | | {source_text} |')

    return '\n'.join(lines)

def print_evidence_summary(data):
    """Print a summary of what evidence needs to be collected."""
    print("\n" + "="*70)
    print("EVIDENCE NEEDED FOR TIMELINE")
    print("="*70 + "\n")

    missing_evidence = []
    for event in data['events']:
        for source in event.get('sources', []):
            if '[NEEDED' in source.get('evidence', '') or '[COLLECT' in source.get('evidence', ''):
                missing_evidence.append({
                    'event': event.get('title', ''),
                    'source_type': source.get('type', ''),
                    'need': source.get('evidence', '')
                })

    for item in missing_evidence:
        print(f"[*] {item['event']}")
        print(f"    Type: {item['source_type']}")
        print(f"    Need: {item['need']}\n")

    print(f"Total items needing evidence: {len(missing_evidence)}")

def main():
    """Generate timeline outputs."""
    project_root = Path(__file__).parent.parent

    # Load data
    timeline_data = load_json(project_root / 'data' / 'timeline_events.json')

    # Generate HTML
    print("Generating timeline HTML...")
    visual_html = generate_timeline_visual_html(timeline_data)

    # Print stats
    print(f"[OK] Timeline has {len(timeline_data['events'])} events")
    print(f"[OK] Visual timeline HTML generated ({len(visual_html)} chars)")

    # Check for missing evidence
    print_evidence_summary(timeline_data)

    # Suggest next steps
    print("\n" + "="*70)
    print("NEXT STEPS")
    print("="*70)
    print("\n1. Review timeline_events.json and add missing dates/evidence")
    print("2. Update Quarto timeline.qmd to read from JSON (instead of hardcoded HTML)")
    print("3. Add new events as discovered by running:")
    print("   - Copy/paste a new event object into timeline_events.json")
    print("   - Include evidence fields with sources")
    print("   - Re-render the book: quarto render")
    print()

if __name__ == '__main__':
    main()
