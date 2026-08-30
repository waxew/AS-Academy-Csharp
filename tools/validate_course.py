#!/usr/bin/env python3
"""Strict static integrity checks for the AS Academy C# Course Package."""

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
lessons = []
for path in sorted((COURSE / "lessons").glob("*.json")):
    for lesson in records(load(path)):
        lesson_id = lesson["id"]
        require(lesson_id not in lesson_ids, f"duplicate lesson id {lesson_id}")
        require(lesson["chapterId"] in chapter_ids, f"unknown chapter in lesson {lesson_id}")
        require(lesson.get("blocks"), f"lesson {lesson_id} has no learning blocks")
        require(lesson.get("estimatedMinutes", 0) > 0, f"lesson {lesson_id} has invalid estimatedMinutes")
        lesson_ids.add(lesson_id)
        lessons.append(lesson)
require(lessons, "no lessons found")

extras = {}
for folder in ("exercises", "quizzes"):
    ids = set()
    items = []
    for path in sorted((COURSE / folder).glob("*.json")):
        for item in records(load(path)):
            item_id = item["id"]
            require(item_id not in ids, f"duplicate {folder} id {item_id}")
            require(item["lessonId"] in lesson_ids, f"{folder} item {item_id} references missing lesson")
            ids.add(item_id)
            items.append(item)
    extras[folder] = (ids, items)

project_ids = set()
projects = []
for path in sorted((COURSE / "projects").glob("*.json")):
    for item in records(load(path)):
        require(item["id"] not in project_ids, f"duplicate project id {item['id']}")
        require(item.get("steps"), f"project {item['id']} has no steps")
        project_ids.add(item["id"])
        projects.append(item)

exercise_ids, _ = extras["exercises"]
quiz_ids, quizzes = extras["quizzes"]
for lesson in lessons:
    for block in lesson.get("blocks", []):
        metadata = block.get("metadata") or {}
        if "exerciseId" in metadata:
            require(metadata["exerciseId"] in exercise_ids, f"lesson {lesson['id']} links missing exercise {metadata['exerciseId']}")
        if "quizId" in metadata:
            require(metadata["quizId"] in quiz_ids, f"lesson {lesson['id']} links missing quiz {metadata['quizId']}")
        if "projectId" in metadata:
            require(metadata["projectId"] in project_ids, f"lesson {lesson['id']} links missing project {metadata['projectId']}")

for quiz in quizzes:
    require(quiz.get("questions"), f"quiz {quiz['id']} has no questions")
    question_ids = set()
    for question in quiz["questions"]:
        require(question["id"] not in question_ids, f"duplicate question id {question['id']} in quiz {quiz['id']}")
        question_ids.add(question["id"])
        answers = question.get("answers") or []
        require(len(answers) >= 2, f"quiz {quiz['id']} question {question['id']} needs at least two answers")
        require(any(answer.get("isCorrect") for answer in answers), f"quiz {quiz['id']} question {question['id']} has no correct answer")

print(f"Course OK: {len(levels)} levels, {len(chapters)} chapters, {len(lesson_ids)} lessons, {len(exercise_ids)} exercises, {len(quiz_ids)} quizzes, {len(project_ids)} projects")
