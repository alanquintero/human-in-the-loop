# Releasing the plugin

The current `0.1.0-dev` version is development metadata, not a published release. The marketplace entry is `NOT_AVAILABLE`; the README installation flow is a preview.

## First release

1. Complete the intended skills and catalog them in the README. Run the [contribution checks](../CONTRIBUTING.md), including representative agent scenarios.
2. Set the plugin version for the release and review its identity, license, prerequisites, and package contents. Confirm the marketplace entry resolves to the plugin root and matches its name.
3. Prepare a release commit with the marketplace installation policy set to `AVAILABLE`. Register a local marketplace with `codex plugin marketplace add .`, install through the Plugins Directory, and verify the packaged skills in a fresh chat. Run this in a test setup; registration changes local Codex configuration.
4. Publish the reviewed commit and a matching version tag (for example, `v0.1.0`) with release notes. Verify installation from GitHub in a clean test setup using `codex plugin marketplace add alanquintero/human-in-the-loop --ref v0.1.0`, substituting the actual tag.
5. After installation succeeds, remove the README's unreleased notice, replace the planned instructions with the verified command pinned to the release tag, and record tested client versions. If verification fails, keep the warning and correct the package before announcing availability.

## Later releases

Bump the plugin version when shipped behavior changes. Repeat scenario and installation checks, document behavior changes, publish a matching tag, and update the README's pinned installation command. Development on the default branch must not silently replace the release users installed.
