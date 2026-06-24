# Writing and Structuring NEWS.md for an R Package Release

## File requirements

- A `NEWS` or `NEWS.md` file in the package root is **mandatory** for rOpenSci packages.
- Prefer **`NEWS.md`** — it renders nicely on GitHub and CRAN.
- Do **not** add `NEWS.md` to `.Rbuildignore` (plain `NEWS` files should be added).

## Version header format

Each release gets its own header. The required format is:

```
pkgname 0.2.0 (2025-06-23)
==========================
```

The header must include:

- The package name
- The version number (no `v` prefix)
- The release date in parentheses
- A row of `=` characters matching the header width

## Grouping changes under section headings

Organise entries under headings as needed. Standard headings (use those that apply):

- **NEW FEATURES**
- **MINOR IMPROVEMENTS**
- **BUG FIXES**
- **DEPRECATED AND DEFUNCT**
- **DOCUMENTATION FIXES**

Add custom headings for large, coherent groups of changes (e.g., **BREAKING CHANGES**, **PERFORMANCE**).

## Writing individual entries

Each bullet:

- Describes what changed and, where relevant, **why** (user impact, not implementation detail).
- Links the related GitHub issue or PR with `(#12)` — these become clickable hyperlinks in GitHub Release notes.
- Is written in plain language, not imperative/commit style.

Example:

```
# pkgname 0.2.0 (2025-06-23)

## NEW FEATURES

* Added `read_atlas()` function for importing NIfTI-format brain atlases (#45).
* `plot_brain()` now accepts a `palette` argument for custom colour scales (#38).

## BUG FIXES

* Fixed incorrect hemisphere assignment when using symmetric atlases (#51).
* `as_ggseg_atlas()` no longer drops region labels that contain spaces (#49).

## DEPRECATED AND DEFUNCT

* `old_plot()` is deprecated in favour of `plot_brain()` and will be removed
  in the next major release (#33).

## DOCUMENTATION FIXES

* Corrected example in `?read_atlas` that used a removed argument (#55).
```

## Development version suffix

Between releases, carry a `.9000` suffix in `DESCRIPTION` (e.g., `0.2.0.9000`) and add a development header at the top of `NEWS.md`:

```
# pkgname (development version)

* No changes yet.
```

Remove the development header and suffix when preparing the actual release.

## Style reference

Follow the [tidyverse NEWS style guide](https://style.tidyverse.org/news.html) for bullet phrasing, capitalisation, and punctuation. Key points:

- Use sentence case for bullet text.
- End bullets with a period.
- Keep bullets to one or two sentences; link to an issue for detail.
- Avoid restating the function name as the subject when it is clear from context — prefer "Fixed incorrect..." over "`foo()` now correctly...".

## Tooling that helps

```r
# fledge automates NEWS entries from commit messages
fledge::bump_version()   # tags and updates NEWS + DESCRIPTION together
```

The **`fledge`** package can automate NEWS updates by reading commit messages, keeping version, NEWS, and git tags in sync.

## Checklist before release

- [ ] Development header removed; dated version header added.
- [ ] All user-visible changes since the last release are listed.
- [ ] Each entry links its GitHub issue with `(#n)`.
- [ ] Changes are grouped under appropriate headings.
- [ ] Version in `NEWS.md` matches `DESCRIPTION` (no `.9000` suffix).
