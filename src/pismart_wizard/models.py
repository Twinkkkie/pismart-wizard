from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Module:
    name: str
    module_type: str
    address: int
    memory_bytes: int
    settings: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Module":
        return cls(
            name=str(data["name"]),
            module_type=str(data["module_type"]),
            address=int(data["address"]),
            memory_bytes=int(data.get("memory_bytes", 0)),
            settings=dict(data.get("settings", {})),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "module_type": self.module_type,
            "address": self.address,
            "memory_bytes": self.memory_bytes,
            "settings": self.settings,
        }


@dataclass(slots=True)
class Bus:
    name: str
    protocol: str
    modules: list[Module] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Bus":
        return cls(
            name=str(data["name"]),
            protocol=str(data.get("protocol", "industrial-bus")),
            modules=[Module.from_dict(item) for item in data.get("modules", [])],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "protocol": self.protocol,
            "modules": [m.to_dict() for m in self.modules],
        }


@dataclass(slots=True)
class Project:
    name: str
    version: str
    buses: list[Bus] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Project":
        return cls(
            name=str(data["name"]),
            version=str(data.get("version", "1.0")),
            buses=[Bus.from_dict(item) for item in data.get("buses", [])],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "buses": [b.to_dict() for b in self.buses],
        }
