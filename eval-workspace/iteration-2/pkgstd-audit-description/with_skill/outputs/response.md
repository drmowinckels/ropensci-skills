# DESCRIPTION audit for WeatherTools

Here is a review of your `DESCRIPTION` file against rOpenSci packaging standards.
Issues are split into **required fixes** (gates that block review) and **recommendations** (improvements).

---

## Required fixes

### 1. Replace `Author:` with `Authors@R`

The `Author:` field is not accepted by rOpenSci. You must use the structured `Authors@R` field with explicit roles. At minimum you need a creator (`cre`) and an author (`aut`). Add ORCIDs where available.

```r
Authors@R: c(
  person("Jane", "Doe",
         email = "jane@example.com",
         role = c("aut", "cre"),
         comment = c(ORCID = "0000-0000-0000-0000"))
)
```

If Jane Doe is also the copyright holder, add `"cph"` to her roles (or declare a separate `Copyright` field).

### 2. Specify a license

Your `License:` field is missing or unclear ("What license is it?" is not a valid value). You must choose a CRAN- or OSI-accepted license and declare it correctly. Common choices for rOpenSci packages:

```
License: MIT + file LICENSE
```

or `Apache-2.0`, `GPL-3`, etc. Use `usethis::use_mit_license()` (or the equivalent for your chosen license) — it writes the correct `License:` value and creates the `LICENSE` / `LICENSE.md` files.

### 3. Move all packages from `Depends` to `Imports`

`Depends: dplyr, RCurl, rjson` is wrong on two counts:

- **`Depends` should not be used for packages you call internally.** `Depends` attaches the package to the user's search path on load, which pollutes their namespace and can mask their objects. Use `Imports` instead.
- If you genuinely need to expose a dependency's functions to users, import and re-export them explicitly with `#' @importFrom pkg fn` + `#' @export`.

```
Imports:
    dplyr,
    httr2,
    jsonlite
```

(See also point 4 below about which packages to use.)

### 4. Replace `RCurl` and `rjson` with preferred alternatives

rOpenSci explicitly discourages `RCurl` and `rjson` in favour of modern packages:

| Task          | Use instead                                     |
| ------------- | ----------------------------------------------- |
| HTTP requests | `httr2` (preferred) or `httr` / `curl` / `crul` |
| JSON parsing  | `jsonlite`                                      |

`RCurl` is a low-level C binding that is hard to use correctly and has been superseded. `rjson` is slower and less feature-complete than `jsonlite`. Switching now avoids a required change at review time.

### 5. Fix the `Description` field — do not start with "This package"

The `Description` field must not begin with the package name or the phrase "This package". Rewrite to lead with what the package actually does:

```
Description: Provides functions for downloading, parsing, and
    visualising weather data from <https://...>. ...
```

---

## Recommendations

### 6. Title: remove "in R"

Your title is `Tools for Weather Data in R`. The rOpenSci guide says titles should not include "in R" or "with R" — R is already implied by the package context. A cleaner title:

```
Title: Tools for Acquiring and Analysing Weather Data
```

Also confirm it is in Title Case (it is, so that part is fine) and has no trailing period.

### 7. Add `URL` and `BugReports` fields

These are not strictly required but are strongly recommended and expected by rOpenSci reviewers:

```
URL: https://github.com/yourorg/WeatherTools, https://yourorg.github.io/WeatherTools
BugReports: https://github.com/yourorg/WeatherTools/issues
```

### 8. Package name casing

`WeatherTools` uses mixed case. rOpenSci strongly recommends all-lowercase package names (e.g. `weathertools`) for discoverability and consistency. Check availability with `pak::pkg_name_check("weathertools")` before renaming.

### 9. Review whether `dplyr` is truly needed

Fewer dependencies is better. If `dplyr` is used only for a handful of operations (filtering, mutating), consider replacing those calls with base R — `subset()`, `transform()`, `[`, etc. — to avoid pulling in a heavy dependency. If you do keep it, `Imports` (not `Depends`) is still required.

---

## Quick remediation checklist

```r
# Set license
usethis::use_mit_license("Jane Doe")

# After editing DESCRIPTION manually, verify it parses correctly
devtools::check()
```

Then edit `DESCRIPTION` to:

1. Replace `Author:` with `Authors@R:` (structured form above)
2. Change `Depends:` to `Imports:` and swap `RCurl` → `httr2`, `rjson` → `jsonlite`
3. Rewrite `Description:` to not start with "This package"
4. Remove "in R" from `Title:`
5. Add `URL:` and `BugReports:` fields
