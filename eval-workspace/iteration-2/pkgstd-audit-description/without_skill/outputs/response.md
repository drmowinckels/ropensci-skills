# DESCRIPTION Audit: WeatherTools

Here are the issues I found in your `DESCRIPTION` file against rOpenSci packaging standards, ordered by severity.

---

## 1. `Authors@R` is required — replace `Author:` field

**Problem:** You are using the legacy `Author:` plain-text field. rOpenSci (and CRAN) require the structured `Authors@R` field, which captures roles and enables machine-readable authorship.

**Fix:** Replace the `Author:` (and any `Maintainer:`) field with:

```
Authors@R: person("Jane", "Doe", email = "jane@example.com",
    role = c("aut", "cre"))
```

Use `"aut"` for author and `"cre"` for the maintainer/creator. If there are additional contributors, add more `person()` calls separated by `c(...)`.

---

## 2. `License:` must be specified — it appears to be missing or unclear

**Problem:** Your DESCRIPTION does not clearly state a license. This is a required field and a blocker for CRAN submission and rOpenSci review.

**Fix:** rOpenSci strongly recommends permissive licenses. Typical choices:

```
License: MIT + file LICENSE
```

or

```
License: Apache License (>= 2)
```

Pick one, add the field, and (for MIT) add a `LICENSE` file in the package root containing the MIT license text with the correct year and copyright holder.

---

## 3. `Depends:` should almost certainly be `Imports:`

**Problem:** `Depends: dplyr, RCurl, rjson` attaches all three packages into the user's search path when your package loads. This is almost never the right behaviour for non-base packages and is flagged by `R CMD check` as a NOTE, and by rOpenSci reviewers as a design issue.

**Fix:** Move all three to `Imports:`:

```
Imports:
    dplyr,
    RCurl,
    rjson
```

Use `Depends:` only for R itself (e.g. `Depends: R (>= 4.1.0)`) or for packages that define classes your package extends (rare, mostly S4/R5).

---

## 4. Consider replacing `RCurl` and `rjson` with modern alternatives

**Problem:** `RCurl` is a low-level libcurl wrapper that is harder to use correctly and less actively maintained than alternatives. `rjson` similarly has more ergonomic replacements. These are not hard rOpenSci rules, but reviewers will commonly raise them.

**Suggested replacements:**

- `RCurl` → `httr2` (preferred by rOpenSci) or `curl`
- `rjson` → `jsonlite` (more widely used, better maintained)

---

## 5. `Title:` must not end with a period and should be in title case

**Problem:** Your title is `Tools for Weather Data in R`. Two checks:

- It should not end with a period (if it does).
- The word "in" should be lower-case in title case (`Tools for Weather Data in R` is actually fine as-is by title-case rules, where short prepositions are lower-cased).

If the title currently ends with `.`, remove it. Titles also must not include the package name (redundant and flagged by `R CMD check`).

---

## 6. `Description:` must not start with "This package"

**Problem:** Your Description field starts with `"This package …"`. CRAN and rOpenSci both flag this: the description should not refer to the package by name or with "this package" — write as if completing the sentence "The package …" is already implied.

**Fix:** Rewrite the opening sentence. For example, instead of:

```
Description: This package provides tools for downloading and processing
    weather data from public APIs.
```

write:

```
Description: Provides tools for downloading and processing weather data
    from public APIs.
```

---

## Summary checklist

| Field          | Issue                             | Action                                                    |
| -------------- | --------------------------------- | --------------------------------------------------------- |
| `Author:`      | Legacy field                      | Replace with `Authors@R:` using `person()`                |
| `License:`     | Missing/unclear                   | Add a valid SPDX license (recommend `MIT + file LICENSE`) |
| `Depends:`     | Wrong field for non-base packages | Move to `Imports:`                                        |
| `RCurl`        | Outdated dependency               | Consider replacing with `httr2`                           |
| `rjson`        | Less standard                     | Consider replacing with `jsonlite`                        |
| `Description:` | Starts with "This package"        | Rewrite to start with an imperative verb                  |
| `Title:`       | Check for trailing period         | Remove period if present                                  |
