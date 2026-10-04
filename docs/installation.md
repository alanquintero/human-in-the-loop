# Agent installation (planned)

**Unreleased:** skill sources are available for development and local review; marketplace installation remains unavailable. These routes follow official documentation reviewed on 2026-10-03; none has passed an installation and workflow run for this plugin. See [release checks](releasing.md) before publishing.

## Shared format, different installation routes

Every skill ships once in `skills/<name>/SKILL.md` using the [Agent Skills format](https://agentskills.io/specification). Copy its entire directory, including scripts, references, and assets. An agent's skill folder belongs in the consuming project or user profile; cloning this repository alone does not install its skills.

The installer uses these documented locations. Project paths are relative to the consuming project; `~` means the user's home directory, including on Windows.

| Agent / installer name | Project skills | Personal skills | Official instructions |
| --- | --- | --- | --- |
| Codex / `codex` | `.agents/skills/` | `~/.agents/skills/` | [Codex skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code / `claude` | `.claude/skills/` | `~/.claude/skills/` | [Claude skills](https://code.claude.com/docs/en/skills) |
| GitHub Copilot / `copilot` | `.github/skills/` | `~/.copilot/skills/` | [Copilot skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| Cursor / `cursor` | `.cursor/skills/` | `~/.cursor/skills/` | [Cursor skills](https://cursor.com/help/customization/skills) |
| Gemini CLI / `gemini` | `.gemini/skills/` | `~/.gemini/skills/` | [Gemini skills](https://geminicli.com/docs/cli/using-agent-skills/) |
| Windsurf / Devin Desktop Cascade / `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | [Cascade skills](https://docs.devin.ai/desktop/cascade/skills) |
| Cline / `cline` | `.cline/skills/` | `~/.cline/skills/` | [Cline skills](https://docs.cline.bot/customization/skills) |
| OpenCode / `opencode` | `.opencode/skills/` | `~/.config/opencode/skills/` | [OpenCode skills](https://opencode.ai/docs/skills/) |

Cascade's current project folder is `.devin/skills/`; the installer uses its documented `.windsurf/skills/` compatibility path. Several agents also read `.agents/skills/`; use one installation route per agent to avoid duplicate skills.

Personal files stay on the local machine unless the agent explicitly syncs them. For remote or cloud sessions, install and commit project skills into the repository that session runs, or use the host's supported plugin/sync route. Cursor syncs personal skills from `~/.cursor/skills/` when enabled. Claude Cowork and cloud sessions use account skills; Claude cloud sessions can also read committed project skills. Local personal folders do not supply those sessions.

## Copy installer

After release, download a tagged source archive or clone the release tag, then run from this repository with Python 3.9+. On Windows use `py -3` instead of `python3` if needed. No third-party Python packages are required.

Preview a project installation, then repeat without `--dry-run` to install:

```sh
python3 scripts/install-skills.py --agent copilot --scope project --project "/path/to/your-project" --dry-run
```

For personal installation:

```sh
python3 scripts/install-skills.py --agent claude --scope user --dry-run
```

Replace `--agent` with any name in the table. By default all skills are selected; use `--skill <name>` (repeatable) for individual skills. The script copies complete folders without changing their contents or relying on symlinks. It refuses existing destination names, including dangling symlinks, before copying any selected skill. Empty sources and unknown skill names fail without installing anything. It checks directory names and the presence of `SKILL.md`, not YAML metadata or workflow behavior.

Restart the agent or use its documented reload action, check its skills list, and invoke a skill. For example, Gemini offers `/skills reload` and `/skills list`; Claude Code plugin skills use `/human-in-the-loop:<name>`.

For updates, review and remove only the previously installed skill directories before installing the new tagged version. To uninstall copied skills, remove those directories. Other skills and agent settings are outside the installer's scope. Filesystem errors during copying may leave a partial installation; the script reports the error and exits unsuccessfully.

Manual installation is also supported: copy `skills/<name>/` to `<table-path>/<name>/`. Keep the folder name and all supporting resources intact.

## Codex and ChatGPT Work plugin

The root `plugin.json` packages `skills/`. `.agents/plugins/marketplace.json` catalogs that plugin and remains `NOT_AVAILABLE` during development. [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins) describes this route for Codex and Work mode in the ChatGPT desktop app.

After release, register the marketplace using its actual tag (replace the example `v0.1.0`):

```sh
codex plugin marketplace add alanquintero/human-in-the-loop --ref v0.1.0
```

Then open the Plugins Directory, select Human in the Loop, and install the plugin. Marketplace registration alone does not install it. Standalone Codex skills can instead use the copy installer. This plugin route does not imply installation into every ChatGPT chat surface.

## Claude Code plugin

`.claude-plugin/plugin.json` lets Claude Code discover the same root `skills/`; it does not duplicate the workflows. The Claude marketplace's `plugins` array stays empty until release because its catalog uses a different format from OpenAI's. [Claude marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces) describes registration and installation.

After release, register a checkout of the reviewed release tag, then install:

```sh
claude plugin marketplace add /path/to/tagged/human-in-the-loop
claude plugin install human-in-the-loop@human-in-the-loop
```

Use Claude Code's plugin manager to update or uninstall. Use the copy installer instead for standalone skills; it needs no marketplace.

## Compatibility limits

Installation makes instructions discoverable; workflow execution also requires the tools and access declared by each skill. A model provider alone does not define skill installation. An agent hosting that model must support skills and the workflow's capabilities. Add other hosts only after checking their documented mechanism; do not claim universal or tested support from the shared file format alone.
