# PIsmart Wizard

Desktop configuration and engineering tool for industrial modular systems, developed as part of commercial software work at PassatInnovation.

> **Portfolio case study.** The original application was developed in a commercial environment. Proprietary source code, customer data, internal configuration files, and company assets are intentionally not published in this repository.

## What the application does

PIsmart Wizard provides a visual workflow for configuring modular industrial systems. A project is modeled through buses and modules, validated before generation, and then used to produce engineering artifacts.

### Core capabilities

- Visual project configuration with buses and hardware modules
- Module settings and connection management
- Project save/load through structured JSON data
- Validation of configuration constraints and naming rules
- Automated configuration generation
- Automated project information generation
- Memory map generation
- Technical specification generation and export
- Engineering document generation from a configured project

## Architecture

The original application was implemented as a Python desktop application using PyQt. Its domain model includes Project, Bus, and Module entities, with dedicated validation, generation, image/resource management, and specification-printing components.

See [Architecture](docs/architecture.md).

## Technology stack

- Python
- PyQt5
- JSON
- openpyxl
- SVG / PDF generation
- PyInstaller
- Git

## My contribution

- Desktop application development in Python/PyQt
- Project configuration model and UI workflows
- Configuration validation
- Generation of configuration files and engineering outputs
- Automated technical specification generation
- Project persistence and restoration
- Packaging and desktop distribution workflow

## Portfolio note

A runnable public demo can be added separately using synthetic modules and sample configuration data, without exposing proprietary company code or internal product data.

## Public demo implementation

This repository also contains a **clean-room portfolio demo** under `src/` using synthetic module data. It was reimplemented from the functional workflow for portfolio purposes and does **not** contain the original employer source code.

The demo models `Project -> Bus -> Module`, validates addressing/naming rules, and generates a small engineering bundle containing project metadata, a memory map, and a specification.

```bash
python -m pip install -e .
pismart-demo examples/sample_project.json --output generated
python -m unittest discover -s tests -v
```

The original commercial application had a PyQt desktop UI and a broader generation pipeline; the public demo intentionally focuses on the domain and generation layer so it remains safe to share.
