# Deprecating a Function in an rOpenSci Package

The rOpenSci Developer Guide recommends a **two-stage process**: deprecate first, then make it defunct in the next release. This gives users at least one release cycle to migrate before the function stops working.

## Stage 1 — Deprecate (e.g. v0.2.0)

Replace the function body with a call to `.Deprecated()`, then delegate to the new function. The function still runs, but emits a **warning**.

```r
foo <- function(...) {
  .Deprecated("bar")
  bar(...)
}
```

At the same time:

- Add a `pkgname-deprecated` roxygen2 man page listing all currently deprecated items. Use `@rdname pkgname-deprecated` on each deprecated function to collect them on one page.
- Update `NEWS.md` to note the deprecation.

## Stage 2 — Defunct (next release, e.g. v0.3.0)

Replace `.Deprecated()` with `.Defunct()`. Now calling the function throws an **error** instead of a warning.

```r
foo <- function(...) {
  .Defunct("bar")
}
```

Key details for defunct functions:

- Keep `...` in the signature. Without it, any arguments the user passes produce a confusing "unused argument" error instead of the clear defunct message.
- Move the item from the `-deprecated` man page to a `pkgname-defunct` man page. **Keep this page indefinitely** — users searching old documentation need to find it.
- Remove the tests for the defunct function (they're no longer meaningful). Do keep tests for any behavior changes and, if this was a rename, tests verifying old and new functions produce equivalent results.

## Using the `lifecycle` package (optional but recommended)

The `lifecycle` package provides a structured, signal-based alternative to `.Deprecated()` / `.Defunct()`. It integrates with rlang's condition system and gives users finer-grained control via `lifecycle::lifecycle_opt()`. The same two-stage logic applies; `lifecycle` just standardises the messaging and adds badges for your documentation.

```r
# Stage 1
foo <- function(...) {
  lifecycle::deprecate_warn("0.2.0", "foo()", "bar()")
  bar(...)
}

# Stage 2
foo <- function(...) {
  lifecycle::deprecate_stop("0.3.0", "foo()", "bar()")
}
```

`lifecycle` is recommended but not required — base R's `.Deprecated()` / `.Defunct()` are fully acceptable.

## If you are renaming the function (not removing it)

Use gradual aliasing:

1. **First release**: keep the old name as a wrapper that calls the new name (optionally with a deprecation warning). Use `@rdname` to point the old name's documentation at the new function.
2. **Later release**: follow the deprecate → defunct path above to remove the old name.

## Changing argument names

- **Strict**: `stop()` immediately if the old argument is supplied.
- **Helpful**: emit a `warning()` and map the old argument to the new one for one release cycle, then error in the next.
- If the function has `...`, **do not silently drop the old argument** — leave it explicitly in the signature and `stop()` if it is used. Otherwise `...` absorbs it silently and users get no feedback.

## Checklist

- [ ] Stage 1: replace body with `.Deprecated("new_name")` + delegation, bump version, update NEWS.md, add/update `-deprecated` man page.
- [ ] Stage 2 (next release): replace with `.Defunct("new_name")`, keep `...` in signature, move entry to `-defunct` man page (keep it forever), remove defunct function's tests, bump version, update NEWS.md.
