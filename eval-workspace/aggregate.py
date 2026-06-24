#!/usr/bin/env python3
"""Aggregate iteration-1 runs into benchmark.json (schema per skill-creator references/schemas.md).

Reads grading.json (schema {expectations, passed_count, total}) and timing.json
from each eval's with_skill/ and without_skill/ dirs, builds runs[], run_summary,
delta, and analyst notes.
"""
import json, math, pathlib, statistics, datetime, sys

ITER = pathlib.Path(__file__).parent / (sys.argv[1] if len(sys.argv) > 1 else "iteration-1")

CONFIGS = ("with_skill", "without_skill")

# Discover evals dynamically: any subdir with with_skill/grading.json.
# eval_name/eval_id come from eval_metadata.json; skill from its 'skill' field if present.
EVALS = []
for sub in sorted(p for p in ITER.iterdir() if p.is_dir()):
    if not (sub / "with_skill" / "grading.json").exists():
        continue
    meta = {}
    mp = sub / "eval_metadata.json"
    if mp.exists():
        meta = json.loads(mp.read_text())
    EVALS.append((sub.name,
                  meta.get("eval_id", len(EVALS) + 1),
                  meta.get("eval_name", sub.name),
                  meta.get("skill", "")))


def stats(vals):
    if not vals:
        return {"mean": 0.0, "stddev": 0.0, "min": 0.0, "max": 0.0}
    mean = sum(vals) / len(vals)
    sd = statistics.stdev(vals) if len(vals) > 1 else 0.0
    return {"mean": round(mean, 4), "stddev": round(sd, 4),
            "min": round(min(vals), 4), "max": round(max(vals), 4)}


runs = []
per_config = {c: {"pass_rate": [], "time_seconds": [], "tokens": []} for c in CONFIGS}

for ed, eid, name, skill in EVALS:
    for cfg in CONFIGS:
        base = ITER / ed / cfg
        grading = json.loads((base / "grading.json").read_text())
        timing = json.loads((base / "timing.json").read_text())
        passed = grading["passed_count"]
        total = grading["total"]
        pass_rate = round(passed / total, 4) if total else 0.0
        secs = timing.get("total_duration_seconds", 0.0)
        toks = timing.get("total_tokens", 0)
        runs.append({
            "eval_id": eid,
            "eval_name": name,
            "skill": skill,
            "configuration": cfg,
            "run_number": 1,
            "result": {
                "pass_rate": pass_rate,
                "passed": passed,
                "failed": total - passed,
                "total": total,
                "time_seconds": secs,
                "tokens": toks,
                "errors": 0,
            },
            "expectations": grading["expectations"],
            "notes": [],
        })
        per_config[cfg]["pass_rate"].append(pass_rate)
        per_config[cfg]["time_seconds"].append(secs)
        per_config[cfg]["tokens"].append(toks)

run_summary = {c: {"pass_rate": stats(per_config[c]["pass_rate"]),
                   "time_seconds": stats(per_config[c]["time_seconds"]),
                   "tokens": stats(per_config[c]["tokens"])} for c in CONFIGS}

dp = run_summary["with_skill"]["pass_rate"]["mean"] - run_summary["without_skill"]["pass_rate"]["mean"]
dt = run_summary["with_skill"]["time_seconds"]["mean"] - run_summary["without_skill"]["time_seconds"]["mean"]
dk = run_summary["with_skill"]["tokens"]["mean"] - run_summary["without_skill"]["tokens"]["mean"]
run_summary["delta"] = {
    "pass_rate": f"{dp:+.2f}",
    "time_seconds": f"{dt:+.1f}",
    "tokens": f"{dk:+.0f}",
}

# Analyst notes: flag non-discriminating assertions (pass in both configs across all evals)
note_lines = []
by_text = {}
for r in runs:
    for e in r["expectations"]:
        by_text.setdefault(e["text"], {"with": None, "without": None})
        # find which config this run is
    cfg = r["configuration"]
    for e in r["expectations"]:
        by_text[e["text"]][ "with" if cfg == "with_skill" else "without"] = e["passed"]

nondiscriminating = [t for t, v in by_text.items() if v["with"] and v["without"]]
for t in nondiscriminating:
    note_lines.append(f"Assertion '{t}' passes in BOTH configs - does not isolate rOpenSci-specific value.")

# biggest single-eval pass-rate gap (with - without)
gaps = {}
for r in runs:
    g = gaps.setdefault(r["eval_name"], {})
    g[r["configuration"]] = r["result"]["pass_rate"]
gap_list = sorted(((n, v.get("with_skill", 0) - v.get("without_skill", 0)) for n, v in gaps.items()),
                  key=lambda x: -x[1])
if gap_list:
    note_lines.append(
        f"Skill lifts pass rate by {dp:+.0%} on average (with={run_summary['with_skill']['pass_rate']['mean']:.0%}, "
        f"without={run_summary['without_skill']['pass_rate']['mean']:.0%}); biggest single-eval gap is '{gap_list[0][0]}' "
        f"({gap_list[0][1]:+.0%}).")
note_lines.append(
    f"{len(nondiscriminating)} assertion(s) pass in BOTH configs - to the extent these match generic packaging "
    "vocabulary the benchmark understates the skill's rOpenSci-specific value.")
tok_sign = "adds" if dk > 0 else "saves"
note_lines.append(
    f"Skill {tok_sign} {abs(dk):.0f} tokens vs baseline on average and runs {abs(dt):.0f}s "
    f"{'slower' if dt > 0 else 'faster'}; baseline time/tokens vary run-to-run because without the skill the model "
    "explores/searches, while with it the model answers from grounded references.")

benchmark = {
    "metadata": {
        "skill_name": sys.argv[2] if len(sys.argv) > 2 else "ropensci-skills",
        "skill_path": str(pathlib.Path(__file__).parent.parent),
        "executor_model": "claude-sonnet-4-6",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "evals_run": [e[1] for e in EVALS],
        "runs_per_configuration": 1,
    },
    "runs": runs,
    "run_summary": run_summary,
    "notes": note_lines,
}

out = ITER / "benchmark.json"
out.write_text(json.dumps(benchmark, indent=2) + "\n")
print(f"wrote {out}")
print(f"with_skill pass_rate mean={run_summary['with_skill']['pass_rate']['mean']:.2%}  "
      f"without={run_summary['without_skill']['pass_rate']['mean']:.2%}  delta={run_summary['delta']['pass_rate']}")
print(f"non-discriminating assertions: {len(nondiscriminating)}")
