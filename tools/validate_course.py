#!/usr/bin/env python3
"""Static integrity checks for the AS Academy C# Course Package."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def fail(message: str):
    raise SystemExit(f"COURSE VALIDATION FAILED: {message}")


def require(condition: bool, message: str):
    if not condition:
        fail(message)


def records(value):
    """Accept one object or a JSON array so legacy bundles stay valid."""
    return value if isinstance(value, list) else [value]


manifest = load(COURSE / "manifest.json")
levels = load(COURSE / "levels.json")
chapters = load(COURSE / "chapters.json")

require(manifest.get("courseId") == "csharp", "manifest.courseId must be csharp")
require(len(levels) == 4, "exactly four Academy levels are required")

level_ids = {item["id"] for item in levels}
require(len(level_ids) == len(levels), "duplicate level ids")

chapter_ids = set()
for chapter in chapters:
    require(chapter["levelId"] in level_ids, f"unknown level in chapter {chapter['id']}")
    require(chapter["id"] not in chapter_ids, f"duplicate chapter id {chapter['id']}")
    chapter_ids.add(chapter["id"])

lesson_ids = set()
lesson_files = sorted((COURSE / "lessons").glob("*.json"))
require(lesson_files, "no lessons found")
for path in lesson_files:
    for lesson in records(load(path)):
        lesson_id = lesson["id"]
        require(lesson_id not in lesson_ids, f"duplicate lesson id {lesson_id}")
        require(lesson["chapterId"] in chapter_ids, f"unknown chapter in lesson {lesson_id}")
        require(lesson.get("blocks"), f"lesson {lesson_id} has no learning blocks")
        lesson_ids.add(lesson_id)

for folder in ("exercises", "quizzes"):
    for path in sorted((COURSE / folder).glob("*.json")):
        for item in records(load(path)):
            require(item["lessonId"] in lesson_ids, f"{folder} item {item['id']} references missing lesson")

project_ids = set()
for path in sorted((COURSE / "projects").glob("*.json")):
    for item in records(load(path)):
        require(item["id"] not in project_ids, f"duplicate project id {item['id']}")
        require(item.get("steps"), f"project {item['id']} has no steps")
        project_ids.add(item["id"])

print(
    f"Course OK: {len(levels)} levels, {len(chapters)} chapters, "
    f"{len(lesson_ids)} lessons, {len(project_ids)} projects"
)
