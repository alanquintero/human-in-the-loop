# Local developer setup

Clone this repository to try or contribute to its unreleased skills. The routes below follow official documentation reviewed on 2026-10-03; installation and workflow runs for this project remain unverified. Public marketplace installation stays unavailable, and [release installation](installation.md) remains planned.

## Clone and choose an agent

Install Git and your chosen agent, then clone the source:

```sh
git clone https://github.com/alanquintero/human-in-the-loop.git
cd human-in-the-loop
```

For pull requests without repository write access, fork on GitHub and clone your fork instead. Create a branch before editing. Cloning alone does not install the skills. Keep source changes in `skills/`; use a separate consuming project for scenario tests and keep installed copies out of this plugin's commits.

| Agent | Development route for all skills |
| --- | --- |
| [Codex](#codex) | Register a separate local test marketplace, then install the whole plugin. |
| [ChatGPT Work](#chatgpt-work) | Install the local test plugin through the desktop Plugins Directory. |
| [Claude Code](#claude-code) | Load the whole source checkout with `--plugin-dir`. |
| [GitHub Copilot CLI](#github-copilot) | Install the whole local plugin with `copilot plugin install`. |
| [Copilot in IDEs](#github-copilot) | Batch-copy all skills into the consuming project's discovery folder. |
| [Cursor](#cursor) | Copy the whole plugin into Cursor's local plugin folder. |
| [Gemini CLI](#gemini-cli) | Link the entire `skills/` directory for development, or install a snapshot. |
| [Windsurf / Devin Desktop Cascade](#windsurf--devin-desktop-cascade) | Batch-copy all skills into Cascade's discovery folder. |
| [Cline](#cline) | Batch-copy all skills and check the Skills tab. |
| [OpenCode](#opencode) | Batch-copy all skills into OpenCode's discovery folder. |

Choose one route and scope per agent to avoid duplicate skill names. Native commands below run in your shell unless labeled as chat commands. Use the provider's current client; if a command is missing, check its `--help` and the linked official instructions. The copy route requires Python 3.9+; native plugin routes do not require running this repository's Python installer.

## Codex

[Codex's CLI](https://learn.chatgpt.com/docs/developer-commands) installs the whole plugin after registering its marketplace. The shared catalog sets installation to `NOT_AVAILABLE`. For development, create a separate test checkout from your source checkout:

```sh
git clone . ../human-in-the-loop-plugin-test
```

This contains your current committed branch. Copy any uncommitted skill directories and their resources into the test checkout's `skills/` before testing. In that test checkout only, change `policy.installation` in `.agents/plugins/marketplace.json` to `AVAILABLE`. Do not submit this test-only catalog change.

From your source checkout:

```sh
codex plugin marketplace add ../human-in-the-loop-plugin-test
codex plugin add human-in-the-loop@human-in-the-loop
codex plugin list --json
```

The names before and after `@` are the plugin and marketplace names; both are `human-in-the-loop`. Registration alone does not install the plugin. These commands update local Codex configuration and cache; avoid reusing a marketplace name already configured for another checkout.

Open a fresh chat in your consuming project and select `repo-learning-tutor` from the skill picker. For standalone copied skills, you can also use `$repo-learning-tutor`. Check both skills and their references.

The installed plugin is cached. Refresh the test checkout's files, then reinstall and restart Codex:

```sh
codex plugin remove human-in-the-loop@human-in-the-loop
codex plugin add human-in-the-loop@human-in-the-loop
```

To uninstall, remove the plugin, then run `codex plugin marketplace remove human-in-the-loop`. Keep the shared source catalog unavailable. See [OpenAI packaging](https://developers.openai.com/plugins/build/plugins) for cache behavior and local marketplaces.

## ChatGPT Work

Use the same separate test checkout and `AVAILABLE` edit from the Codex section. Open that checkout in the ChatGPT desktop app, open the Plugins Directory, select Human in the Loop from its local marketplace, and install. Check its packaged skills in a fresh Work chat. [OpenAI documents local marketplaces for the desktop app](https://developers.openai.com/plugins/build/plugins).

Local plugins load from an installed cache. Refresh the test checkout, remove and reinstall through the plugin controls, and restart the app after changes. Uninstall through those controls when finished. This route applies to Work's supported local plugin surface; it does not install skills into every ChatGPT chat or a remote workspace.

## Claude Code

Load the entire checkout directly, including local edits, without filling the empty release marketplace. From the source checkout:

```sh
claude plugin validate .
claude --plugin-dir .
```

To test a different repository, start Claude there with an absolute path to this checkout:

```sh
claude --plugin-dir "/absolute/path/to/human-in-the-loop"
```

In that Claude session, invoke `/human-in-the-loop:repo-learning-tutor` or `/human-in-the-loop:task-tech-tutor`. After editing the source, run `/reload-plugins` and start a fresh conversation for scenario testing. This is session-only loading: finish the session and launch without the flag to stop loading the plugin. [Claude's development guide](https://code.claude.com/docs/en/plugins/create) documents this route and reload behavior.

For persistent standalone skills, use the batch-copy route with `--agent claude`. The repository's Claude marketplace stays empty until release; `--plugin-dir` needs no marketplace change.

## GitHub Copilot

Copilot CLI supports this repository's root Agent Plugins manifest and `skills/` layout. From the checkout, install the whole plugin:

```sh
copilot plugin install .
copilot plugin list
```

Start Copilot in your consuming project, run `/skills list`, and invoke `/repo-learning-tutor`. [GitHub's plugin creation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating) documents local installation and skill discovery.

After edits, refresh the local installation before starting a new session:

```sh
copilot plugin uninstall human-in-the-loop
copilot plugin install .
```

To uninstall, run only the first command. [The CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) documents management commands and local plugin specifications. This direct local installation needs no release marketplace entries.

For Copilot in VS Code or JetBrains, use the batch-copy route with `--agent copilot`, then start agent mode in the consuming project and request the skill by name. Copilot CLI's plugin installation does not establish that an IDE or cloud session has loaded it. [GitHub's skill documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) lists project and personal discovery folders across its clients.

## Cursor

Cursor can load this repository's root `plugin.json` and all of `skills/` as an Agent Plugin. Create a new folder at `~/.cursor/plugins/local/human-in-the-loop/`, then copy `plugin.json` and the entire `skills/` directory from your checkout into it. The result must be:

```text
~/.cursor/plugins/local/human-in-the-loop/
├── plugin.json
└── skills/
    ├── repo-learning-tutor/SKILL.md
    └── task-tech-tutor/SKILL.md
```

Include all supporting resources, not just the two SKILL.md files. Restart Cursor or run **Developer: Reload Window**, open **Customize**, and check that both skills appear. Invoke `/repo-learning-tutor` or select it with `@` in Agent chat.

After edits, replace only this local plugin's copied files with the checkout's current files, then reload. To uninstall, remove only its local plugin folder and reload. Local imports must be allowed by your organization; an installed marketplace plugin with the same name takes precedence. Cursor skips external symlinks from this folder, so copy the files. These rules follow [Cursor's local plugin instructions](https://cursor.com/docs/plugins).

The standalone alternative is batch-copy with `--agent cursor`. [Cursor's skills guide](https://cursor.com/help/customization/skills) documents invocation and personal skill syncing. [GitHub plugin import](https://cursor.com/docs/skills#installing-skills-from-a-repository) requires a Cursor marketplace catalog, which this unreleased repository does not ship; use the local route above.

## Gemini CLI

Gemini CLI can link every skill under the source directory in one command. Its native install and link commands can replace existing same-name destinations; save any previous local edits before running either. From the checkout:

```sh
gemini skills link ./skills --scope user
gemini skills list
```

For workspace scope, run from the consuming project's root with the source's absolute path:

```sh
gemini skills link "/absolute/path/to/human-in-the-loop/skills" --scope workspace
```

Links use the current source files, including uncommitted edits. Keep the checkout in place. After changes, run `/skills reload` in Gemini and check `/skills list`. Ask Gemini to use `repo-learning-tutor`; Gemini presents its own activation consent prompt. [Gemini's skill management guide](https://geminicli.com/docs/cli/using-agent-skills/) documents linking, scopes, reload, and consent.

To install a snapshot of all skills instead, run `gemini skills install ./skills --scope user` from the checkout. Gemini's [installer and linker implementation](https://github.com/google-gemini/gemini-cli/blob/main/packages/cli/src/utils/skillUtils.ts) scans the directory for skills and applies the operation to all of them. Reinstall snapshots after source changes, or keep links for development.

Remove each installed or linked skill by name, using the scope you chose:

```sh
gemini skills uninstall repo-learning-tutor --scope user
gemini skills uninstall task-tech-tutor --scope user
```

For workspace installs, run in the consuming project and substitute `--scope workspace`. Check for new skills to unlink if the source catalog grows.

## Windsurf / Devin Desktop Cascade

Use batch-copy with `--agent windsurf`. It installs all skills into `.windsurf/skills/` for a project or `~/.codeium/windsurf/skills/` for your user. The current Cascade docs prefer `.devin/skills/` for projects and continue to read `.windsurf/skills/`. For manual installation in Devin Desktop, copy all complete skill directories into `.devin/skills/` instead; choose one folder.

Open the consuming workspace in Cascade, start a fresh chat, and mention `@repo-learning-tutor`. Refresh or remove copied directories as described below. [Cascade's skills guide](https://docs.devin.ai/desktop/cascade/skills) documents these locations and invocation. These instructions cover Cascade; Devin Local/CLI uses a separate discovery mechanism.

## Cline

Use batch-copy with `--agent cline`. Open the consuming project in Cline, click the scale icon beside the model selector, and open the **Skills** tab. Check both skills are present and enabled, then select `/repo-learning-tutor` from chat suggestions.

Refresh or remove copied directories as described below. [Cline's skills guide](https://docs.cline.bot/customization/skills) documents automatic discovery, toggles, and slash commands. A global same-name skill takes precedence over a project skill, so remove duplicate test copies if your edits do not load.

## OpenCode

Use batch-copy with `--agent opencode`, then start a fresh OpenCode session in the consuming project. Ask it to load `repo-learning-tutor` through its skill tool and use it to explain the repository. If it is missing, check the selected agent's skill permissions and the frontmatter's name and description.

Refresh or remove copied directories as described below. [OpenCode's skills guide](https://opencode.ai/docs/skills/) documents the discovery folders and permission controls; this is skill-folder installation, not an OpenCode executable-code plugin.

## Batch-copy all skills

This repository's installer supports every local skill-folder route below. It copies **all** complete skill directories by default, including references, scripts, and assets. Run it from the source checkout with Python 3.9+; no third-party packages are needed. On Windows, use `py -3` instead of `python3` if needed.

| Agent argument | Project destination | Personal destination |
| --- | --- | --- |
| `codex` | `.agents/skills/` | `~/.agents/skills/` |
| `claude` | `.claude/skills/` | `~/.claude/skills/` |
| `copilot` | `.github/skills/` | `~/.copilot/skills/` |
| `cursor` | `.cursor/skills/` | `~/.cursor/skills/` |
| `gemini` | `.gemini/skills/` | `~/.gemini/skills/` |
| `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| `cline` | `.cline/skills/` | `~/.cline/skills/` |
| `opencode` | `.opencode/skills/` | `~/.config/opencode/skills/` |

Choose your agent argument from the table. For example, preview and install all Cline skills into an existing consuming project:

```sh
python3 scripts/install-skills.py --agent cline --scope project --project "/path/to/your-project" --dry-run
python3 scripts/install-skills.py --agent cline --scope project --project "/path/to/your-project"
```

For personal installation, replace `cline` with your chosen agent:

```sh
python3 scripts/install-skills.py --agent cline --scope user --dry-run
python3 scripts/install-skills.py --agent cline --scope user
```

Project paths are relative to the consuming project; personal paths are under your home directory. ChatGPT Work uses the plugin route above and is not a copy-installer target.

For a manual alternative without Python, create the destination folder and copy **every subdirectory inside `skills/`** into it using your file manager. Preserve each folder name and all its resources. Do not copy the outer `skills/` folder inside another `skills/` folder. Official discovery sources are linked in the [installation matrix](installation.md#shared-format-different-installation-routes).

The repository installer refuses existing destination names, including dangling symlinks, before copying the batch. Copies are snapshots. After source changes, save any edits made to installed copies, remove only this repository's copied skill directories, and rerun the installer. Start a fresh session and repeat scenarios. To uninstall, remove only those directories; leave unrelated skills and settings intact. Filesystem errors may leave a partial copy; inspect the reported destination before retrying.

## Remote and cloud sessions

Local installation alone does not configure a remote host. Follow the provider's route for the environment you actually run:

| Environment | Development setup |
| --- | --- |
| Codex remote sessions / ChatGPT workspace | Use that host's project-skill or workspace-plugin route; a local plugin cache does not publish to the workspace. See [OpenAI packaging](https://developers.openai.com/plugins/build/plugins). |
| Copilot cloud agent | Copy into `.github/skills/` in the consuming repository and commit the skills and resources to its test branch. See [GitHub's guide](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills). |
| Cursor Cloud Agents | Commit project skills, or enable **Sync Skills for Cloud Agents** for personal `~/.cursor/skills/` in Settings → Agents → Context and Tools. Local plugin folders and `~/.agents/skills/` are not this personal sync route. See [Cursor skills](https://cursor.com/help/customization/skills). |
| Claude Code cloud sessions | Follow [Claude's install guide](https://code.claude.com/docs/en/plugins/install); local `--plugin-dir` sessions and local installed plugins do not supply cloud sessions. Claude.ai/Cowork have separate plugin controls. |
| SSH, containers, other remote workers | Install the agent's skill directories on the worker or commit project skills in its consuming repository; keep the plugin source repository's `skills/` canonical. |

## Verify and contribute

Edit `skills/<name>/SKILL.md` and its resources following the [authoring guide](skill-authoring.md). Refresh your chosen route, then run the skill's `references/scenarios.md` in fresh agent sessions. Verify discovery of both skills, explicit invocation, and access to bundled references. An installation or filesystem copy does not prove workflow execution.

From the source checkout:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Follow [CONTRIBUTING.md](../CONTRIBUTING.md) for remaining checks and PR requirements. Record client version, model, OS, date, scope, installation route, observed scenario results, and skipped checks. Keep public catalogs unavailable until [release checks](releasing.md) are complete.
