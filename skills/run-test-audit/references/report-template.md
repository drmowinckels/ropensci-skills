# Test-audit report template

The audit produces one self-contained Quarto report, `Review_AI_test_audit.qmd`.
The structure is what makes an AI-assisted audit **auditable**: a reader sees
what was asked, which skill text ran, which model ran it, what was executed, and
what was not. Fill every section — an empty "Not run" or "Skill" section is
itself information.

Copy the skeleton, replace the `<…>` placeholders, and delete guidance in
parentheses.

```markdown
---
title: "<PKG> <VERSION> — AI-Assisted Test-Suite Audit"
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

> <The verbatim request that triggered the audit.>

# Skill

<Reproduce the operative `run-test-audit` instructions verbatim (blockquoted),
plus the skill's version/source. Skill text changes over time; capturing the
version that ran keeps the report self-contained.>

# Report

## Method

<Reproducible detail: R version and package versions (`covr`, `devtools`, the
package itself); how the suite was run and how many times (e.g. "twice with
`devtools::test()`"); how coverage was measured; the offline/mock setup (e.g.
`httptest2` fixtures + dummy credentials) vs. any live path; and an explicit
"No package files were modified." statement.>

## Headline

<One paragraph: the verdict, with the key numbers — pass/fail/skip counts,
timing, coverage %. Then the single most important caveat (e.g. "green, fast,
deterministic — but shallow: 75% of assertions only check that a call runs").>

## A. Coverage gaps

<Untested exports; return values never asserted; documented behaviours never
verified; error branches never exercised. Tag each _(High/Medium/Low.)_ and cite
`file.R:line` or the enumerated surface diff.>

## B. Weak or meaningless tests

<Smoke-only assertions (`expect_no_error()` where a value should be checked),
hollow tests (e.g. an operator-precedence bug that pipes the wrong thing into the
matcher), bare `expect_error()` accepting any error, duplicate assertions. Show
the offending snippet.>

## C. Instability / flakiness

<Time-bombs (tests that will fail on a future date / leap year), wall-clock
coupling, unseeded randomness, global state, order-dependence, hidden skips.
Reproduce where possible and paste the evidence.>

## D. Consistency / maintainability

<Duplicated setup/bootstrap that belongs in `setup.R`/`helper.R`, oversized
`test_that()` blocks that blur failure localization, dead/`.blob` test files,
misleading roxygen-style tags in test files.>

## Verified healthy (no action)

<What is genuinely well done: suite reproducible run-to-run, offline by
construction, no order-dependence, good surface breadth, real assertions correct,
secrets redacted in fixtures. Cite evidence — a fair audit reports strengths too.>

## Coverage snapshot (`covr`, line coverage)

<Total %, then a per-file table (lowest first). Add the caveat that line
coverage reflects breadth, not depth, where that applies.>

| Coverage | File     |
| -------: | -------- |
|   <NN> % | <file.R> |

## Not run (reason)

<Everything not exercised and why: live/paid/network paths not authorized,
credentials unavailable, checks out of scope. A first-class section — silence
here would overstate the audit's coverage.>

## Suggested fix priority

<Ordered, highest-impact first, each item pointing back to the finding IDs above
with a severity — what the author should act on.>
```

## Notes

- **Attribution is required.** The `author` line names both the human accountable
  for the review and the AI harness/model that assisted — rOpenSci reviews are
  signed and non-anonymous.
- **`eval: false` on purpose.** The report is a record of a run, not a live
  notebook; embedding results (not re-execution) is what makes it stable and
  attachable to the public review issue.
