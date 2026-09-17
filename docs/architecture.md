# Architecture

```mermaid
flowchart LR
    UI[PyQt Desktop UI] --> Project[Project Model]
    Project --> Bus[Bus]
    Bus --> Module[Module]
    UI --> Validator[Project Validator]
    Validator --> Project
    UI --> Generator[Project Generator]
    Generator --> Config[Configuration Files]
    Generator --> Info[Project Info]
    Generator --> Memory[Memory Map]
    Generator --> Spec[Technical Specification]
    Project --> JSON[Project JSON]
```

The original commercial application used separate domain entities (`Project`, `Bus`, `Module`) and supporting components for validation, generation, resource management, and specification printing. The public demo keeps only a synthetic version of the domain and generation layers.
