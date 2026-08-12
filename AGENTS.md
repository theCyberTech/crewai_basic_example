# AGENTS.md

## Cursor Cloud specific instructions

This repo is a single **CrewAI JSON-first** project (see `Instructions.md`). It defines one
research agent (`agents/researcher.jsonc`) and one task (`crew.jsonc`) that writes a markdown
report to `output/research_result.md`. There is no web service or GUI — it is a CLI/crew app.

Standard setup/run commands live in `Instructions.md`; the CI validate step is in
`.github/workflows/pylint.yml`. Prefer those sources over duplicating commands here. The notes
below are only the non-obvious gotchas discovered during setup.

- Toolchain: `uv` (installed at `~/.local/bin`, added to `PATH` via `~/.bashrc`/`~/.profile`)
  and the `crewai` CLI (installed via `uv tool install crewai`). Both persist in the VM snapshot;
  the startup update script only runs `uv sync` to refresh the project `.venv` from `uv.lock`.

- Validate / lint (matches CI): `uv run python -c "from crewai.project.json_loader import
  validate_crew_project; validate_crew_project('crew.jsonc')"`. This does NOT call the LLM, so it
  works without an API key.

- Running the crew requires a valid `OPENAI_API_KEY` with access to the `gpt-5.6-luna` model
  (configured in `agents/researcher.jsonc`). Provide it as an environment variable / secret.
  Do NOT leave a `.env` file containing a placeholder key: the JSON-crew runner calls
  `load_dotenv(".env", override=True)`, so a stale placeholder in `.env` will OVERRIDE the real
  injected `OPENAI_API_KEY` env var. Either have no `.env` (the injected env var is used directly)
  or put the real key in `.env`.

- `crewai run` loads this JSON crew because `pyproject.toml` sets
  `[tool.crewai] type = "crew"` and `definition = "crew.jsonc"`. Without `definition`, the CLI
  falls back to the classic `uv run run_crew` entrypoint (which does not exist here). Set
  `CREWAI_DMN_MODE=1` for plain, non-TUI terminal output. The report is written to
  `output/research_result.md`.
