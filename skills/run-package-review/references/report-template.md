# Review report template

Every review pass produces one self-contained Quarto report, `Review_AI_<pass>.qmd`
(e.g. `Review_AI_test_audit.qmd`). The structure below is what makes an
AI-assisted review **auditable**: a reader can see exactly what was asked, which
skill text ran, which model ran it, what was executed, and what was not. Fill
every section — an empty "Not run" or "Skill" section is itself information.

Copy the skeleton, replace the `<…>` placeholders, and delete guidance in
parentheses.

```markdown
---
title: "<PKG> <VERSION> — AI-Assisted <Pass> (e.g. Test-Suite Audit)"
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

> <The verbatim prompt/request that triggered this pass. Quote it exactly —
> this is the "what was asked" half of transparency.>

# Skill

<Which skill(s) drove this pass, and their version/source. Because skill text
changes over time, reproduce the operative instructions verbatim (blockquoted)
so the report is self-contained. If no skill was used, say so explicitly and
describe the method that replaced it.>

# Report

## Method

<Exactly what was run, so the pass is reproducible:

- tools and versions (R version, package versions, `covr`/`cyclocomp`/… );
- commands executed and how many times (e.g. "suite run twice with
  `devtools::test()`"; "coverage via `covr::package_coverage()`");
- the offline/mock setup vs. any live path;
- an explicit "No package files were modified." statement.>

## Headline

<One paragraph: the verdict. The single most important thing a reader should
take away, with the key number(s). Lead with green/amber/red reality, then the
one caveat that matters most.>

## Findings

<Group findings into labelled buckets appropriate to the pass, and tag each with
a severity — _(High.)_ / _(Medium.)_ / _(Low.)_. Every finding cites evidence:
a `path/file.R:line`, a command's output, or a reproduced probe. Suggested
buckets by pass:

- Test audit → **A** Coverage gaps · **B** Weak/meaningless tests ·
  **C** Instability/flakiness · **D** Consistency/maintainability
- Complexity → **Measured profile** (table: fn · cc · LOC · verdict) then one
  **Hotspot N** subsection per offender, each with a minimal reproducing
  snippet and a concrete refactor that keeps the user-facing surface unchanged
- Dependencies → **Tier 1** clear wins · **Tier 2** worth doing · **Tier 3**
  defer · **Keep** (removal buys nothing)
- Performance → measured hot paths, each with before/after evidence

Prefer tables for profiles/inventories; prefer fenced code for reproducing
snippets. Never assert a defect you have not shown.>

## Verified healthy (no action)

<The positive findings — what is genuinely well done. A review that only lists
problems is neither fair nor trustworthy. Cite evidence here too.>

## Not run (reason)

<Everything that was NOT exercised and why: live/paid/network paths not
authorized, environments unavailable, checks out of scope. This is a
first-class section — silence here would overstate the review's coverage.>

## Suggested fix priority

<An ordered, actionable list — highest-impact first — each item pointing back to
the finding IDs above with a severity. This is what the author acts on.>
```

## Notes

- **One pass, one file.** Keep each report focused; don't fold four audits into
  one document. The filename records the pass.
- **Attribution is required, not decorative.** The `author` line names both the
  human accountable for the review and the AI harness/model that assisted —
  rOpenSci reviews are signed and non-anonymous.
- **`eval: false` on purpose.** The report is a record of a run, not a live
  notebook; embedding results (not re-execution) is what makes it attachable and
  stable.
