"""
family_tree.py — Generate a visual family tree for Victor R. Cicconetti's 80th birthday.

Reads data/family.json and produces a Graphviz DOT rendering in PDF and PNG formats.
Output files are written to reports/family_tree.pdf and reports/family_tree.png.

Usage:
    python src/family_tree.py
    python src/family_tree.py --output-dir reports
    python src/family_tree.py --format png
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import graphviz


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

COLORS = {
    "male": "#B3D4FC",       # light blue
    "female": "#F8C8DC",     # light pink
    "unknown": "#D3D3D3",    # light gray (gaps)
    "deceased_male": "#7BA7D9",
    "deceased_female": "#E8A0B5",
    "deceased_unknown": "#A9A9A9",
    "marriage_edge": "#8B0000",  # dark red
    "child_edge": "#2F4F4F",     # dark slate
}

FONT = "Helvetica"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "family.json"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "reports"


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_family_data(path: Path = DATA_FILE) -> dict:
    """Load the family.json data file."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_people_lookup(data: dict) -> dict[str, dict]:
    """Return a dict mapping person id -> person record."""
    return {p["id"]: p for p in data["people"]}


# ---------------------------------------------------------------------------
# Node helpers
# ---------------------------------------------------------------------------

def _life_span(person: dict) -> str:
    """Return a string like '1946 - 1980' or 'b. 1946' or '?'."""
    b = person.get("birth_year")
    d = person.get("death_year")
    if b and d:
        return f"{b}\u2013{d}"
    if b:
        return f"b. {b}"
    if d:
        return f"d. {d}"
    return ""


def _node_color(person: dict) -> str:
    """Pick fill color based on gender and alive/deceased status."""
    gender = person.get("gender")
    deceased = person.get("death_year") is not None

    if gender == "male":
        return COLORS["deceased_male"] if deceased else COLORS["male"]
    if gender == "female":
        return COLORS["deceased_female"] if deceased else COLORS["female"]
    return COLORS["deceased_unknown"] if deceased else COLORS["unknown"]


def _display_name(person: dict) -> str:
    """Build a multi-line label for the node."""
    name = person.get("full_name", "?")
    nickname = person.get("nickname")
    maiden = person.get("maiden_name")

    parts = []
    if nickname:
        parts.append(f'"{nickname}"')

    label_line1 = name
    if maiden:
        label_line1 += f"\n(nee {maiden})"

    lifespan = _life_span(person)
    lines = [label_line1]
    if parts:
        lines[0] = f"{name}  {' '.join(parts)}"
        if maiden:
            lines.append(f"(nee {maiden})")
    elif maiden:
        pass  # already appended above
    if lifespan:
        lines.append(lifespan)

    return "\n".join(lines)


def _is_gap(person: dict) -> bool:
    """Return True if this person is an unknown/gap placeholder."""
    name = person.get("full_name", "")
    return name.startswith("?") or "[GAP]" in person.get("notes", "")


# ---------------------------------------------------------------------------
# Graph construction
# ---------------------------------------------------------------------------

