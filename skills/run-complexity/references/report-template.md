# Complexity-analysis report template

The analysis produces one self-contained Quarto report, `Review_AI_complexity.qmd`.
The structure is what makes an AI-assisted analysis **auditable**: a reader sees
what was asked, how complexity was measured, which model ran it, what was
executed, and every recommendation's evidence. Fill every section.

Copy the skeleton, replace the `<…>` placeholders, and delete guidance in
parentheses.

```markdown
---
title: "<PKG> <VERSION> — AI-Assisted Code-Complexity Analysis"
author: "<Your Name> (AI-assisted, <harness> / <model>, e.g. Claude Code / Opus 4.8)"
date: <YYYY-MM-DD>
format:
  html:
    toc: true
    toc-depth: 3
    embed-resources: true # self-contained: attachable to the review issue
execute:
  eval: false # the report records results; it is not re-run
---

# Prompt

> <The verbatim request that triggered the analysis.>

# Method

<Say plainly how this pass was done — by the `run-complexity` skill, or by direct
measurement if no skill was used (state which). Then the reproducible detail:
R version and package versions (`cyclocomp`, `devtools`, the package itself);
that per-function metrics came from `cyclocomp::cyclocomp()` on a
`devtools::load_all()`d namespace, plus LOC / nesting / `if`-`for` counts;
that duplication and call-site counts came from a static call-graph over `R/*.R`
via `utils::getParseData()`; that behavioural findings were confirmed with
runtime probes in a scratch session; and an explicit "No package files were
modified." statement.>

# Report

## Measured profile

<A table of the notable functions, then the cc distribution and the one-line
takeaway (e.g. "per-function complexity is fine except one outlier — the real
issue is structural duplication invisible to cyclomatic complexity").>

| Function | Where             |   cc |   LOC | `if` blocks | Verdict            |
| -------- | ----------------- | ---: | ----: | ----------: | ------------------ |
| <fn>     | <internal/export> | <cc> | <loc> |         <n> | <one-line verdict> |

<Distribution of cyclomatic complexity (n = <N>): `(0,2]` → …, `(2,5]` → …, …
Median cc = …; max = …>

## Hotspot N — `<function>` (cc <n>): <one-line characterisation>

<Why it is complex (god-function / deep nesting / repeated block), with a minimal
reproducing snippet. If measuring surfaced a latent bug (inert validation, broken
error path, always-true condition), show it and cite `file.R:line` — these often
matter more than the score.>

### Recommendation

<A concrete refactor that keeps the user-facing surface identical — exported
names, signatures, return types unchanged. Prefer explicit shims over
function-factories so `?help`, autocomplete, and `@inheritParams` keep working.
Show before/after where it clarifies.>

## Minor

<Smaller simplifications not worth a hotspot — duplicate guard blocks, an inflated
but genuinely-simple score to leave alone, etc.>

## User-facing recommendations (API unchanged, but worth noting)

<Genuine discoverability / naming / UX observations, kept clearly separate from
the internal refactors above and marked optional — these are design changes, not
simplifications.>

## Suggested fix priority

<Ordered, highest-impact first, each pointing back to a hotspot with a severity
— what the author should act on. Mark correctness fixes (not cosmetics) as High.>
```

## Notes

- **Measure, then read.** The table is the spine of the report; every hotspot
  should trace back to a number, and every behavioural claim to a reproduced probe.
- **User-facing surface stays fixed.** Internal-refactor recommendations must not
  change the exported API; anything that would is flagged separately as optional.
- **Attribution is required** and **`eval: false` on purpose** — same as the other
  `run-*` reports: the report is a signed, stable record of a run, attachable to
  the public review issue.
