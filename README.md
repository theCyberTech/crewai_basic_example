# CrewAI basic example

A JSON-first CrewAI research crew. Agents live in `agents/*.jsonc`, and tasks
plus crew settings live in `crew.jsonc`.

## Running

```bash
crewai install
crewai run
```

The completed report is written to `output/research_result.md`. See
`Instructions.md` for prerequisites, environment setup, and project layout.

## Project structure

- `agents/` — Agent definitions (JSONC)
- `crew.jsonc` — Crew definition with tasks and configuration
- `tools/` — Custom tools (Python)
- `knowledge/` — Knowledge files for agents
- `skills/` — Optional skill files applied to the crew

> **Note:** `custom:<name>` tool references execute `tools/<name>.py` as local
> Python code when the crew loads. Only run crew projects from sources you
> trust.
