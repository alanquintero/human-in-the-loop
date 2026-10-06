# Installer verification

`install-skills.py` uses Python 3.9+ and the standard library. It batch-copies all skills by default. See [local usage and development guide](../docs/local-development.md#batch-copy-all-skills) for unreleased checkout commands and [planned release installation](../docs/installation.md) for tagged-source setup and discovery paths. Native plugin and Gemini link/install commands are separate routes; this script does not register marketplaces, configure tools, or validate full skill metadata.

Run the fixture checks from the repository root:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Fixtures exercise all documented destination paths, complete resource copying, selection, dry runs, conflicts, empty sources, invalid names, missing SKILL.md, and required scope arguments. Packaging checks keep manifest metadata aligned, Codex development installation available, and the unreleased Claude catalog empty. No fixture is shipped as a workflow skill, and tests do not write to real user profiles.

Before advertising a route as tested, follow [CONTRIBUTING.md](../CONTRIBUTING.md) and the [release checklist](../docs/releasing.md): install a real skill in a fresh agent session, verify discovery, invoke it, and load a bundled resource. Record client version, model, OS, date, scope, and observed behavior. A successful filesystem copy alone does not complete these checks.