def build_graph(data: dict) -> graphviz.Digraph:
    """Construct the Graphviz Digraph representing the family tree."""
    people = build_people_lookup(data)

    dot = graphviz.Digraph(
        name="CicconettiFamilyTree",
        comment="Victor R. Cicconetti Family Tree - 80th Birthday",
        format="pdf",
    )

    # Global attributes
    dot.attr(
        rankdir="TB",
        splines="ortho",
        nodesep="0.6",
        ranksep="1.0",
        fontname=FONT,
        label="The Cicconetti Family\nVictor's 80th Birthday - March 2026",
        labelloc="t",
        fontsize="22",
        fontcolor="#333333",
        bgcolor="white",
    )

    dot.attr("node", shape="box", style="filled,rounded", fontname=FONT, fontsize="11")
    dot.attr("edge", fontname=FONT, fontsize="9")

    # -----------------------------------------------------------------------
    # Add person nodes
    # -----------------------------------------------------------------------
    for pid, person in people.items():
        color = _node_color(person)
        label = _display_name(person)
        border = "dashed" if _is_gap(person) else "solid"
        peripheries = "1"

        dot.node(
            pid,
            label=label,
            fillcolor=color,
            color="#555555",
            style=f"filled,rounded,{border}",
            peripheries=peripheries,
        )

    # -----------------------------------------------------------------------
    # Marriage nodes (invisible join points) and edges
    # -----------------------------------------------------------------------
    for marriage in data.get("marriages", []):
        mid = marriage["id"]
        s1 = marriage.get("spouse1")
        s2 = marriage.get("spouse2")
        date = marriage.get("date", "")
        location = marriage.get("location", "")

        if not s1:
            continue

        marriage_label = ""
        if date:
            marriage_label = f"m. {date}"
        if location:
            marriage_label += f"\n{location}" if marriage_label else location

        # Create invisible marriage point node
        dot.node(
            mid,
            label=marriage_label if marriage_label else "m.",
            shape="diamond",
            width="0.3",
            height="0.2",
            fillcolor="#FFFACD",
            style="filled",
            fontsize="8",
        )

        # Edges from spouses to marriage point
        if s1 and s1 in people:
            dot.edge(s1, mid, dir="none", color=COLORS["marriage_edge"], penwidth="2")
        if s2 and s2 in people:
            dot.edge(s2, mid, dir="none", color=COLORS["marriage_edge"], penwidth="2")

    # -----------------------------------------------------------------------
    # Parent-child edges
    # -----------------------------------------------------------------------
    # Group children by parent pair
    parent_pairs: dict[tuple[str, str], list[str]] = {}
    for rel in data.get("parent_child", []):
        parent_id = rel["parent"]
        child_id = rel["child"]
        # Find matching marriage for this parent
        for marriage in data.get("marriages", []):
            s1 = marriage.get("spouse1")
            s2 = marriage.get("spouse2")
            if parent_id in (s1, s2):
                pair_key = (s1, s2) if s1 else (parent_id, None)
                if child_id not in parent_pairs.get(pair_key, []):
                    parent_pairs.setdefault(pair_key, []).append(child_id)
                break

    # Draw edges from marriage nodes to children
    drawn_children: set[str] = set()
    for marriage in data.get("marriages", []):
        mid = marriage["id"]
        s1 = marriage.get("spouse1")
        s2 = marriage.get("spouse2")
        pair_key = (s1, s2)

        children = parent_pairs.get(pair_key, [])
        for child_id in children:
            if child_id not in drawn_children and child_id in people:
                dot.edge(
                    mid,
                    child_id,
                    color=COLORS["child_edge"],
                    penwidth="1.2",
                )
                drawn_children.add(child_id)

    # -----------------------------------------------------------------------
    # Rank grouping by generation
    # -----------------------------------------------------------------------
    generations: dict[int, list[str]] = {}
    for pid, person in people.items():
        gen = person.get("generation", 0)
        generations.setdefault(gen, []).append(pid)

    for gen in sorted(generations):
        with dot.subgraph() as s:
            s.attr(rank="same")
            for pid in generations[gen]:
                s.node(pid)

    return dot


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_tree(
    data: dict,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    formats: list[str] | None = None,
    filename: str = "family_tree",
) -> list[Path]:
    """Build and render the family tree. Returns list of output file paths."""
    if formats is None:
        formats = ["pdf", "png"]

    output_dir.mkdir(parents=True, exist_ok=True)
    dot = build_graph(data)

    outputs = []
    for fmt in formats:
        dot.format = fmt
        outpath = dot.render(
            filename=filename,
            directory=str(output_dir),
            cleanup=True,
        )
        outputs.append(Path(outpath))
        print(f"  Rendered: {outpath}")

    # Also save the DOT source for inspection
    dot_path = output_dir / f"{filename}.dot"
    dot_path.write_text(dot.source, encoding="utf-8")
    outputs.append(dot_path)
    print(f"  DOT source: {dot_path}")

    return outputs


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Cicconetti family tree visualization."
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=DATA_FILE,
        help="Path to family.json (default: data/family.json)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory (default: reports/)",
    )
    parser.add_argument(
        "--format",
        nargs="+",
        default=["pdf", "png"],
        choices=["pdf", "png", "svg"],
        help="Output format(s) (default: pdf png)",
    )
    parser.add_argument(
        "--filename",
        default="family_tree",
        help="Base filename without extension (default: family_tree)",
    )
    args = parser.parse_args()

    print("Loading family data...")
    data = load_family_data(args.data)
    print(f"  {len(data['people'])} people, {len(data['marriages'])} marriages loaded.")

    print("Rendering family tree...")
    outputs = render_tree(data, args.output_dir, args.format, args.filename)

    print(f"\nDone! {len(outputs)} files generated in {args.output_dir}/")


if __name__ == "__main__":
    main()
