# Is your package in scope for rOpenSci, and what do you need to do before submitting?

## Is it in scope?

Almost certainly yes. rOpenSci accepts two categories that directly cover what you describe:

**Data extraction** — packages that retrieve data from unstructured sources such as text, images, and PDFs. The `tabulapdf` package (extracts tables from PDFs) is an established example in this exact category.

**Data retrieval** — packages for accessing and downloading data from online or offline sources with scientific applications. Government publications are a recognised source type; packages like `tidyhydat` (Canadian government hydrometric data) and `read.abares` (Australian government agricultural data) show this is well-trodden ground.

Your package — scraping PDFs from government reports and tidying the data for researchers — sits squarely in data extraction, with elements of data retrieval. Unless your package is really a general-purpose PDF parser with no specific scientific data focus, it fits.

**One edge case to watch:** if the package's primary value is just downloading files (no parsing or tidying), that may not qualify. But since you describe tidying the data for analysis, that concern does not apply here.

**What falls outside scope** (for awareness): data visualisation packages, general computing utilities, statistical/ML modelling libraries, and clients for broad cloud services without additional scientific functionality.

**If you are still uncertain** after reading the scope section of the [Software Peer Review Policies](https://devguide.ropensci.org/softwarereview_policies.html), open a pre-submission inquiry as a GitHub issue on [ropensci/software-review](https://github.com/ropensci/software-review) before submitting. This is the recommended path and editors respond promptly.

---

## What to do before submitting

Work through these areas in roughly this order.

### 1. Confirm you can maintain it

You must be willing and able to maintain the package for at least two years, or be able to identify a replacement maintainer. This is a hard requirement, not a formality.

### 2. Package quality baseline

**R CMD check must be clean.** No errors, no warnings. Notes are acceptable if you can explain them; aim to eliminate them.

**Test coverage must be at least 75%.** Run `covr::package_coverage()` or use a CI coverage report to verify. Tests should cover major functionality and meaningful error paths, not just happy paths.

**Function and API design:**

- Use `snake_case` naming throughout.
- Consider a consistent function prefix (e.g., `gov_` or a short package-name prefix) so your namespace is clear.
- Functions that manipulate data should accept the data object as the first argument (pipe-friendly).
- Avoid `\dontrun{}` in examples; use `\donttest{}` only where needed (e.g., examples requiring network access).

### 3. Documentation

- All exported functions must be documented with roxygen2, including `@return` tags and working `@examples`.
- Add top-level package documentation accessible via `?packagename`.
- Write at least one HTML vignette that walks through a realistic use case end-to-end. This is required, not optional.
- Build a pkgdown site. It does not need to be deployed anywhere fancy, but editors will use it to assess the package.

### 4. README

Your README must include, without requiring the reader to install the package:

- What the package does and who it is for
- Installation instructions
- A short, runnable usage example
- A comparison to similar packages (e.g., `tabulapdf`, `pdftools`) explaining why yours exists or what it adds
- CI badge, test coverage badge, and a [repostatus.org](https://www.repostatus.org/) "Active" badge

### 5. Repository hygiene

- Host on GitHub (not GitLab or Bitbucket — the review process uses GitHub issues).
- Default branch must not be named `master`; rename to `main` if needed.
- Add a CITATION file (`usethis::use_citation()`).
- Add contributor guidelines (`usethis::use_tidy_contributing()` or similar).
- Add a DESCRIPTION `URL` field pointing to your pkgdown site and a `BugReports` field pointing to your issues page.
- Remove scrap files (`.DS_Store`, `.vscode`, `Thumbs.db`, object files) and add them to `.gitignore`.
- Deactivate `renv` if you are using it (it interferes with the review tooling).
- The GitHub repo should not be a fork.

### 6. Licensing

Use a CRAN or OSI-accepted licence. MIT and Apache 2.0 are common choices. If you incorporated code from another source (e.g., a Python scraper you ported), attribute the original author using the `cph` role in `Authors@R`.

### 7. Continuous integration

Set up CI to run R CMD check on at least Linux, macOS, and Windows. The standard approach is [r-lib/actions](https://github.com/r-lib/actions). Add test coverage reporting (e.g., codecov). Badges for both should appear in your README.

### 8. Run pkgcheck

Install and run `pkgcheck` locally:

```r
# install.packages("pkgcheck", repos = "https://ropensci.r-universe.dev")
library(pkgcheck)
checks <- pkgcheck()
summary(checks)
```

The submission system runs this automatically and the editor will see the results. **Your package may only be submitted once the summary shows all ticks and no cross symbols.** Fix everything pkgcheck flags before opening the submission issue.

You can also add the [pkgcheck GitHub Action](https://ropensci.org/blog/2022/02/01/pkgcheck-action/) to your repo to run it on every push.

### 9. Timing considerations

- Submit **before** publishing to CRAN or submitting to a journal (JOSS, MEE). Review may require significant changes, and doing it before CRAN submission avoids having to push a new CRAN version immediately after.
- Do not submit if you are unavailable to respond within a few weeks — the review timeline depends on author responsiveness.
- If you have another package currently under review at rOpenSci, wait for it to complete before submitting a second one.

---

## Submission itself

Once everything above is in order:

1. Go to [github.com/ropensci/software-review](https://github.com/ropensci/software-review) and open a new issue using the **Package Submission** template.
2. Fill in all fields in the template accurately (package name, scope category, links to repo and pkgdown site, short description).
3. Enable GitHub notifications on the issue so you do not miss editor or reviewer comments.

The editor will confirm scope, run pkgcheck, and assign reviewers. Expect the full review process to take two to four months.

---

## Key references

- [Software Peer Review Policies (scope)](https://devguide.ropensci.org/softwarereview_policies.html)
- [Guide for Authors](https://devguide.ropensci.org/softwarereview_author.html)
- [Packaging Guide](https://devguide.ropensci.org/pkg_building.html)
- [pkgcheck documentation](https://docs.ropensci.org/pkgcheck/)
- [software-review repository (for pre-submission inquiries and submissions)](https://github.com/ropensci/software-review)
