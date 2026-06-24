# Deprecating and Removing Functions in an rOpenSci Package

The recommended approach follows a staged lifecycle: **deprecate → warn → defunct → remove**, using the `lifecycle` package to signal intent clearly and consistently.

---

## Step 1: Add the `lifecycle` package

Add `lifecycle` to `Imports` in your `DESCRIPTION`:

```r
usethis::use_lifecycle()
```

This also adds the lifecycle badge infrastructure and imports the necessary functions.

---

## Step 2: Mark the function as deprecated

Use `lifecycle::deprecate_warn()` in the function body. Choose the version when the deprecation was introduced:

```r
#' My old function
#'
#' @description
#' `r lifecycle::badge("deprecated")`
#'
#' `old_function()` was deprecated in mypkg 1.2.0. Use [new_function()] instead.
#'
#' @keywords internal
#' @export
old_function <- function(x, y) {
  lifecycle::deprecate_warn(
    when = "1.2.0",
    what = "old_function()",
    with = "new_function()"
  )
  new_function(x, y)
}
```

- `when`: the package version in which deprecation is introduced.
- `what`: the function being deprecated (use `"pkg::fn()"` if cross-package).
- `with`: the replacement (optional, but highly recommended).

The warning fires once per session by default, not on every call, to avoid flooding users.

---

## Step 3: Update NEWS.md

Document the deprecation clearly:

```markdown
## mypkg 1.2.0

### Deprecated functions

- `old_function()` is deprecated; use `new_function()` instead (#issue_number).
```

---

## Step 4: Leave it deprecated for at least one CRAN release cycle

Give users time to migrate — ideally at least one major or minor release, longer for widely-used packages. The rOpenSci guide recommends a minimum of one release after the deprecation warning appears before moving to defunct.

---

## Step 5: Move to defunct (hard stop)

After sufficient warning time, replace the body with `lifecycle::deprecate_stop()`:

```r
#' @description
#' `r lifecycle::badge("defunct")`
#'
#' `old_function()` was deprecated in mypkg 1.2.0 and is now defunct.
#' Use [new_function()] instead.
#'
#' @keywords internal
#' @export
old_function <- function(x, y) {
  lifecycle::deprecate_stop(
    when = "1.2.0",
    what = "old_function()",
    with = "new_function()"
  )
}
```

This throws an error instead of a warning. Keep the function exported so that users who call it get an informative error rather than a "function not found" error.

Document this in NEWS.md:

```markdown
## mypkg 2.0.0

### Defunct functions

- `old_function()` is now defunct. Use `new_function()` instead (#issue_number).
```

---

## Step 6: Remove entirely

After another release cycle (or immediately if this is a major version bump with clear communication), remove the function from the package entirely. At this point, users who call it get `Error: could not find function "old_function"` — which is acceptable because they have had ample notice.

Remove the function's `.R` file or code block, its tests, and its documentation.

---

## Signaling to users who suppress warnings

Some users run `options(lifecycle_verbosity = "quiet")`. To reach them, consider posting migration notes in:

- A package vignette or article (e.g., "Migrating from v1 to v2")
- The pkgdown changelog page
- GitHub Releases

---

## Summary timeline

| Phase     | Mechanism           | User experience                 |
| --------- | ------------------- | ------------------------------- |
| Deprecate | `deprecate_warn()`  | Warning once per session        |
| Defunct   | `deprecate_stop()`  | Error with informative message  |
| Remove    | Delete the function | `could not find function` error |

Keep at least one CRAN release at each phase before advancing to the next, and communicate clearly in NEWS.md and release notes at every step.
