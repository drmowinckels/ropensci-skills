# DESCRIPTION Audit Against rOpenSci Packaging Standards

Here are the issues found in your `DESCRIPTION` file, ordered by severity.

---

## 1. `License` — placeholder must be replaced (blocking)

```
License: What license is it?
```

This is not a valid SPDX license identifier. rOpenSci strongly recommends permissive licenses. Pick one and replace the field:

```
License: MIT + file LICENSE
```

or

```
License: Apache License (>= 2)
```

MIT is the most common choice for rOpenSci packages. If you use `MIT + file LICENSE`, you must also create a `LICENSE` file in the package root containing the MIT license text with your name and year filled in.

---

## 2. `Version` — must follow three-part semantic versioning

```
Version: 0.1
```

R requires at least a two-part version, but rOpenSci (and CRAN) expect three parts:

```
Version: 0.1.0
```

---

## 3. `Author` — use the `Authors@R` field instead of `Author` + `Maintainer`

The `Author` / `Maintainer` pair is the old format. rOpenSci standards (and current CRAN policy) require `Authors@R`, which uses `person()` objects and supports ORCID IDs:

```
Authors@R: person("Jane", "Doe", email = "jane@example.com",
    role = c("aut", "cre"),
    comment = c(ORCID = "0000-0000-0000-0000"))
```

- `"aut"` — author
- `"cre"` — maintainer (creator); exactly one person must hold this role
- ORCID is optional but encouraged by rOpenSci

When you switch to `Authors@R`, remove both the `Author:` and `Maintainer:` fields entirely.

---

## 4. `Description` — too vague; must be a full, informative sentence

```
Description: This package provides functions to get weather data.
```

rOpenSci requires a description that explains _what_ the package does, _for whom_, and ideally _how_. It should be at least one full paragraph. Avoid starting with "This package":

```
Description: Provides functions to download, parse, and visualise
    weather observations and forecasts from public APIs (e.g.,
    Open-Meteo, NOAA). Designed for researchers and analysts who
    need reproducible access to meteorological data directly from R.
```

Also note: the `Description` field should be wrapped at 80 characters with hanging indentation (four spaces) for multi-line text.

---

## 5. `Depends` — move packages to `Imports` unless absolutely required

```
Depends: dplyr, RCurl, rjson
```

`Depends` attaches packages to the user's search path when your package is loaded, which is almost never the right behaviour and pollutes the user's session. rOpenSci policy (and CRAN policy) is:

- Use `Imports:` for packages your code calls internally.
- Use `Depends:` only if your package genuinely extends another (e.g., a package that subclasses `ggplot2` objects).

Additionally, consider these package substitutions:

| Current | Recommended alternative  | Reason                                                                    |
| ------- | ------------------------ | ------------------------------------------------------------------------- |
| `RCurl` | `httr2` (or `curl`)      | `RCurl` is legacy; `httr2` is the modern rOpenSci-recommended HTTP client |
| `rjson` | `jsonlite`               | `jsonlite` is more robust, widely used in the rOpenSci ecosystem          |
| `dplyr` | keep if used extensively | acceptable, but prefer `Imports`                                          |

```
Imports:
    dplyr,
    httr2,
    jsonlite
```

---

## 6. `Title` — capitalise as a title, not a sentence

```
Title: Tools for Weather Data in R
```

This is actually fine in capitalisation. However, rOpenSci style asks you not to end the title with a period, and not to include "R" or "package" in it unless strictly necessary (the context already implies R). Consider shortening:

```
Title: Tools for Weather Data
```

If the focus is a specific API or dataset, be more specific:

```
Title: Download and Process Meteorological Data from Public APIs
```

---

## 7. Missing recommended fields

rOpenSci packages should also include:

```
URL: https://github.com/yourusername/WeatherTools,
    https://yourusername.github.io/WeatherTools
BugReports: https://github.com/yourusername/WeatherTools/issues
Encoding: UTF-8
RoxygenNote: 7.x.x   # filled in automatically by devtools::document()
```

`Encoding: UTF-8` is required for CRAN submission and expected by rOpenSci.

---

## Corrected `DESCRIPTION`

```
Package: WeatherTools
Type: Package
Title: Download and Process Meteorological Data from Public APIs
Version: 0.1.0
Authors@R: person("Jane", "Doe", email = "jane@example.com",
    role = c("aut", "cre"),
    comment = c(ORCID = "0000-0000-0000-0000"))
Description: Provides functions to download, parse, and visualise
    weather observations and forecasts from public APIs. Designed
    for researchers and analysts who need reproducible access to
    meteorological data directly from R.
License: MIT + file LICENSE
Encoding: UTF-8
URL: https://github.com/yourusername/WeatherTools,
    https://yourusername.github.io/WeatherTools
BugReports: https://github.com/yourusername/WeatherTools/issues
Imports:
    dplyr,
    httr2,
    jsonlite
```

---

## References

- [rOpenSci Packaging Guide — Package Metadata](https://devguide.ropensci.org/pkg_building.html#metadata)
- [Writing R Extensions — The DESCRIPTION file](https://cran.r-project.org/doc/manuals/R-exts.html#The-DESCRIPTION-file)
- [CRAN Repository Policy](https://cran.r-project.org/web/packages/policies.html)
