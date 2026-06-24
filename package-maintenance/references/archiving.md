# Archiving a Package

Source: <https://devguide.ropensci.org/maintenance_evolution.html> (archiving section)

When a package reaches end of life:

1. **Preserve the old README**: move its content to `README-OLD.md`.
2. **Replace the README** with minimal content plus the right repostatus badge and
   the peer-review badge:
   - **"unsupported"** — for packages that were formerly released.
   - **"abandoned"** — for former concept/WIP packages.
3. **Close issues** with an explanation that links to this guidance.
4. **Archive the repo** in GitHub settings.
5. **Transfer** to the `ropensci-archive` org (or email
   `[email protected]`).

Archived packages can be **unarchived** on request.

## Minimal archived README template

```markdown
# <package name>

[![Project Status: Unsupported](https://www.repostatus.org/badges/latest/unsupported.svg)](https://www.repostatus.org/#unsupported)
[![Peer-review badge](https://badges.ropensci.org/<issue_number>_status.svg)](https://github.com/ropensci/software-review/issues/<issue_number>)

This package has been archived. The former README is now in [README-old](link-to-README-old).
```

Swap the `unsupported` badge for `abandoned` if the package was never released:

```
[![Project Status: Abandoned](https://www.repostatus.org/badges/latest/abandoned.svg)](https://www.repostatus.org/#abandoned)
```
