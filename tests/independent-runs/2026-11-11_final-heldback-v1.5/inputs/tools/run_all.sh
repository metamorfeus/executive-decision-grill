#!/usr/bin/env bash
# Runs SEAL-1..4, two at a time, each through the memory/time cap. Shared ledger stops all at $15.
W="C:/dev/dg-final-2026-11-11"
run_one () {
  local id="$1" mode="$2"
  python C:/Scripts/capped_run.py --timeout 2700 --mem-mb 2048 --job-mb 3072 --procs 64 -- \
    python -I "$W/tools/run_conversation.py" --test-id "$id" --label F --mode "$mode" \
      --scenario-file "$W/heldback/scenarios-held-back.md" --instructions "$W/instructions_as_run.md" \
      --out "$W/runs/$id" --max-usd 5 --ledger "$W/ledger.txt" --stop-total 15 \
    > "$W/runs/$id.log" 2>&1
  echo "$id exit=$?" >> "$W/runs/progress.txt"
}
: > "$W/ledger.txt"; : > "$W/runs/progress.txt"
run_one SEAL-1 "Mode 1 — Decision Grill" & run_one SEAL-2 "Mode 1 — Decision Grill" & wait
run_one SEAL-3 "Mode 2 — Questionnaire" & run_one SEAL-4 "Mode 2 — Questionnaire" & wait
echo ALL-DONE >> "$W/runs/progress.txt"
