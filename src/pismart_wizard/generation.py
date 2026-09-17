from __future__ import annotations

import csv
import json
from pathlib import Path
from .models import Project
from .validation import validate_project


class ProjectValidationError(ValueError):
    pass


def build_memory_map(project: Project) -> list[dict[str, int | str]]:
    rows: list[dict[str, int | str]] = []
    offset = 0
    for bus in project.buses:
        for module in bus.modules:
            rows.append({"bus": bus.name, "module": module.name, "address": module.address, "offset": offset, "size": module.memory_bytes})
            offset += module.memory_bytes
    return rows


def build_specification(project: Project) -> list[dict[str, str | int]]:
    return [{"bus": bus.name, "module": module.name, "type": module.module_type, "address": module.address} for bus in project.buses for module in bus.modules]


def generate_bundle(project: Project, output_dir: str | Path) -> Path:
    issues = validate_project(project)
    if issues:
        raise ProjectValidationError("; ".join(f"{i.code}: {i.message}" for i in issues))
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "project.json").write_text(json.dumps(project.to_dict(), indent=2), encoding="utf-8")
    with (out / "memory_map.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["bus", "module", "address", "offset", "size"])
        writer.writeheader(); writer.writerows(build_memory_map(project))
    with (out / "specification.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["bus", "module", "type", "address"])
        writer.writeheader(); writer.writerows(build_specification(project))
    summary = {"project": project.name, "version": project.version, "bus_count": len(project.buses), "module_count": sum(len(bus.modules) for bus in project.buses), "total_memory_bytes": sum(module.memory_bytes for bus in project.buses for module in bus.modules)}
    (out / "project_info.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return out
