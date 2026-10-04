# Repository setup

AGENTS.md guides agents editing this repository and links to detailed guidance. CLAUDE.md imports that entry point. These files guide development of the plugin; they are not its workflow skills.

For cloning and trying all unreleased skills in any listed agent, follow [local usage and development guide](local-development.md). It covers native plugin loading, Gemini skill linking, and batch-copy discovery folders, with refresh and uninstall instructions.

The repository root is the plugin package: `plugin.json` identifies it, and `skills/` holds its canonical skill sources. `.agents/plugins/marketplace.json` catalogs the plugin with a source path relative to the repository root. Its installation policy is `NOT_AVAILABLE` while development is incomplete. `.claude-plugin/plugin.json` supplies Claude Code metadata; its marketplace catalog has no plugin entries until release. Keep both manifests' identity, version, and descriptive metadata synchronized.

Keep skill sources in `skills/`; consumers install the plugin or copy complete skill directories using the [installation guide](installation.md). The installer targets consumers' discovery folders; those folders are not distribution sources. Add discovery links here only for documented local testing, and keep one source of truth. Installing skills is separate from configuring an agent to edit this repository.

Codex/Work marketplace tests enable installation only in a separate test checkout. Claude Code can load the root directly with `--plugin-dir`; Copilot CLI and Cursor also support the root Agent Plugins manifest without extra source directories. Gemini links the canonical skill directories. Keep provider caches, local plugin copies, and test-only catalog edits outside contributions.

For other development agents, configure their instruction entry point to read AGENTS.md using their documented mechanism. Add integration files only when needed.

Local plans belong in `.agents/plans/` (Git-ignored); create it when needed. Reusable guidance, examples, and scenarios belong in tracked docs or skill resources. Local settings and worktrees are ignored.

See [the release checklist](releasing.md) for enabling distribution and [OpenAI's packaging guide](https://developers.openai.com/plugins/build/plugins) for the package and marketplace formats.
