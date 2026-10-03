# Releasing the plugin

The current `0.1.0-dev` version is development metadata, not a published release. The OpenAI marketplace entry is `NOT_AVAILABLE`, the Claude Code catalog is empty, and all [installation instructions](installation.md) are planned.

## First release

1. Complete the intended skills and catalog them in the README. Run the [contribution checks](../CONTRIBUTING.md), including representative agent scenarios.
2. Set the release version in both `plugin.json` and `.claude-plugin/plugin.json`; review identity, license, prerequisites, and package contents. Run the installer/packaging checks in CONTRIBUTING.md. Confirm each catalog's name and source resolve to the plugin root.
3. In an isolated release test checkout, set the OpenAI marketplace policy to `AVAILABLE`. Add `{ "name": "human-in-the-loop", "source": "./" }` to the Claude marketplace's `plugins` array. Keep the development catalogs unavailable until the checks below succeed.
4. Test Codex / ChatGPT Work by registering `codex plugin marketplace add .`, installing through the Plugins Directory, and invoking packaged skills in a fresh chat. Test Claude Code with `claude plugin validate .`, `claude plugin marketplace add .`, and `claude plugin install human-in-the-loop@human-in-the-loop`; invoke `/human-in-the-loop:<skill-name>` and load a bundled resource. Registration changes local agent configuration; use test profiles.
5. For each copy-install route in the installation matrix, install into a temporary consuming project using the script and run a representative skill in that agent. Check personal scope in isolated profiles. Verify resource loading, missing prerequisites, invocation boundaries, and updates/uninstall without affecting unrelated skills. For cloud claims, repeat in that host's remote environment with committed project skills or its documented sync/plugin route.
6. Record agent/client version, model, OS, date, scope, install route, observed results, and skipped checks. Mark each route as tested or unverified in the installation guide; don't infer support for every host or chat surface from a successful copy. Correct failed routes before advertising them as verified.
7. Prepare the release commit with reviewed catalog changes. Publish it and a matching version tag (for example, `v0.1.0`) with release notes. Verify the tagged GitHub source in clean test setups: `codex plugin marketplace add alanquintero/human-in-the-loop --ref v0.1.0`, Claude marketplace registration from a tagged checkout, and the copy installer from the tagged archive. Substitute the actual tag.
8. After the release's advertised routes succeed, remove the README's unreleased notice and replace planned commands with verified commands pinned to the tag. Retain explicit limitations for unverified routes. If verification fails, keep the warning and correct the package before announcing availability.

## Later releases

Bump both plugin manifests' versions when shipped behavior changes. Repeat scenario and installation checks, document behavior changes, publish a matching tag, and update the installation guide's pinned commands. Development on the default branch must not silently replace the release users installed.
