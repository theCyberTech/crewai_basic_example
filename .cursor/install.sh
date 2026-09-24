#!/usr/bin/env bash
# Cloud Agent install step for this JSON-first CrewAI project.
# Idempotent: safe to run repeatedly and against cached/partial state.
set -euo pipefail

# 1. Install uv (Python toolchain) if it is not already present.
if ! command -v uv >/dev/null 2>&1 && [ ! -x "$HOME/.local/bin/uv" ]; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi
export PATH="$HOME/.local/bin:$PATH"

# 2. Persist ~/.local/bin on PATH for interactive agent shells.
for profile in "$HOME/.bashrc" "$HOME/.profile"; do
  if [ -f "$profile" ] || touch "$profile" 2>/dev/null; then
    grep -q '.local/bin' "$profile" 2>/dev/null || \
      echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$profile"
  fi
done

# 3. Install the crewai CLI as a uv tool (skip if already available).
if ! command -v crewai >/dev/null 2>&1; then
  uv tool install crewai
fi

# 4. Sync the project virtualenv from uv.lock.
uv sync

echo "CrewAI dev environment ready. Run the crew with: CREWAI_DMN=1 crewai run"
