# Basic CrewAI example

This example uses CrewAI's current JSON-first project format. It defines one
research agent in `agents/researcher.jsonc` and one task in `crew.jsonc`. The
task writes a markdown report to `output/research_result.md`.

## Prerequisites

- Python 3.10 through 3.13
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/)

Install Ollama, start it, and download the model used by the example:

```bash
ollama pull mistral:7b-instruct-q4_0
```

## Install

Install the CrewAI CLI and project dependencies:

```bash
uv tool install crewai
crewai install
```

If `crewai` is not on your `PATH`, run `uv tool update-shell` and restart your
terminal.

## Run

Run the crew from the repository root:

```bash
crewai run
```

The default topic is configured in `crew.jsonc` under `inputs`. To use a
different topic, edit that value before running the crew. The completed report
is written to `output/research_result.md`.

## Project structure

```text
.
├── agents/
│   └── researcher.jsonc
├── crew.jsonc
├── pyproject.toml
└── output/
```

Sensitive environment files should not be committed. If your setup needs
environment variables, copy `.env.example` to `.env` and edit the values.

See the [CrewAI installation guide](https://docs.crewai.com/en/installation)
and [first crew guide](https://docs.crewai.com/en/guides/crews/first-crew) for
the current project format and CLI commands.

