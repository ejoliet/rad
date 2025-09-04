#!/usr/bin/env python3
"""
Generate Mermaid mindmaps and a dependency graph for GDPS ASDF schemas.

Inputs:
- Scans latest/SSC/GDPS and latest/SSC/GDPS/keywords

Outputs:
- docs/gdps_mindmaps/*.md with Mermaid mindmap blocks
- docs/gdps_graph.md with a Mermaid flowchart of $ref dependencies
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple, Set

import yaml


WORKSPACE = Path(__file__).resolve().parents[1]
GDPS_DIR = WORKSPACE / "latest" / "SSC" / "GDPS"
KEYWORDS_DIR = GDPS_DIR / "keywords"
DOCS_OUT = WORKSPACE / "docs" / "gdps_mindmaps"
DOCS_OUT.mkdir(parents=True, exist_ok=True)


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def is_top_level_schema(path: Path) -> bool:
    # Filter only GDPS top-level schemas (exclude keywords dir)
    return path.parent == GDPS_DIR and path.suffix in {".yaml", ".yml"}


def collect_keyword_files() -> Dict[str, Path]:
    mapping: Dict[str, Path] = {}
    for p in sorted(KEYWORDS_DIR.glob("*.y*ml")):
        data = load_yaml(p)
        schema_id = data.get("id")
        if not schema_id:
            continue
        mapping[schema_id] = p
    return mapping


def extract_refs(schema: Dict[str, Any]) -> List[str]:
    refs: List[str] = []
    props = schema.get("properties", {})
    meta = props.get("meta") if isinstance(props, dict) else None
    if isinstance(meta, dict):
        all_of = meta.get("allOf", [])
        for item in all_of:
            if isinstance(item, dict) and "$ref" in item:
                refs.append(item["$ref"]) 
    return refs


def extract_properties(schema: Dict[str, Any]) -> List[Tuple[str, Dict[str, Any]]]:
    props = schema.get("properties", {})
    items: List[Tuple[str, Dict[str, Any]]] = []
    if not isinstance(props, dict):
        return items
    for key, val in props.items():
        if not isinstance(val, dict):
            continue
        items.append((key, val))
    return items


def build_mindmap_for_keywords(name: str, schema: Dict[str, Any]) -> str:
    # Mermaid mindmap; if not supported in viewer, it still renders as code block.
    lines: List[str] = ["```mermaid", "mindmap", f"  root(({name}))"]
    props = schema.get("properties", {})
    if isinstance(props, dict):
        for key, val in props.items():
            title = val.get("title") if isinstance(val, dict) else None
            tpe = val.get("type") if isinstance(val, dict) else None
            tag = val.get("tag") if isinstance(val, dict) else None
            leaf = f"{key}"
            meta_desc: List[str] = []
            if title:
                meta_desc.append(title)
            if tpe:
                meta_desc.append(f"type={tpe}")
            if tag:
                meta_desc.append(f"tag={tag}")
            if meta_desc:
                leaf += f" — {'; '.join(meta_desc)}"
            lines.append(f"    root::{leaf}")
    lines.append("```")
    return "\n".join(lines)


def build_mindmap_for_top_level(file_name: str, schema: Dict[str, Any], keyword_schemas: Dict[str, Dict[str, Any]]) -> str:
    title = schema.get("title", file_name)
    lines: List[str] = ["```mermaid", "mindmap", f"  root(({title}))", "    root::meta"]
    # Expand meta allOf -> referenced keyword groups
    for ref in extract_refs(schema):
        ref_name = ref.rsplit("/", 1)[-1]
        ref_schema = keyword_schemas.get(ref)
        display = ref_name
        lines.append(f"      meta::{display}")
        if isinstance(ref_schema, dict):
            props = ref_schema.get("properties", {})
            if isinstance(props, dict):
                for key, val in props.items():
                    title_k = val.get("title") if isinstance(val, dict) else None
                    tpe = val.get("type") if isinstance(val, dict) else None
                    tag = val.get("tag") if isinstance(val, dict) else None
                    leaf = f"{key}"
                    meta_desc: List[str] = []
                    if title_k:
                        meta_desc.append(title_k)
                    if tpe:
                        meta_desc.append(f"type={tpe}")
                    if tag:
                        meta_desc.append(f"tag={tag}")
                    if meta_desc:
                        leaf += f" — {'; '.join(meta_desc)}"
                    lines.append(f"        {display}::{leaf}")
    lines.append("```")
    return "\n".join(lines)


def build_dependency_graph(top_files: List[Path], keyword_id_to_path: Dict[str, Path]) -> str:
    edges: Set[Tuple[str, str]] = set()
    for top in top_files:
        schema = load_yaml(top)
        src = top.stem
        for ref in extract_refs(schema):
            dst = ref.rsplit("/", 1)[-1]
            edges.add((src, dst))

    lines: List[str] = ["```mermaid", "flowchart TD"]
    for a, b in sorted(edges):
        # sanitize node ids for mermaid
        aid = re.sub(r"[^A-Za-z0-9_]", "_", a)
        bid = re.sub(r"[^A-Za-z0-9_]", "_", b)
        lines.append(f"  {aid}[{a}] --> {bid}[{b}]")
    lines.append("```")
    return "\n".join(lines)


def main() -> int:
    if not GDPS_DIR.exists():
        print(f"GDPS directory not found: {GDPS_DIR}", file=sys.stderr)
        return 1

    keyword_id_to_path = collect_keyword_files()
    # Load keyword schemas content for expansion
    keyword_schemas: Dict[str, Dict[str, Any]] = {
        k: load_yaml(v) for k, v in keyword_id_to_path.items()
    }

    top_files = [p for p in sorted(GDPS_DIR.glob("*.y*ml")) if is_top_level_schema(p)]
    if not top_files:
        print("No top-level GDPS schemas found.")
    # Generate per-keyword mindmaps (optional, can be helpful)
    for schema_id, path in keyword_id_to_path.items():
        name = schema_id.rsplit("/", 1)[-1]
        mind = build_mindmap_for_keywords(name, load_yaml(path))
        out_path = DOCS_OUT / f"{name}.md"
        out_path.write_text(mind + "\n", encoding="utf-8")

    # Generate top-level mindmaps expanding meta -> keyword properties
    for p in top_files:
        data = load_yaml(p)
        name = p.stem
        mind = build_mindmap_for_top_level(name, data, keyword_schemas)
        out_path = DOCS_OUT / f"{name}.md"
        out_path.write_text(mind + "\n", encoding="utf-8")

    # Dependency graph across top-level schemas
    graph = build_dependency_graph(top_files, keyword_id_to_path)
    (WORKSPACE / "docs" / "gdps_graph.md").write_text(graph + "\n", encoding="utf-8")

    print(f"Generated {len(list(DOCS_OUT.glob('*.md')))} mindmaps and dependency graph at docs/gdps_graph.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

