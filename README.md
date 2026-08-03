# CrewAI basic example

This beginner-friendly example creates one CrewAI agent and one task. The
researcher uses a local [Ollama](https://ollama.com/) model to write five
paragraphs about a configurable topic.

The project follows CrewAI's current
[JSON-first crew structure](https://docs.crewai.com/en/installation):

- `agents/researcher.jsonc` defines the agent.
- `crew.jsonc` defines the task, crew settings, and default input.
- `pyproject.toml` defines the supported Python and CrewAI versions.

## Prerequisites

- Python 3.10 through 3.13
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Ollama](https://ollama.com/download)

Install the CrewAI CLI and download the model:

```bash
uv tool install crewai
ollama pull llama3.2
```

Make sure Ollama is running before starting the crew.

## Install and run

Clone the repository, enter its directory, and install the locked dependencies:

```bash
crewai install
```

The example connects to Ollama through its OpenAI-compatible API. Set these
environment variables in your shell:

```bash
export OPENAI_BASE_URL=http://localhost:11434/v1
export OPENAI_API_KEY=ollama
```

Run the crew:

```bash
crewai run
```

The result is written to `output/research_result.txt`.

## Change the topic

Edit the default `topic` under `inputs` in `crew.jsonc`. You can instead remove
that default; `crewai run` will then prompt for the missing value.

To use another Ollama model, pull it and update the `llm` value in
`agents/researcher.jsonc`. Keep the `openai/` prefix when using Ollama's
OpenAI-compatible endpoint.
