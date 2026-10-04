# Contributing

Keep each change focused on one workflow or one shared improvement. Describe the problem, the resulting behavior, and how you checked it.

## Get started locally

Follow [local developer setup](docs/local-development.md) to clone this repository or your fork and load all unreleased skills in your chosen agent. Use its native plugin/link route where documented, or batch-copy all skills, then refresh that route when testing edits. You do not need a published release to contribute; keep test-only catalog changes and installed copies out of the PR.

## Authoring

Follow [the skill authoring guide](docs/skill-authoring.md). Update the README catalog when adding or renaming a skill. Keep general repository guidance in AGENTS.md and linked docs; workflow-specific instructions belong in the skill.

Use fictional or sanitized tickets, diffs, and comments for examples. Never commit credentials, private customer data, or personal agent configuration.

Develop skills in `skills/`. End users install a plugin or copy complete skill directories using the [installation guide](docs/installation.md). Keep the unreleased notice and unavailable marketplace catalogs until [the release checklist](docs/releasing.md) is complete.

## Verification

For each new skill or behavior change:

1. Check metadata, relative resource links, referenced commands, and declared prerequisites.
2. Record scenarios in the skill's `references/scenarios.md`: input, expected behavior, and completion criteria. Include a normal case, missing information, an out-of-scope request, and any relevant approval boundary.
3. Run representative scenarios in a fresh agent session with the intended tools available. Record the agent, model, date, observed result, and any skipped scenarios in the PR or local review notes.
4. Check that a review skill reports evidence and file locations, and that an implementation skill verifies its changes with the target project's checks.
5. Run `git diff --check` and inspect `git status --short` for accidental files.

If an agent run is unavailable, state that limitation and distinguish static review from observed behavior. Add automated checks when executable scripts or repeatable validation justify them; document their commands and dependencies alongside the code.

For installation or packaging changes, run `python3 -m unittest discover -s tests -v` (Python 3.9+, standard library only). These checks use temporary skills and destinations; they do not prove agent discovery or workflow execution. Follow [the installer verification guide](scripts/README.md) and the release guide for those checks. There is no application build or workflow test suite.

### Automated repository checks

[Repository checks](.github/workflows/ci.yml) runs on every push, pull request, and manual dispatch:

- Installer and packaging fixtures on Linux with Python 3.9, and Linux, macOS, and Windows with Python 3.14. These include complete resource copying, safe destination handling, synchronized manifests, and unavailable development catalogs.
- Markdown linting for tracked documentation and future skills, using [.markdownlint-cli2.jsonc](.markdownlint-cli2.jsonc). Long prose lines and fragments without an H1 are allowed.
- GitHub Actions syntax validation with actionlint and whitespace validation across all tracked files.

To repeat the checks locally from the repository root:

```sh
python3 -m unittest discover -s tests -v
npx --yes markdownlint-cli2@0.23.2
actionlint
git diff --check
git diff --check "$(git hash-object -t tree /dev/null)" HEAD
```

Markdown linting requires Node.js 22+ and npm. Install [actionlint 1.7.12](https://github.com/rhysd/actionlint/releases/tag/v1.7.12) to match CI. Actions are pinned to commit SHAs; Dependabot opens grouped weekly update PRs. When updating the Markdown action, align the local CLI version above with its bundled version. Update the actionlint version and archive checksum together in the workflow.

These checks validate files and installer behavior. Fresh-agent scenario runs and release-route verification remain required before advertising skills or installation routes as verified.

## Pull requests

Use the PR template. List changed workflows, meaningful verification results, and remaining limitations. Avoid unrelated cleanup in the same PR.
