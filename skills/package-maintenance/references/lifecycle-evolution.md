# Package Evolution & Lifecycle

Source: <https://devguide.ropensci.org/maintenance_evolution.html>

Philosophy: as a package matures, changes to user-facing methods should become
**rare**. Packages that many others depend on must be especially careful. The
`lifecycle` package is **recommended but not required** — base R works too
(`.Deprecated()`, `.Defunct()`, `delayedAssign()`).

## Two-stage function deprecation: deprecate → defunct

1. **Deprecate** (e.g. v0.2.0): mark with `.Deprecated("bar")`. The function still
   runs but emits a **warning**. Add a `pkgname-deprecated` man page listing
   deprecated items.

   ```r
   foo <- function(...) {
     .Deprecated("bar")
     bar(...)
   }
   ```

2. **Defunct** (next release, e.g. v0.3.0): mark with `.Defunct("bar")`. Now it
   throws an **error**. Add `...` to defunct functions so args passed to them yield
   the defunct message rather than "unused argument". Add a `pkgname-defunct` man
   page — **keep this page indefinitely.**

   ```r
   foo <- function(...) {
     .Defunct("bar")
   }
   ```

## Changing argument names

- Strict approach: `stop()` if the old argument is supplied.
- Helpful approach: `warning()` then map the old argument to the new one.
- Caveat: if the function has `...`, a removed parameter is silently absorbed —
  **leave the argument in the signature and throw an error if it's used.**

## Renaming functions

Gradual aliasing:

- First release: keep the old name as an alias/wrapper (optionally warning), and use
  `@rdname` to point it at the new function.
- Later release: remove the old name (following the deprecate → defunct path).

## Deprecating datasets

Use `delayedAssign()` (the Bioconductor 3-step method) so accessing the dataset
emits a warning **and** still returns the data.

## Testing deprecated code

- You don't need to change tests of deprecated functions until they become defunct.
- Do test any behavior changes and, for renames, that old and new give equivalent
  results.
- Once a function is **defunct, remove its tests.**

## Renaming a package

- Early in development a rename is fine (and a chance to comply with naming advice).
- For a CRAN/released package, renaming is **problematic** — CRAN names are
  persistent. Prefer a **new generation** (e.g. `httr` → `httr2`) or an "edition"
  (e.g. `testthat`). Soft-deprecate the old package with a startup message and
  acknowledge reused-code authors in `DESCRIPTION`.
