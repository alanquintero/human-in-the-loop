#!/usr/bin/env python3
"""Copy canonical skills into an agent's discovery folder. Requires Python 3.9+."""

import argparse
from pathlib import Path
import re
import shutil
import sys


# Official discovery paths and sources are recorded in docs/installation.md.
# Each pair is relative to the project root and the user's home, respectively.
AGENT_PATHS = {
    "codex": (".agents/skills", ".agents/skills"),
    "claude": (".claude/skills", ".claude/skills"),
    "copilot": (".github/skills", ".copilot/skills"),
    "cursor": (".cursor/skills", ".cursor/skills"),
    "gemini": (".gemini/skills", ".gemini/skills"),
    "windsurf": (".windsurf/skills", ".codeium/windsurf/skills"),
    "cline": (".cline/skills", ".cline/skills"),
    "opencode": (".opencode/skills", ".config/opencode/skills"),
}


def install(source_root, destination_root, names=None, dry_run=False):
    """Preflight the entire selection, then copy complete skill folders."""
    sources = sorted(path for path in source_root.iterdir() if path.is_dir())
    if names:
        selected = set(names)
        missing = selected - {path.name for path in sources}
        if missing:
            raise ValueError("Unknown skills: " + ", ".join(sorted(missing)))
        sources = [path for path in sources if path.name in selected]
    if not sources:
        raise ValueError("No skills available. This repository is still unreleased.")

    for source in sources:
        if len(source.name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", source.name):
            raise ValueError(f"Invalid skill directory name: {source.name}")
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing SKILL.md: {source}")
        destination = destination_root / source.name
        if destination.exists() or destination.is_symlink():
            raise ValueError(f"Destination already exists; nothing overwritten: {destination}")
        resolved_destination = destination.resolve()
        resolved_source = source.resolve()
        if resolved_destination == resolved_source or resolved_source in resolved_destination.parents:
            raise ValueError(f"Destination is inside the source skill: {destination}")

    for source in sources:
        destination = destination_root / source.name
        if dry_run:
            print(f"Would copy {source} -> {destination}")
        else:
            destination_root.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, destination)
            print(f"Installed {source.name} -> {destination}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True, choices=AGENT_PATHS)
    parser.add_argument("--scope", required=True, choices=("project", "user"))
    parser.add_argument("--project", type=Path, help="Existing target project root (required for project scope)")
    parser.add_argument("--skill", action="append", help="Skill directory name; repeat to select several (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Show copies without writing files")
    args = parser.parse_args(argv)

    if args.scope == "project":
        if args.project is None or not args.project.expanduser().is_dir():
            parser.error("--scope project requires --project pointing to an existing directory")
        base = args.project.expanduser().resolve()
        relative = AGENT_PATHS[args.agent][0]
    else:
        if args.project is not None:
            parser.error("--project is only valid with --scope project")
        base = Path.home()
        relative = AGENT_PATHS[args.agent][1]

    try:
        install(Path(__file__).resolve().parent.parent / "skills", base / relative, args.skill, args.dry_run)
    except (OSError, ValueError, shutil.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
