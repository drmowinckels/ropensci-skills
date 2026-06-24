#!/usr/bin/env python3
"""Grade batch-2 rOpenSci skill eval runs (stats/release/maintenance/blog).

Same mechanics as grade.py: each assertion passes if ANY regex alternative matches
the response (case-insensitive). Writes grading.json into each run dir and the
assertion list back into eval_metadata.json. Usage: python3 grade2.py [iter-dir]
"""
import json, re, pathlib, sys

ITER = pathlib.Path(__file__).parent / (sys.argv[1] if len(sys.argv) > 1 else "batch2/iteration-1")

ASSERTIONS = {
    "stats-bayesian-submission": [
        ("Says statistical review extends the general package standards", [r"extension|extends|on top of|in addition to|general (package )?standards|normal package requirement"]),
        ("Identifies Bayesian (BS) and/or Regression (RE) standard categories", [r"\bBS\b|\bRE\b|bayesian.*(categor|standard)|regression.*(categor|standard)"]),
        ("Uses the srr package to document standards", [r"\bsrr\b"]),
        ("Mentions @srrstats / @srrstatsTODO / @srrstatsNA tags", [r"@?srrstats(todo|na)?|srrstatsTODO|srrstatsNA"]),
        ("Mentions srr_report() / srr_stats_pre_submit()", [r"srr_report|srr_stats_pre_submit|pre_submit"]),
        ("Recommends running autotest", [r"autotest"]),
        ("Editor verifies via @ropensci-review-bot check srr", [r"check srr|review-bot[^\n]{0,30}srr|srr[^\n]{0,30}review-bot"]),
        ("Mentions graded badges for statistical packages", [r"graded badge|grade[^\n]{0,15}badge|badge[^\n]{0,15}grade|gold|silver|bronze"]),
    ],
    "stats-srr-tags": [
        ("Mentions srr_stats_roxygen() scaffolding the standards file", [r"srr_stats_roxygen|srr-stats-standards|srr_stats_roclet"]),
        ("Mentions @srrstatsTODO placeholder tags", [r"srrstatstodo"]),
        ("Shows the @srrstats satisfied tag", [r"@srrstats\b"]),
        ("Shows the @srrstatsNA not-applicable tag", [r"srrstatsna"]),
        ("Notes the roclet runs on devtools::document() / roxygenise", [r"devtools::document|roxygeni[sz]|roclet|document\(\)"]),
        ("Mentions srr_report() coverage report", [r"srr_report"]),
        ("Mentions srr_stats_pre_submit() completeness gate", [r"srr_stats_pre_submit|pre_submit"]),
    ],
    "release-cran-process": [
        ("Recommends usethis::use_release_issue()", [r"use_release_issue"]),
        ("Recommends devtools::release()", [r"devtools::release|devtools release|::release\("]),
        ("Mentions semantic versioning", [r"semantic version|semver|major\.minor\.patch"]),
        ("Says update NEWS.md", [r"news\.md|news file"]),
        ("Says git-tag each CRAN release", [r"git tag|tag[^\n]{0,20}release|tag[^\n]{0,20}version"]),
        ("Says create a GitHub Release", [r"github release"]),
        ("Says announce via R Weekly", [r"r ?weekly"]),
        ("Mentions CRAN Task View", [r"task view"]),
    ],
    "release-news-file": [
        ("Says NEWS.md in package root (preferred/mandatory)", [r"news\.md"]),
        ("Shows a dated version header", [r"\(\d{4}-\d{2}-\d{2}\)|\d{4}-\d{2}-\d{2}|version header|dated header"]),
        ("Groups items under NEW FEATURES / BUG FIXES / etc.", [r"new features|bug fixes|minor improvements"]),
        ("Mentions DEPRECATED AND DEFUNCT grouping", [r"deprecated and defunct|deprecated|defunct"]),
        ("Links related GitHub issues like (#12)", [r"\(#\d+\)|#\d+|link[^\n]{0,20}issue|issue[^\n]{0,20}number"]),
        ("References the tidyverse NEWS style", [r"tidyverse"]),
        ("Says update before every CRAN release", [r"before (every|each)[^\n]{0,20}release|every release|each release"]),
    ],
    "maintenance-deprecate": [
        ("Describes a two-stage deprecate then defunct process", [r"two[- ]stage|deprecat[^\n]{0,30}defunct|defunct[^\n]{0,30}deprecat|first[^\n]{0,40}deprecat"]),
        ("Mentions .Deprecated() (warns, still works)", [r"\.deprecated|deprecated\(\)"]),
        ("Mentions .Defunct() (errors)", [r"\.defunct|defunct\("]),
        ("Mentions pkgname-deprecated / -defunct help pages", [r"-deprecated|-defunct|deprecated[^\n]{0,15}man|defunct[^\n]{0,15}(man|help)"]),
        ("Suggests the lifecycle package", [r"lifecycle"]),
        ("Notes deprecated warns while defunct errors", [r"warn[^\n]{0,30}error|error[^\n]{0,30}warn|still (works|runs)|throws? an error|stops working"]),
    ],
    "maintenance-takeover": [
        ("Set new maintainer aut+cre, former to aut only", [r"aut[^\n]{0,8}cre|cre[^\n]{0,8}aut|c\(.?aut.?, ?.?cre|role[^\n]{0,15}cre"]),
        ("Update maintainer name everywhere (CITATION/CONTRIBUTING/man)", [r"citation|contributing|man page|everywhere"]),
        ("Old maintainer must email CRAN for an active package", [r"email cran|cran[^\n]{0,20}email|notify cran|contact cran|cran[^\n]{0,20}confirm"]),
        ("Notes no permission needed if archived/orphaned", [r"archived|orphaned|no permission"]),
        ("Mentions rOpenSci newsletter / Call For Contributors", [r"call for contributors|newsletter"]),
        ("Mentions keeping admin access / Slack channel", [r"admin access|slack|package-maintenance"]),
    ],
    "blog-write-submit": [
        ("Distinguishes blog post vs tech note", [r"tech note"]),
        ("Get go-ahead / date from the Community Manager", [r"community manager"]),
        ("Fork the roweb3 repository", [r"roweb3"]),
        ("Post lives in content/blog/YYYY-MM-DD-slug/", [r"content/blog"]),
        ("Knit and commit BOTH source and generated index.md", [r"both[^\n]{0,40}index\.md|index\.md[^\n]{0,40}(source|both|render|knit|generated)|knit[^\n]{0,30}(commit|generated|render)|(render|generated)[^\n]{0,30}index\.md|source[^\n]{0,30}(and|\+)[^\n]{0,20}index\.md"]),
        ("Never use the .RMarkdown format", [r"\.rmarkdown"]),
        ("Put each sentence on its own line", [r"each sentence[^\n]{0,15}line|one sentence[^\n]{0,15}line|sentence per line|sentence on its own line|own line"]),
        ("Use relative URLs for rOpenSci links", [r"relative url|relative link"]),
        ("Every image needs alt text", [r"alt[- ]?text|alternative text"]),
        ("Link the software-review review thread", [r"software-review|review thread"]),
        ("Run roblog checks (ro_lint_md / ro_check_urls)", [r"roblog|ro_lint_md|ro_check_urls"]),
    ],
    "blog-yaml-metadata": [
        ("Author metadata at content/author/ (singular) /_index.md", [r"content/author/|author/[a-z][a-z-]+/_index\.md"]),
        ("Post YAML needs a slug field", [r"\bslug\b"]),
        ("Title should be Title Case", [r"title case"]),
        ("Reuse existing tags rather than invent new ones", [r"reuse[^\n]{0,20}tag|existing tag|tags page"]),
        ("Mentions the ~100-character description", [r"100[- ]?char|~ ?100|100 character"]),
        ("Mentions socialImg / socialAlt fields", [r"socialimg|socialalt"]),
        ("Remove the categories field the addin adds", [r"categories[^\n]{0,40}(remove|delete|addin|automatically|drop)|(remove|delete|drop)[^\n]{0,20}categories|(addin|blogdown)[^\n]{0,30}categories"]),
        ("package_version / Software Peer Review tags for reviewed pkg", [r"package_version|software peer review"]),
    ],
}


def grade_text(text, alts):
    for pat in alts:
        m = re.search(pat, text, re.IGNORECASE | re.DOTALL)
        if m:
            return True, m.group(0)[:160]
    return False, ""


for eval_dir, asserts in ASSERTIONS.items():
    base = ITER / eval_dir
    meta_path = base / "eval_metadata.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())
        meta["assertions"] = [a[0] for a in asserts]
        meta_path.write_text(json.dumps(meta, indent=2) + "\n")
    for config in ("with_skill", "without_skill"):
        resp = base / config / "outputs" / "response.md"
        if not resp.exists():
            print(f"MISSING {resp}")
            continue
        text = resp.read_text()
        expectations = []
        for atext, alts in asserts:
            passed, evidence = grade_text(text, alts)
            expectations.append({"text": atext, "passed": passed, "evidence": evidence})
        grading = {"expectations": expectations,
                   "passed_count": sum(1 for e in expectations if e["passed"]),
                   "total": len(expectations)}
        (base / config / "grading.json").write_text(json.dumps(grading, indent=2) + "\n")
        print(f"{eval_dir}/{config}: {grading['passed_count']}/{grading['total']}")
