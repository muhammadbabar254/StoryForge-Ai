"""Story History — persistent index of all generated stories."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

HISTORY_DIR = Path("Stories")
INDEX_FILE = HISTORY_DIR / ".storyforge_history.json"


def _load_index() -> list:
    if INDEX_FILE.exists():
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_index(entries: list):
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


def record_story(
    title: str,
    summary: str,
    tags: str,
    word_count: int,
    md_path: str,
    json_path: str,
    elapsed_seconds: float,
    models_used: Optional[Dict] = None,
    extra: Optional[Dict] = None,
) -> dict:
    """Add a story entry to the history index."""
    entry = {
        "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "title": title,
        "summary": summary,
        "tags": tags,
        "word_count": word_count,
        "md_path": md_path,
        "json_path": json_path,
        "elapsed_seconds": round(elapsed_seconds, 1),
        "created_at": datetime.now().isoformat(),
        "generator": "StoryForge AI",
        "models": models_used or {},
        **(extra or {}),
    }

    index = _load_index()
    index.insert(0, entry)
    _save_index(index)
    return entry


def list_stories(limit: int = 50) -> list:
    """Return recent stories from history."""
    return _load_index()[:limit]


def get_story(story_id: str) -> Optional[dict]:
    """Look up a story by its history ID."""
    for entry in _load_index():
        if entry.get("id") == story_id:
            return entry
    return None


def delete_story(story_id: str) -> bool:
    """Remove a story from history (does not delete files)."""
    index = _load_index()
    new_index = [e for e in index if e.get("id") != story_id]
    if len(new_index) == len(index):
        return False
    _save_index(new_index)
    return True


def rebuild_index_from_disk(stories_dir: str = "Stories") -> int:
    """Scan Stories/ for .json files and rebuild the history index."""
    entries = []
    stories_path = Path(stories_dir)
    if not stories_path.exists():
        return 0

    for json_file in sorted(stories_path.glob("*.json"), reverse=True):
        if json_file.name.startswith("."):
            continue
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            md_file = json_file.with_suffix(".md")
            entries.append(
                {
                    "id": json_file.stem,
                    "title": data.get("Title", json_file.stem),
                    "summary": data.get("Summary", ""),
                    "tags": data.get("Tags", ""),
                    "word_count": 0,
                    "md_path": str(md_file) if md_file.exists() else "",
                    "json_path": str(json_file),
                    "elapsed_seconds": 0,
                    "created_at": datetime.fromtimestamp(
                        json_file.stat().st_mtime
                    ).isoformat(),
                    "generator": "StoryForge AI",
                    "rebuilt": True,
                }
            )
        except (json.JSONDecodeError, OSError):
            continue

    _save_index(entries)
    return len(entries)
