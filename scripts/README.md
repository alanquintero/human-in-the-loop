# Installer verification

`install-skills.py` uses Python 3.9+ and the standard library. Its CLI and discovery paths are documented in [planned installation](../docs/installation.md). It copies files; it does not register marketplaces, configure tools, or validate full skill metadata.

Run the fixture checks from the repository root:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Fixtures exercise all documented destination paths, complete resource copying, selection, dry runs, conflicts, empty sources, invalid names, missing SKILL.md, and required scope arguments. Packaging checks keep manifest metadata aligned and catalogs unavailable during development. No fixture is shipped as a workflow skill, and tests do not write to real user profiles.

Before advertising a route as tested, follow [CONTRIBUTING.md](../CONTRIBUTING.md) and the [release checklist](../docs/releasing.md): install a real skill in a fresh agent session, verify discovery, invoke it, and load a bundled resource. Record client version, model, OS, date, scope, and observed behavior. A successful filesystem copy alone does not complete these checks.
