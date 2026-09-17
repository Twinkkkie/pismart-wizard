from __future__ import annotations

import argparse
import json
from pathlib import Path
from .generation import generate_bundle
from .models import Project


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a synthetic PIsmart engineering bundle.")
    parser.add_argument("project", type=Path)
    parser.add_argument("--output", type=Path, default=Path("generated"))
    args = parser.parse_args()
    project = Project.from_dict(json.loads(args.project.read_text(encoding="utf-8")))
    output = generate_bundle(project, args.output)
    print(f"Generated portfolio demo artifacts in: {output.resolve()}")


if __name__ == "__main__":
    main()
