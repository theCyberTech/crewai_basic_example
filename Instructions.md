# Basic CrewAI example

This example uses CrewAI's current JSON-first project format. It defines one
research agent in `agents/researcher.jsonc` and one task in `crew.jsonc`. The
task writes a markdown report to `output/research_result.md`.

## Prerequisites

- Python 3.10 through 3.13
- [uv](https://docs.astral.sh/uv/)
- An OpenAI API key with access to `gpt-5.6-luna`

## Install

Install the CrewAI CLI and project dependencies:

```bash
uv tool install crewai
crewai install
```

If `crewai` is not on your `PATH`, run `uv tool update-shell` and restart your
terminal.

Copy the environment template and set your OpenAI API key:

```bash
cp .env.example .env
```

## Run

Run the crew from the repository root:

```bash
crewai run
```

The default topic is configured in `crew.jsonc` under `inputs`. To use a
different topic, edit that value before running the crew. The completed report
is written to `output/research_result.md`.

The researcher uses the OpenAI model `gpt-5.6-luna`, configured in
`agents/researcher.jsonc`.

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

