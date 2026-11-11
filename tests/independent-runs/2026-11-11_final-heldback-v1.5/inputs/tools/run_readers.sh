#!/usr/bin/env bash
# Runs the two blind readers at the same time (2 processes), each through the memory/time cap.
W="C:/dev/dg-final-2026-11-11"
CL="C:/Users/<you>/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/bin/claude.exe"
one () {
  local r="$1"
  ( cd "$W/readers/$r" && git rev-parse 2>/dev/null && { echo "$r in git repo" >> "$W/readers/progress.txt"; return; }
    python C:/Scripts/capped_run.py --timeout 3000 --mem-mb 2048 --job-mb 3072 --procs 64 -- \
      "$CL" -p "Read task_prompt.md in this folder and do exactly what it says." --model opus \
      --output-format json --permission-mode acceptEdits --allowedTools "Bash(python:*)" \
      > result.json 2> capped.log
    echo "$r exit=$?" >> "$W/readers/progress.txt" )
}
: > "$W/readers/progress.txt"
one reader1 & one reader2 & wait
echo ALL-DONE >> "$W/readers/progress.txt"
