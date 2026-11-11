"""Copy the final held-back run into the product's record folder (step 1), then fingerprint it (step 2, --seal-record).
Usage: python build_record.py            # copy + inputs.sha256 + cost-summary.json
       python build_record.py --fingerprint   # after README.md exists: record.sha256"""
import hashlib, json, os, shutil, sys
W = r"C:\dev\dg-final-2026-11-11"
REC = r"C:\OD\OneDrive - ADVANCED HARMONY ASSOCIATION\METAMORFEUS\DECISION-GRILL\tests\independent-runs\2026-11-11_final-heldback-v1.5"
def sh(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def listing(root, skip=()):
    out = []
    for d, ds, fs in os.walk(root):
        ds.sort()
        for f in sorted(fs):
            p = os.path.join(d, f); rel = "./" + os.path.relpath(p, root).replace("\\", "/")
            if rel in skip: continue
            out.append(f"{sh(p)} *{rel}\n")
    return "".join(out)
if "--fingerprint" in sys.argv:
    assert os.path.exists(os.path.join(REC, "README.md"))
    open(os.path.join(REC, "record.sha256"), "w", encoding="ascii", newline="\n").write(listing(REC, skip=("./record.sha256",)))
    print("record.sha256 lines:", open(os.path.join(REC, "record.sha256")).read().count("\n")); sys.exit()
if os.path.exists(REC): sys.exit("record exists")
os.makedirs(os.path.join(REC, "inputs", "tools")); os.makedirs(os.path.join(REC, "inputs", "heldback"))
shutil.copyfile(os.path.join(W, "instructions_as_run.md"), os.path.join(REC, "inputs", "instructions_as_run.md"))
for f in os.listdir(os.path.join(W, "heldback")):
    shutil.copyfile(os.path.join(W, "heldback", f), os.path.join(REC, "inputs", "heldback", f))
shutil.copyfile(os.path.join(W, "modes.json"), os.path.join(REC, "inputs", "modes.json"))
changed = {}
for f in sorted(os.listdir(os.path.join(W, "tools"))):
    src = os.path.join(W, "tools", f)
    if os.path.isdir(src): continue
    b = open(src, "rb").read()
    if b"<you>" in b:
        nb = b.replace(b"<you>", b"<you>")
        changed[f] = {"before": hashlib.sha256(b).hexdigest(), "after": hashlib.sha256(nb).hexdigest()}
        b = nb
    open(os.path.join(REC, "inputs", "tools", f), "wb").write(b)
json.dump(changed, open(os.path.join(REC, "inputs", "user-name-replaced.json"), "w"), indent=1)
open(os.path.join(REC, "inputs.sha256"), "w", encoding="ascii", newline="\n").write(listing(os.path.join(REC, "inputs")))
# runs (without the empty working directory)
shutil.copytree(os.path.join(W, "runs"), os.path.join(REC, "runs"), ignore=shutil.ignore_patterns("_cwd"))
# readers: their folders without our launcher log and DONE marker, plus the letter key
for r in ("reader1", "reader2"):
    shutil.copytree(os.path.join(W, "readers", r), os.path.join(REC, "readers", r), ignore=shutil.ignore_patterns("DONE.txt", "capped.log"))
shutil.copyfile(os.path.join(W, "readers", "letter-key.json"), os.path.join(REC, "readers", "letter-key.json"))
for f in ("ledger.txt", "analysis-console.txt"):
    shutil.copyfile(os.path.join(W, f), os.path.join(REC, f))
conv = {}
for i in range(1, 5):
    conv[f"SEAL-{i}"] = json.load(open(os.path.join(W, "runs", f"SEAL-{i}", "summary.json")))["cost_usd_total"]
rd = {}
for r in ("reader1", "reader2"):
    t = open(os.path.join(W, "readers", r, "result.json"), encoding="utf-8-sig").read()
    rd[r] = round(json.loads(t[t.find("{"):t.rfind("}") + 1])["total_cost_usd"], 2)
cost = {"conversations": round(sum(conv.values()), 2), "per_conversation": conv, **rd, "runner_check": 0.004}
cost["final_run_total"] = round(cost["conversations"] + rd["reader1"] + rd["reader2"] + 0.004, 2)
cost["all_rounds_with_65.59"] = round(65.59 + cost["final_run_total"], 2)
json.dump(cost, open(os.path.join(REC, "cost-summary.json"), "w"), indent=1)
bad = [os.path.join(d, f) for d, _, fs in os.walk(REC) for f in fs if b"<you>" in open(os.path.join(d, f), "rb").read().upper()]
print("user-name hits in record:", bad)
print("changed tools:", list(changed)); print("cost:", cost)
print("files:", sum(len(fs) for _, _, fs in os.walk(REC)))
