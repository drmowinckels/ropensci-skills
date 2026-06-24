# Submitting Your Government PDF Scraper to rOpenSci

## Is it in scope?

Yes, almost certainly. rOpenSci's scope includes packages that provide **programmatic access to data**, and a package that scrapes and tidies government PDF reports falls squarely into the "data access and retrieval" category. The key criteria are:

- **Data access**: your package retrieves data that researchers would otherwise have to extract manually — this is exactly the kind of friction rOpenSci packages are meant to remove.
- **Scientific use case**: government data used by researchers qualifies as scientific/research data.
- **Reproducibility**: making PDF-locked data programmatically accessible directly supports reproducible research.

If there is any doubt (e.g., the data is highly domain-specific or the package is primarily a wrapper around another R package rather than the source), you can post a pre-submission inquiry on the [rOpenSci forum](https://discuss.ropensci.org) before opening a formal submission. The editors respond quickly and will tell you definitively.

---

## What to do before submitting

### 1. Meet the minimum technical standards

rOpenSci uses the `pkgcheck` tool to automate many of these checks. Run it yourself first:

```r
# install.packages("pkgcheck", repos = "https://ropensci.r-universe.dev")
library(pkgcheck)
pkgcheck()
```

The hard requirements are:

- Pass `R CMD check` with no ERRORs or WARNINGs, and ideally no NOTEs beyond the standard "new submission" note.
- Use **roxygen2** for all documentation.
- Export a complete, documented public API (no undocumented exported functions).
- Include a `README.Rmd` / `README.md` with a clear description, installation instructions, and a minimal worked example.
- Include at least one **vignette** demonstrating real usage.

### 2. Test coverage

rOpenSci expects meaningful test coverage. Use `testthat` and aim for good coverage of your parsing and tidying logic. PDF scraping is tricky to test — the standard approach is to include small, representative sample PDF files in `tests/testthat/` (or `inst/extdata/`) and test against those. Do not rely solely on live downloads in tests; they make tests fragile and slow.

Check coverage with:

```r
covr::package_coverage()
```

### 3. Handle PDF scraping responsibly

Reviewers will look at how you retrieve the PDFs. Make sure:

- You respect `robots.txt` and any terms of service for the government sites you scrape.
- You implement rate limiting or caching so users do not hammer servers.
- If URLs are stable, consider caching downloads (e.g., via `tools::R_user_dir()` or the `rappdirs` package) so repeated calls do not re-download.
- Document clearly which government source(s) the package covers, and include the data licence or terms of use in your documentation.

### 4. User-facing messaging

Use `cli` (not `cat()`, `message()`, or `print()`) for all user-facing output. This is an rOpenSci and tidyverse convention that reviewers enforce.

```r
# Good
cli::cli_inform("Downloading {n} report{?s}...")

# Avoid
message("Downloading ", n, " reports...")
```

### 5. Error handling

Use `rlang::abort()` / `cli::cli_abort()` for errors, not `stop()`. Give informative messages that tell users what went wrong and what to do about it.

### 6. Dependencies

Keep dependencies lean. For PDF scraping, `pdftools` is the standard rOpenSci-friendly choice. If you are using `tabulapdf` (formerly `tabulizer`), note it has a Java dependency which adds friction — document it clearly.

### 7. Lifecycle badges and NEWS.md

- Add a `NEWS.md` file (even if it just records the first release).
- If any functions are experimental or subject to change, mark them with `lifecycle::badge("experimental")`.

### 8. pkgdown site

Build a `pkgdown` site. This is not strictly required but is strongly encouraged and makes the review process smoother:

```r
usethis::use_pkgdown()
pkgdown::build_site()
```

---

## The submission process

1. **Pre-submission inquiry** (optional but recommended if scope is uncertain): open an issue on [ropensci/software-review](https://github.com/ropensci/software-review/issues) using the pre-submission template.
2. **Formal submission**: open an issue on [ropensci/software-review](https://github.com/ropensci/software-review/issues) using the submission template. You will answer a checklist that maps to the points above.
3. **Editor check**: an editor will run `pkgcheck` and confirm the package is ready for review within ~2 weeks.
4. **Peer review**: two reviewers (domain experts + R package experts) will review the package. Reviews are public and conducted in the GitHub issue. Typical turnaround is 4–8 weeks.
5. **Revisions and acceptance**: you respond to reviews, make changes, and the editor approves when satisfied. Your package then gets the rOpenSci badge and is onboarded to the rOpenSci R-universe.

---

## Quick checklist before you submit

- [ ] `R CMD check` passes with 0 errors, 0 warnings
- [ ] `pkgcheck()` passes
- [ ] All exported functions documented with roxygen2
- [ ] `README.md` with install instructions and a working example
- [ ] At least one vignette
- [ ] Tests covering core parsing/tidying logic, using local sample PDFs
- [ ] `NEWS.md` present
- [ ] `cli` used for all user messages
- [ ] PDF source(s) and data licence documented
- [ ] Rate limiting / caching in place for HTTP calls
