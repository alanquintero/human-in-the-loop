# Local learning documents

Read before every technology-map, learning-note, or handoff write. These safeguards implement the skill's Git boundary; they do not grant publication permission.

1. Choose exact document paths in the project's permitted local-notes location; follow project rules over a default. If none is specified, use `TASK_TECH_NOTES.md` at the project root. Keep notes scoped to the task and preserve learner history. Never overwrite an unrelated file or another task's notes; choose a distinct path when necessary.
2. In Git, resolve the repository root and local exclusion file with read-only Git commands, including `git rev-parse --git-path info/exclude` for linked worktrees. Check every intended document path with `git ls-files`. If any is tracked, leave it untouched; never remove it from the index to make persistence possible.
3. For untracked documents, append missing exact-path rules to local `info/exclude`, preserving existing entries. Anchor each rule at the repository root, including any nested project prefix, and escape Git ignore metacharacters when needed. Do not ignore a whole source directory. Ensure local rules exist even when project or global ignores already cover the documents.
4. Before each write, verify every destination is untracked and its local exclusion rule remains present and effective with `git check-ignore`. If tracking, permissions, conflicting patterns, unavailable Git commands, or project instructions prevent verification, leave affected documents untouched and provide their content in conversation. Do not edit project/global ignore files, Git configuration, or tracked documents as a workaround.
5. Outside Git, create only learning documents in the permitted location without initializing Git. If the directory is unwritable, continue without saving.

Record concise source-linked versions, technology targets, demonstrated understanding, remaining gaps, and readiness; omit source dumps and secrets. Report saved paths or unsaved progress in the handoff. Recheck the relevant project versions before reusing saved lessons after project changes.
