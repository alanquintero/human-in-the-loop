# Human in the Loop

An installable plugin of AI skills for the software development lifecycle, with human judgment at the decisions that need it.

> **Unreleased — in development.** No workflow skills are available yet. The plugin manifest and marketplace entry are scaffolding; marketplace installation is disabled.

Planned workflows include task analysis, implementation, PR review, and self-review.

## Installation (planned)

After the first release, users will register this marketplace through the Codex CLI:

```sh
codex plugin marketplace add alanquintero/human-in-the-loop
```

Then open the Plugins Directory, select the Human in the Loop marketplace, and install the plugin. Adding the marketplace registers its source; it does not install the plugin itself. Users will not need to manually clone this repository or copy skills into agent folders.

These instructions describe the intended release flow and have not been tested for this plugin. See [the release checklist](docs/releasing.md) before enabling installation. Other agents' installation instructions will be added when their integrations are tested.

## Layout

```text
plugin.json          Plugin identity and development version
skills/              Shipped skill sources, each containing SKILL.md
.agents/plugins/     Marketplace catalog (installation currently disabled)
.agents/plans/        Local task notes and plans (ignored by Git)
docs/                Authoring and repository setup guides
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
