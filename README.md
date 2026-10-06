# Human in the Loop

Portable AI skills for the software development lifecycle, with human judgment at the decisions that need it.

> **Unreleased — in development.** Codex marketplace installation is available for trying the development version. Stable release and workflow verification remain pending.

Planned workflows include task analysis, implementation, PR review, and self-review.

## Skills (in development)

| Skill | Purpose |
| --- | --- |
| [repo-learning-tutor](skills/repo-learning-tutor/SKILL.md) | Learn an unfamiliar code or documentation repository through orientation, guided practice, and local progress notes. |
| [task-tech-tutor](skills/task-tech-tutor/SKILL.md) | Learn the technologies and specific framework concepts a ticket requires before detailed task analysis. |

`repo-learning-tutor` has had brief author use; workflow verification across supported hosts and release checks remain pending for both skills.

## Install in Codex now

With Git and a Codex CLI that supports `codex plugin`, run this single line in your terminal (macOS/Linux or PowerShell 7+) once the default branch on GitHub contains the `AVAILABLE` catalog:

```sh
codex plugin marketplace add alanquintero/human-in-the-loop && codex plugin add human-in-the-loop@human-in-the-loop
```

Codex downloads the repository, registers its marketplace, and installs the whole plugin. You do not need to clone it first or run the Python installer. The line combines two Codex commands; registration must succeed before installation runs. In older PowerShell, run the two commands separately.

Maintainers must push the commit that enables the catalog before sharing this GitHub command; a local `AVAILABLE` change does not update GitHub's marketplace.

If you already cloned the repository, run this from its root instead:

```sh
codex plugin marketplace add . && codex plugin add human-in-the-loop@human-in-the-loop
```

Register the marketplace once. After registration, `codex plugin add human-in-the-loop@human-in-the-loop` is enough. In a fresh Codex CLI 0.160.0 profile, cloning and entering the directory alone did not register the marketplace.

Restart Codex, open a fresh chat in the project where you want to use the skills, and select `repo-learning-tutor` or `task-tech-tutor` from the skill picker. See [Codex setup and troubleshooting](docs/local-development.md#codex) for verification, updates, and an old marketplace showing `NOT_AVAILABLE`. Commands follow [OpenAI's CLI reference](https://learn.chatgpt.com/docs/developer-commands).

## Supported agents (planned)

| Agent | Installation route |
| --- | --- |
| OpenAI Codex | Plugin marketplace or copy installer |
| OpenAI ChatGPT Work | Plugin marketplace |
| Anthropic Claude Code | Direct local plugin, plugin marketplace, or copy installer |
| GitHub Copilot | Local plugin (CLI) or copy installer |
| Cursor | Local Agent Plugin or copy installer |
| Google Gemini CLI | Native skill install/link or copy installer |
| Windsurf / Devin Desktop Cascade | Copy installer |
| Cline | Copy installer |
| OpenCode | Copy installer |

These setup instructions follow each provider's official documentation. Codex CLI installation from a local checkout has been checked; fresh-agent workflow runs and other hosts remain unverified. ChatGPT support refers to Work's plugin route. See [the release checklist](docs/releasing.md) before publishing a stable release.

## Local usage and development

Follow the [local usage and development guide](docs/local-development.md) to clone the repository and try all its skills in your chosen agent. Contributing changes is optional. The guide covers every listed agent, including refresh and uninstall steps. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Release installation (planned)

Follow the [installation guide](docs/installation.md) for commands, prerequisites, official discovery paths, and cloud-session limitations. Each skill stays in one source directory; agent-specific installation puts it where that agent discovers skills.

## Layout

```text
plugin.json          Plugin identity and development version
skills/              Shipped skill sources, each containing SKILL.md
.agents/plugins/     Codex marketplace catalog (development install available)
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
