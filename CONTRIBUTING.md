# Contributing

Keep each change focused on one workflow or one shared improvement. Describe the problem, the resulting behavior, and how you checked it.

## Authoring

Follow [the skill authoring guide](docs/skill-authoring.md). Update the README catalog when adding or renaming a skill. Keep general repository guidance in AGENTS.md and linked docs; workflow-specific instructions belong in the skill.

Use fictional or sanitized tickets, diffs, and comments for examples. Never commit credentials, private customer data, or personal agent configuration.

Develop plugin skills in `skills/`. End users install the packaged plugin; they do not need an author checkout. Keep the unreleased notice and installation policy until [the release checklist](docs/releasing.md) is complete.

## Verification

For each new skill or behavior change:

1. Check metadata, relative resource links, referenced commands, and declared prerequisites.
2. Record scenarios in the skill's `references/scenarios.md`: input, expected behavior, and completion criteria. Include a normal case, missing information, an out-of-scope request, and any relevant approval boundary.
3. Run representative scenarios in a fresh agent session with the intended tools available. Record the agent, model, date, observed result, and any skipped scenarios in the PR or local review notes.
4. Check that a review skill reports evidence and file locations, and that an implementation skill verifies its changes with the target project's checks.
5. Run `git diff --check` and inspect `git status --short` for accidental files.

If an agent run is unavailable, state that limitation and distinguish static review from observed behavior. Add automated checks when executable scripts or repeatable validation justify them; document their commands and dependencies alongside the code.

## Pull requests

Use the PR template. List changed workflows, meaningful verification results, and remaining limitations. Avoid unrelated cleanup in the same PR.
