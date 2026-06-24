# Writing and Structuring NEWS.md for an R Package Release

## Overview

`NEWS.md` is the user-facing changelog for your R package. It lives in the package root and is displayed on CRAN and rendered by `pkgdown`. It should communicate what changed between versions in plain language aimed at package users, not developers.

---

## File Structure

Each version gets its own top-level heading followed by categorized bullet lists:

```markdown
# packagename 1.2.0

## Breaking changes

- `old_function()` has been removed. Use `new_function()` instead (#123).

## New features

- Added `my_new_function()` to do X (#456).
- `existing_function()` gains a `verbose` argument (#789).

## Bug fixes

- Fixed crash when input contained `NA` values (#101).
- `plot_something()` now respects the `col` argument correctly (#102).

## Minor improvements and fixes

- Improved error messages for invalid inputs.
- Updated documentation for `helper_fn()`.

---

# packagename 1.1.0

## New features

- ...
```

---

## Heading Conventions

- Use `# packagename version` (e.g., `# ggplot2 3.5.0`) for version headings — this is what `usethis::use_news_md()` and CRAN expect.
- Use `## Category` subheadings to group changes. Common categories:
  - **Breaking changes** — anything that removes or incompatibly changes existing behaviour
  - **New features** — new functions, new arguments, new methods
  - **Bug fixes** — corrections to incorrect behaviour
  - **Minor improvements and fixes** — small tweaks, better error messages, documentation updates, internal refactors invisible to users
  - **Deprecations** — functions or arguments deprecated (not yet removed)
  - **Dependencies** — changes to Imports/Suggests/Depends

Not all sections are required for every release — omit empty ones.

---

## Entry Style

Each bullet should:

1. **Name the function or feature** at the start when relevant: `` `my_fun()` now accepts a `timeout` argument. ``
2. **Explain the user impact**, not the implementation: say what changed and why it matters.
3. **Link to the issue or PR** with `(#NNN)` at the end — GitHub auto-links these in rendered Markdown.
4. **Credit external contributors** with `(@username)` when someone outside the maintainer team submitted the fix.

Example:

```markdown
- `read_data()` no longer silently drops rows with missing IDs; it now throws
  an informative error. (#234, @contributor-handle)
```

---

## Development Version Entry

While actively developing toward the next release, keep a `# packagename (development version)` entry at the top:

```markdown
# packagename (development version)

## New features

- Added `experimental_fn()` (#300).
```

When you release, replace this heading with the concrete version number:

```markdown
# packagename 1.3.0
```

`usethis::use_news_md()` sets this up for you; `usethis::use_version()` bumps and updates it.

---

## CRAN Submission Notes

- CRAN displays the top entry from `NEWS.md` in the "NEWS" tab on the package page.
- Keep entries concise. CRAN checks for very long NEWS files and may flag them.
- Avoid HTML in `NEWS.md` — plain Markdown renders fine everywhere.
- For patch releases (e.g. `1.0.1`), a brief entry is fine:

```markdown
# mypkg 1.0.1

- Fixed CRAN check failure on Solaris (#310).
```

---

## Tooling Integration

| Tool                            | What it does                                          |
| ------------------------------- | ----------------------------------------------------- |
| `usethis::use_news_md()`        | Creates `NEWS.md` with the dev heading                |
| `usethis::use_version("minor")` | Bumps version in DESCRIPTION and updates NEWS heading |
| `pkgdown::build_news()`         | Renders `NEWS.md` into the pkgdown site               |
| `devtools::check()`             | Warns if NEWS format is non-standard                  |

---

## Full Minimal Example

```markdown
# mypkg 2.0.0

## Breaking changes

- `compute()` no longer accepts a `method = "old"` argument. Use
  `compute_legacy()` for the previous behaviour (#88).

## New features

- New `batch_compute()` function for processing multiple inputs at once (#90).
- `compute()` gains a `parallel` argument to enable multi-core processing (#91).

## Bug fixes

- Fixed incorrect results when input length was exactly 1 (#85, @jsmith).

## Minor improvements and fixes

- Improved error message when `x` is not numeric.
- `compute()` documentation now includes a worked example.

---

# mypkg 1.5.2

## Bug fixes

- Fixed CRAN NOTE about non-portable file paths (#80).
```

---

## Key Principles

- Write for users, not for the git log — NEWS is not a commit history.
- Breaking changes always get their own section and come first.
- Every user-visible change should have an entry; internal refactors generally do not.
- Issue/PR links (`#NNN`) are essential — they let users trace context.
- Keep the top-of-file entry current as you work; don't batch-write it at release time.
