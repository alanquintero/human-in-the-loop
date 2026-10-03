# Repository guidance

This repository develops a distributable plugin of software development lifecycle skills. It is unreleased.

- Keep shipped skills in `skills/<skill-name>/SKILL.md`; supporting resources stay beside their skill. Agent discovery folders are not the distribution source.
- Keep installation instructions labeled as planned and the marketplace entry unavailable until the release checklist is complete.
- Save local task notes in `.agents/plans/` (Git-ignored). Keep reusable examples and verification scenarios in the skill directory.
- Read [the authoring guide](docs/skill-authoring.md) when adding or editing a skill.
- Read [CONTRIBUTING.md](CONTRIBUTING.md) when verifying changes or preparing a contribution.
- Read [the setup guide](docs/agent-setup.md) when changing agent wiring or repository layout.
- Read [the release guide](docs/releasing.md) when changing packaging or preparing a release.

There is no application build or automated test suite yet. Check `git diff --check` and follow the scenario verification in CONTRIBUTING.md. Do not claim an unperformed agent run passed.
