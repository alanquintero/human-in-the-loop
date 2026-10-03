# Repository setup

AGENTS.md guides agents editing this repository and links to detailed guidance. CLAUDE.md imports that entry point. These files guide development of the plugin; they are not its workflow skills.

The repository root is the plugin package: `plugin.json` identifies it, and `skills/` holds its canonical skill sources. `.agents/plugins/marketplace.json` catalogs the plugin with a source path relative to the repository root. Its installation policy is `NOT_AVAILABLE` while development is incomplete.

Keep skill sources in `skills/`; consumers receive them through plugin installation. Add agent-specific discovery links only for a documented local testing need, and keep one source of truth. Installing this plugin is separate from configuring an agent to edit its repository.

For other development agents, configure their instruction entry point to read AGENTS.md using their documented mechanism. Add integration files only when needed.

Local plans belong in `.agents/plans/` (Git-ignored); create it when needed. Reusable guidance, examples, and scenarios belong in tracked docs or skill resources. Local settings and worktrees are ignored.

See [the release checklist](releasing.md) for enabling distribution and [OpenAI's packaging guide](https://developers.openai.com/plugins/build/plugins) for the package and marketplace formats.
