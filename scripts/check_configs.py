#!/usr/bin/env python3
"""Check every shipped manifest and the skill itself. Exit 1 on any failure.

- Every JSON manifest parses.
- Every manifest names the plugin `building-with-decision-models`, and every version
  field (top level, `metadata`, and each marketplace entry) agrees. Copilot, Grok
  and Antigravity show the root plugin.json, so a stale one is what users see.
- Each SKILL.md has frontmatter with `name` and `description`, and the name matches its folder.
- Every file the skill names (`providers/jev.md`, `models/clef.md`, `prior-art/projects/gates.md`, ...) exists.
  Paths are relative to the skill root wherever they appear, so each one names exactly one file.
- Every script a skill names exists and compiles.
- No file in the repo contains something shaped like a TypeSafe API key.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "building-with-decision-models"
SKILL_DIR = ROOT / "skills" / NAME
# Extra frontmatter keys each skill may carry, beyond name and description.
EXTRA_KEYS = {SKILL_DIR.name: []}
SCRIPT_REF = re.compile(r"scripts/([\w-]+\.py)")
JSON_MANIFESTS = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".cursor-plugin/marketplace.json",
    ".devin-plugin/plugin.json",
    ".github/plugin/marketplace.json",
    ".grok-plugin/marketplace.json",
    ".kimi-plugin/plugin.json",
    ".muse-plugin/plugin.json",
    "gemini-extension.json",
    "package.json",
    "plugin.json",
]
KEY_SHAPE = re.compile(r"apikey_[0-9a-f]{20,}")
SKILL_REF = re.compile(r"`((?:[\w-]+/)*[\w.-]+\.md)`")

errors: list[str] = []
versions: dict[str, str] = {}


def note_version(where: str, value) -> None:
    if value is not None:
        versions[where] = str(value)


for rel in JSON_MANIFESTS:
    try:
        data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{rel}: {exc}")
        continue
    if data.get("name") != NAME:
        errors.append(f"{rel}: name is {data.get('name')!r}, expected {NAME!r}")
    note_version(rel, data.get("version"))
    note_version(f"{rel} metadata", (data.get("metadata") or {}).get("version"))
    for entry in data.get("plugins", []):
        if entry.get("name") != NAME:
            errors.append(f"{rel}: plugin entry named {entry.get('name')!r}")
        note_version(f"{rel} plugins[{entry.get('name')}]", entry.get("version"))

if len(set(versions.values())) > 1:
    listing = "\n  ".join(f"{v}  {k}" for k, v in sorted(versions.items()))
    errors.append(f"manifests disagree on version:\n  {listing}")

for skill_dir, extra in EXTRA_KEYS.items():
    path = ROOT / "skills" / skill_dir / "SKILL.md"
    skill = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    if not match:
        errors.append(f"{skill_dir}/SKILL.md: no frontmatter")
        continue
    keys = [line.split(":", 1)[0] for line in match.group(1).splitlines() if re.match(r"^\w", line)]
    if keys[:2] != ["name", "description"] or sorted(keys[2:]) != sorted(extra):
        errors.append(f"{skill_dir}/SKILL.md: frontmatter keys must be name, description{''.join(', ' + k for k in extra)}; found {keys}")
    name = re.search(r"^name:\s*(.+)$", match.group(1), re.M)
    if not name or name.group(1).strip() != skill_dir:
        errors.append(f"{skill_dir}/SKILL.md: name does not match its folder")
    if len(match.group(1)) > 1024:
        errors.append(f"{skill_dir}/SKILL.md: frontmatter is over 1024 characters")
    for script in set(SCRIPT_REF.findall(skill)):
        if not any((ROOT / "skills" / d / "scripts" / script).exists() for d in EXTRA_KEYS):
            errors.append(f"{skill_dir}/SKILL.md: names scripts/{script}, which does not exist")

for script in ROOT.glob("skills/*/scripts/*.py"):
    try:
        compile(script.read_text(encoding="utf-8"), str(script), "exec")
    except SyntaxError as exc:
        errors.append(f"{script.relative_to(ROOT)}: does not compile ({exc})")

for md in SKILL_DIR.rglob("*.md"):
    for ref in SKILL_REF.findall(md.read_text(encoding="utf-8")):
        if not (SKILL_DIR / ref).exists():
            errors.append(f"{md.relative_to(ROOT)}: names `{ref}`, which does not exist under the skill root")

for path in ROOT.rglob("*"):
    if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".json", ".py", ".yaml", ".yml", ".txt", ".toml", ".sh"}:
        if KEY_SHAPE.search(path.read_text(encoding="utf-8", errors="ignore")):
            errors.append(f"{path.relative_to(ROOT)}: contains something shaped like an API key")

for e in errors:
    print(f"error: {e}")
print("ok" if not errors else f"{len(errors)} error(s)")
sys.exit(1 if errors else 0)
