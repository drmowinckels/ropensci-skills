# DESCRIPTION audit for WeatherTools

Here is a review of your `DESCRIPTION` file against rOpenSci packaging standards. Issues are split into **required fixes** (gates that block rOpenSci review) and **recommendations** (strong improvements worth making).

---

## Required fixes

### 1. License is missing

`License: What license is it?` is a placeholder — you must supply a real CRAN- or OSI-accepted license before submission. Common choices:

```
License: MIT + file LICENSE
License: Apache License (>= 2)
License: GPL (>= 3)
```

Use `usethis::use_mit_license()` (or the equivalent for your chosen license) to set this up correctly. It writes the `LICENSE` file and fills in `DESCRIPTION` for you.

### 2. Use `Authors@R`, not `Author`/`Maintainer`

The `Author` and `Maintainer` fields are the old form. rOpenSci requires `Authors@R` with explicit roles. Replace both fields with:

```r
Authors@R: c(
    person("Jane", "Doe",
           email = "jane@example.com",
           role = c("aut", "cre"),
           comment = c(ORCID = "0000-XXXX-XXXX-XXXX"))
)
```

Roles to know: `aut` (author), `cre` (maintainer/creator), `ctb` (contributor), `cph` (copyright holder). Add your ORCID if you have one.

### 3. Move `Depends` to `Imports`

All three packages (`dplyr`, `RCurl`, `rjson`) are listed under `Depends`. rOpenSci requires using `Imports` for packages whose functions you call internally:

```
Imports:
    dplyr,
    RCurl,
    rjson
```

`Depends` attaches packages to the user's search path, which is almost never what you want and pollutes the user's session.

### 4. Replace `RCurl` with a modern HTTP package

`RCurl` is actively discouraged by rOpenSci. Prefer:

- `httr2` (recommended — modern, actively maintained)
- `httr` or `curl` are also acceptable

Switch your HTTP calls to `httr2` and drop `RCurl`.

### 5. Replace `rjson` with `jsonlite`

`rjson` is discouraged. Use `jsonlite` instead — it is the rOpenSci-preferred JSON package and is much more actively maintained.

### 6. Version field is not valid

`Version: 0.1` is not a valid R version string. Use three dot-separated integers:

```
Version: 0.1.0
```

### 7. Description field must not start with "This package"

> "This package provides functions to get weather data."

The `Description` field must not begin with the package name or "This package". Rewrite it to describe what the package actually does, and make it more informative:

```
Description: Provides tools for downloading, parsing, and visualising
    weather data from common meteorological APIs. Supports ...
```

Also: if you reference any external software or service names, single-quote them (e.g., `'OpenWeatherMap'`). Wrap any URLs in angle brackets (`<https://...>`).

---

## Recommendations

### A. Package name uses mixed case

`WeatherTools` contains uppercase letters. rOpenSci strongly recommends short, all-lowercase names (e.g., `weathertools`). Check availability and informativeness with:

```r
pak::pkg_name_check("weathertools")
```

Also search the web to confirm the name is not offensive in other languages and does not conflict with commercial branding.

### B. Title should be more informative

`"Tools for Weather Data in R"` is vague. Title Case is correct, and "in R" is redundant (it is already an R package). Aim for something descriptive:

```
Title: Download and Analyse Meteorological Data from Common Weather APIs
```

### C. Add `URL` and `BugReports` fields

These are expected by rOpenSci and improve discoverability:

```
URL: https://github.com/janedoe/WeatherTools
BugReports: https://github.com/janedoe/WeatherTools/issues
```

---

## Summary of changes

| Field                 | Problem                    | Fix                                           |
| --------------------- | -------------------------- | --------------------------------------------- |
| `License`             | Placeholder text           | Set a real CRAN/OSI license                   |
| `Author`/`Maintainer` | Old form                   | Replace with `Authors@R` (with roles + ORCID) |
| `Depends`             | Wrong field                | Move to `Imports`                             |
| `RCurl`               | Discouraged                | Replace with `httr2`                          |
| `rjson`               | Discouraged                | Replace with `jsonlite`                       |
| `Version`             | Invalid format             | Change to `0.1.0`                             |
| `Description`         | Starts with "This package" | Rewrite to describe functionality directly    |
| Package name          | Mixed case                 | Consider lowercase                            |
| `Title`               | Vague, includes "in R"     | Make more informative, drop "in R"            |
| `URL`/`BugReports`    | Missing                    | Add repository and issue tracker URLs         |
