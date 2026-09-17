from __future__ import annotations

from dataclasses import dataclass
from .models import Project


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str
    message: str
    location: str


def validate_project(project: Project) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    seen_bus_names: set[str] = set()
    seen_module_names: set[str] = set()
    if not project.name.strip():
        issues.append(ValidationIssue("project.name.empty", "Project name is required.", "project"))
    if not project.buses:
        issues.append(ValidationIssue("project.buses.empty", "At least one bus is required.", "project"))
    for bus_index, bus in enumerate(project.buses):
        bus_location = f"buses[{bus_index}]"
        if bus.name in seen_bus_names:
            issues.append(ValidationIssue("bus.name.duplicate", f"Duplicate bus name: {bus.name}", bus_location))
        seen_bus_names.add(bus.name)
        seen_addresses: set[int] = set()
        for module_index, module in enumerate(bus.modules):
            location = f"{bus_location}.modules[{module_index}]"
            if module.name in seen_module_names:
                issues.append(ValidationIssue("module.name.duplicate", f"Duplicate module name: {module.name}", location))
            seen_module_names.add(module.name)
            if module.address in seen_addresses:
                issues.append(ValidationIssue("module.address.duplicate", f"Duplicate address {module.address} on bus {bus.name}", location))
            seen_addresses.add(module.address)
            if module.address < 0 or module.address > 247:
                issues.append(ValidationIssue("module.address.range", "Address must be in the range 0..247.", location))
            if module.memory_bytes < 0:
                issues.append(ValidationIssue("module.memory.negative", "Memory size cannot be negative.", location))
    return issues
