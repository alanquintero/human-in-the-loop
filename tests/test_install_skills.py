"""Filesystem installation contracts; no agent sessions or real profile writes."""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


REPOSITORY = Path(__file__).resolve().parent.parent
SCRIPT = REPOSITORY / "scripts" / "install-skills.py"
SPEC = importlib.util.spec_from_file_location("install_skills", SCRIPT)
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = self.root / "package"
        (self.package / "scripts").mkdir(parents=True)
        shutil.copy2(SCRIPT, self.package / "scripts" / SCRIPT.name)
        self.source = self.package / "skills"
        self.source.mkdir()
        self.project = self.root / "project with spaces"
        self.project.mkdir()
        self.skill = self.add_skill("sample-workflow")

    def add_skill(self, name):
        skill = self.source / name
        (skill / "references").mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Test fixture only.\n---\n"
            "Read [sample](references/sample.txt).\n", encoding="utf-8"
        )
        (skill / "references" / "sample.txt").write_text("resource\n", encoding="utf-8")
        (skill / "assets").mkdir()
        (skill / "assets" / "sample.bin").write_bytes(bytes(range(256)))
        (skill / "scripts").mkdir()
        helper = skill / "scripts" / "helper.py"
        helper.write_text("#!/usr/bin/env python3\nprint('fixture')\n", encoding="utf-8")
        helper.chmod(0o755)
        return skill

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(self.package / "scripts" / SCRIPT.name), *args],
            cwd=self.root, capture_output=True, text=True, check=False
        )

    def test_project_installation_for_documented_agents(self):
        destinations = {
            "codex": ".agents/skills", "claude": ".claude/skills",
            "copilot": ".github/skills", "cursor": ".cursor/skills",
            "gemini": ".gemini/skills", "windsurf": ".windsurf/skills",
            "cline": ".cline/skills", "opencode": ".opencode/skills",
        }
        for agent, relative in destinations.items():
            with self.subTest(agent=agent):
                result = self.run_cli("--agent", agent, "--scope", "project", "--project", str(self.project))
                self.assertEqual(result.returncode, 0, result.stderr)
                installed = self.project / relative / self.skill.name
                for file in ("SKILL.md", "references/sample.txt", "assets/sample.bin", "scripts/helper.py"):
                    self.assertEqual((installed / file).read_bytes(), (self.skill / file).read_bytes())
                if os.name != "nt":
                    self.assertTrue(os.access(installed / "scripts/helper.py", os.X_OK))

    def test_personal_installation_uses_isolated_home(self):
        destinations = {
            "codex": ".agents/skills", "claude": ".claude/skills",
            "copilot": ".copilot/skills", "cursor": ".cursor/skills",
            "gemini": ".gemini/skills", "windsurf": ".codeium/windsurf/skills",
            "cline": ".cline/skills", "opencode": ".config/opencode/skills",
        }
        for agent, relative in destinations.items():
            with self.subTest(agent=agent):
                home = self.root / f"home-{agent}"
                with mock.patch.object(installer, "__file__", str(self.package / "scripts" / SCRIPT.name)), \
                     mock.patch.object(installer.Path, "home", return_value=home), \
                     contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(installer.main(["--agent", agent, "--scope", "user"]), 0)
                self.assertTrue((home / relative / self.skill.name / "references" / "sample.txt").is_file())

    def test_dry_run_does_not_create_destination(self):
        result = self.run_cli("--agent", "copilot", "--scope", "project", "--project", str(self.project), "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Would copy", result.stdout)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_selection_installs_only_requested_skill(self):
        self.add_skill("another-workflow")
        result = self.run_cli("--agent", "cursor", "--scope", "project", "--project", str(self.project),
                              "--skill", self.skill.name)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([path.name for path in (self.project / ".cursor/skills").iterdir()], [self.skill.name])

    def test_repeatable_selection(self):
        self.add_skill("another-workflow")
        self.add_skill("unselected-workflow")
        result = self.run_cli("--agent", "cline", "--scope", "project", "--project", str(self.project),
                              "--skill", self.skill.name, "--skill", "another-workflow")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({path.name for path in (self.project / ".cline/skills").iterdir()},
                         {self.skill.name, "another-workflow"})

    def test_conflict_prevents_entire_batch_and_preserves_existing_files(self):
        self.add_skill("another-workflow")
        destination = self.project / ".agents/skills"
        existing = destination / self.skill.name
        existing.mkdir(parents=True)
        marker = existing / "keep.txt"
        marker.write_text("keep", encoding="utf-8")
        result = self.run_cli("--agent", "codex", "--scope", "project", "--project", str(self.project))
        self.assertEqual(result.returncode, 1)
        self.assertIn("already exists", result.stderr)
        self.assertEqual(marker.read_text(encoding="utf-8"), "keep")
        self.assertFalse((destination / "another-workflow").exists())

    def test_dangling_symlink_is_a_conflict(self):
        destination = self.project / "skills"
        destination.mkdir()
        try:
            (destination / self.skill.name).symlink_to(self.root / "missing", target_is_directory=True)
        except OSError:
            self.skipTest("Symlink creation unavailable on this OS/profile")
        with self.assertRaisesRegex(ValueError, "already exists"):
            installer.install(self.source, destination)
        self.assertTrue((destination / self.skill.name).is_symlink())

    def test_empty_sources_unknown_names_and_incomplete_skills_do_not_install(self):
        destination = self.project / "skills"
        with self.assertRaisesRegex(ValueError, "Unknown skills"):
            installer.install(self.source, destination, [self.skill.name, "absent"])
        (self.source / "incomplete").mkdir()
        with self.assertRaisesRegex(ValueError, "Missing SKILL.md"):
            installer.install(self.source, destination)
        shutil.rmtree(self.source)
        self.source.mkdir()
        (self.source / ".gitkeep").touch()
        with self.assertRaisesRegex(ValueError, "No skills available"):
            installer.install(self.source, destination)
        self.assertFalse(destination.exists())

    def test_invalid_directory_name_and_recursive_copy_are_rejected(self):
        self.add_skill("Invalid_Name")
        with self.assertRaisesRegex(ValueError, "Invalid skill directory name"):
            installer.install(self.source, self.project / "skills")
        with self.assertRaisesRegex(ValueError, "inside the source"):
            installer.install(self.source, self.skill / "nested", [self.skill.name])
        self.assertFalse((self.skill / "nested").exists())

    def test_scope_arguments_cannot_silently_target_another_location(self):
        for args in (("--scope", "project"),
                     ("--scope", "project", "--project", str(self.root / "absent")),
                     ("--scope", "user", "--project", str(self.project))):
            with self.subTest(args=args):
                result = self.run_cli("--agent", "codex", *args)
                self.assertEqual(result.returncode, 2)
        self.assertEqual(list(self.project.iterdir()), [])


