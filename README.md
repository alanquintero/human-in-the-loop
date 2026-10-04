# Human in the Loop

Portable AI skills for the software development lifecycle, with human judgment at the decisions that need it.

> **Unreleased — in development.** The first skill is available in source for development and local review; marketplace installation remains unavailable.

Planned workflows include task analysis, implementation, PR review, and self-review.

## Skills (in development)

| Skill | Purpose |
| --- | --- |
| [repo-learning-tutor](skills/repo-learning-tutor/SKILL.md) | Learn an unfamiliar code or documentation repository through orientation, guided practice, and local progress notes. |

This first version has had brief author use; fresh-agent workflow verification and release checks remain pending.

## Supported agents (planned)

| Agent | Installation route |
| --- | --- |
| OpenAI Codex | Plugin marketplace or copy installer |
| OpenAI ChatGPT Work | Plugin marketplace |
| Anthropic Claude Code | Plugin marketplace or copy installer |
| GitHub Copilot | Copy installer |
| Cursor | Copy installer |
| Google Gemini CLI | Copy installer |
| Windsurf / Devin Desktop Cascade | Copy installer |
| Cline | Copy installer |
| OpenCode | Copy installer |

These routes have packaging and installation instructions; agent installation verification remains pending. ChatGPT support refers to Work's plugin route. See [the release checklist](docs/releasing.md) before enabling distribution.

## Installation (planned)

Follow the [installation guide](docs/installation.md) for commands, prerequisites, official discovery paths, and cloud-session limitations. Each skill stays in one source directory; agent-specific installation puts it where that agent discovers skills.

## Layout

```text
plugin.json          Plugin identity and development version
skills/              Shipped skill sources, each containing SKILL.md
.agents/plugins/     Marketplace catalog (installation currently disabled)
.claude-plugin/      Claude Code manifest and empty unreleased catalog
.agents/plans/        Local task notes and plans (ignored by Git)
scripts/             Portable copy installer and its verification guide
tests/               Installer and packaging checks using temporary fixtures
docs/                Installation, authoring, setup, and release guides
AGENTS.md            Shared instructions for agents working on this repository
CLAUDE.md            Pointer to the shared instructions
CONTRIBUTING.md      Contribution and verification workflow
LICENSE              MIT license
```

## Add a skill

1. Read the [authoring guide](docs/skill-authoring.md).
2. Create `skills/<skill-name>/SKILL.md` with metadata and a focused workflow.
3. Add supporting files only when needed, and record representative scenarios and expected outcomes.
4. Follow [CONTRIBUTING.md](CONTRIBUTING.md) to verify the change.
5. Add the finished skill to this README with its purpose and a relative link.

Skills use the [Agent Skills format](https://agentskills.io/specification) and are distributed together using [plugin packaging](https://developers.openai.com/plugins/build/plugins). Document special requirements with each skill.

## Agent setup

See the [repository setup guide](docs/agent-setup.md) for shared instructions, skill locations, and local planning files.

## License

[MIT](LICENSE).
