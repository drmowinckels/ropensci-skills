# Taking Over Maintenance of an rOpenSci Package

Taking over an rOpenSci package involves changes across several areas: package metadata, repository permissions, communication channels, and community expectations. Here is a practical checklist.

---

## 1. Coordinate with the Outgoing Maintainer

- Get a formal handover — ideally in writing (GitHub issue or email) so there is a record.
- Ask for access to any accounts or services tied to the package (CRAN, r-universe, CI tokens, any API keys stored as secrets).
- Clarify whether they want to remain as a co-author or be removed from the author list.
- Understand any known issues, planned features, or in-flight PRs.

---

## 2. Update DESCRIPTION

This is the most visible change. At minimum:

```r
# Change or add yourself as maintainer
person("Your", "Name", email = "you@example.com", role = c("aut", "cre"))

# Demote the outgoing maintainer to author-only (remove "cre")
person("Former", "Maintainer", role = "aut")
```

- The `Maintainer:` field in the installed package is derived from the `person()` with `role = "cre"`. Only one person can hold `cre` at a time.
- Update `BugReports:` and `URL:` if the repository is moving.

---

## 3. Repository Access and Ownership

- **GitHub:** Have the outgoing maintainer transfer ownership or add you as an admin. For rOpenSci packages, the repo typically lives under the `ropensci` GitHub organisation — contact the rOpenSci team (via the `#package-maintenance` Slack channel or the forum) to get admin rights added.
- **Branch protection rules:** Review and adjust if needed.
- **GitHub Actions secrets:** Re-add any secrets under your own tokens (e.g. `GITHUB_TOKEN` is automatic, but `CODECOV_TOKEN` or `CRAN_*` tokens are not).

---

## 4. CRAN

- Email `cran@r-project.org` to notify them of the maintainer change before your next submission — CRAN sends policy emails to the address in DESCRIPTION, so they need to know who is responsible.
- The next submission with the updated `Maintainer:` field will propagate the change automatically, but a heads-up email avoids confusion.
- If the package is on CRAN and has been archived or flagged, address those issues promptly.

---

## 5. rOpenSci-Specific Steps

- Notify the rOpenSci team via the **rOpenSci forum** or Slack (`#package-maintenance` channel). They maintain a registry and can update metadata on the rOpenSci website.
- The [rOpenSci Software Review](https://ropensci.org/software-review/) issue for the package (if it exists) should be updated — comment there to note the handover.
- Check the [rOpenSci software registry](https://ropensci.org/packages/) entry; the team will update it once notified.
- Familiarise yourself with the [rOpenSci Packages Guide](https://devguide.ropensci.org/) — it covers maintenance expectations, packaging standards, and the annual review process.

---

## 6. Communication Channels

- **GitHub Issues:** Pin a comment or edit the README to announce the new maintainer.
- **README:** Update any "maintainer" badges or contact info.
- **NEWS.md:** Add an entry noting the maintainer change in the next release.
- **Mailing lists / forums:** If the package has a dedicated community space, post there too.

---

## 7. Continuous Integration

- Review all CI workflows (`.github/workflows/`). Tokens or secrets tied to the former maintainer's accounts will stop working.
- Re-generate and store secrets under your own account:
  - Codecov tokens
  - Any deployment keys
  - `r-universe` or `pkgdown` deployment tokens
- Check that `pkgdown` site deploys correctly — the `gh-pages` branch and GitHub Pages settings may need adjustment.

---

## 8. Review Open Issues and PRs

- Triage open issues: close stale ones with a note, label the rest.
- Review open PRs: decide which to merge, request-changes on, or close.
- Set expectations in a pinned issue or CONTRIBUTING.md about response time and scope.

---

## 9. Package Infrastructure Health Check

Run a full check before making any substantive changes so you know the baseline:

```r
# From the package root
devtools::check()
```

Also run:

```r
rcmdcheck::rcmdcheck(args = "--as-cran")
```

Fix any existing `WARNING` or `ERROR` level issues before adding new features — you do not want to inherit silent failures.

---

## 10. Update pkgdown / Documentation Site

- `_pkgdown.yml`: update author info, URLs, and social links.
- Rebuild and redeploy the site.
- Update the `pkgdown` `home.links` section if it points to the old maintainer's profile.

---

## 11. Understand the Codebase and Dependencies

- Read the full DESCRIPTION to understand declared dependencies and their versions.
- Run `devtools::install_deps()` and verify everything resolves.
- Identify packages in `Imports`, `Suggests`, and `Enhances` — track their own maintenance status (are any also unmaintained?).
- Review the test suite coverage to understand what is and is not tested.

---

## 12. Set Expectations Publicly

Update or create a `CONTRIBUTING.md` that states:

- Your response-time goal for issues and PRs
- The scope you plan to maintain (bug fixes only vs. new features)
- How to report security vulnerabilities

---

## Summary Checklist

| Area          | Action                                                 |
| ------------- | ------------------------------------------------------ |
| DESCRIPTION   | Update `cre` role, demote outgoing maintainer to `aut` |
| CRAN          | Email cran@r-project.org about maintainer change       |
| GitHub        | Get admin access, rotate secrets                       |
| rOpenSci      | Notify team via forum/Slack, update registry           |
| CI/CD         | Re-add tokens, verify all workflows pass               |
| README / NEWS | Announce change publicly                               |
| Issues/PRs    | Triage backlog                                         |
| pkgdown       | Update author info, redeploy                           |
| R CMD check   | Establish clean baseline before changes                |
