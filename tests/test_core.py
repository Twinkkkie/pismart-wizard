import json
import tempfile
import unittest
from pathlib import Path

from pismart_wizard.generation import build_memory_map, generate_bundle
from pismart_wizard.models import Project
from pismart_wizard.validation import validate_project


class PISmartDemoTests(unittest.TestCase):
    def setUp(self):
        data = json.loads(Path("examples/sample_project.json").read_text(encoding="utf-8"))
        self.project = Project.from_dict(data)

    def test_valid_demo_project(self):
        self.assertEqual(validate_project(self.project), [])

    def test_memory_map_offsets_are_contiguous(self):
        rows = build_memory_map(self.project)
        self.assertEqual([row["offset"] for row in rows], [0, 16, 32])

    def test_bundle_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = generate_bundle(self.project, tmp)
            self.assertTrue((out / "project_info.json").exists())
            self.assertTrue((out / "memory_map.csv").exists())


if __name__ == "__main__":
    unittest.main()