class PackagingTests(unittest.TestCase):
    def read_json(self, relative):
        return json.loads((REPOSITORY / relative).read_text(encoding="utf-8"))

    def test_manifest_metadata_stays_synchronized(self):
        portable = self.read_json("plugin.json")
        claude = self.read_json(".claude-plugin/plugin.json")
        for key in ("name", "version", "description", "author", "repository", "license"):
            with self.subTest(key=key):
                self.assertEqual(portable[key], claude[key])

    def test_unreleased_catalogs_do_not_offer_installation(self):
        portable = self.read_json("plugin.json")
        openai = self.read_json(".agents/plugins/marketplace.json")
        claude = self.read_json(".claude-plugin/marketplace.json")
        self.assertEqual(openai["name"], claude["name"])
        self.assertEqual(openai["plugins"][0]["name"], portable["name"])
        self.assertEqual(openai["plugins"][0]["source"], {"source": "local", "path": "./"})
        if portable["version"].endswith("-dev"):
            self.assertEqual(openai["plugins"][0]["policy"]["installation"], "NOT_AVAILABLE")
            self.assertEqual(claude["plugins"], [])
        else:
            self.assertEqual(claude["plugins"][0]["name"], portable["name"])
            self.assertEqual(claude["plugins"][0]["source"], "./")


if __name__ == "__main__":
    unittest.main()
