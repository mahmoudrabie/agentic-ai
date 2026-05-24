# Contributing

Thanks for helping improve this repository.

## Current priority

The biggest improvement area is moving entries from LinkedIn-only links to canonical resource links. A strong entry should help a GitHub reader reach the original source quickly.

Preferred resource order:

1. Official project page, paper page, arXiv/OpenReview page, benchmark page, docs, or code repository.
2. Optional commentary post from LinkedIn/X/blog.
3. Optional notes explaining why the resource belongs in the selected domain.

## What to contribute
- New high-signal papers, benchmarks, frameworks, or real-world implementations.
- Canonical links for existing LinkedIn-only entries.
- Short summaries, tags, or resource type labels for existing entries.
- Corrections to titles, links, and section placement.
- Improvements to README structure and navigation.

## Contribution rules
- Keep paper titles readable and not stylized with special font encoding.
- Use canonical links whenever possible.
- Keep entries in the most relevant domain README.
- Preserve table format in each domain file.
- Avoid duplicate entries across domains unless there is a clear reason.

## Recommended entry format

When updating a domain page, prefer this richer format for new or upgraded sections:

```md
| Resource | Type | Canonical Link | Commentary |
| --- | --- | --- | --- |
| Example Agent Benchmark | Benchmark | [Paper](https://example.com) / [Code](https://github.com/example/repo) | [Notes](https://example.com/post) |
```

For legacy two-column tables, keep the existing format unless you are converting the whole section in that file.

## How to contribute
1. Fork the repository and create a branch.
2. Update the relevant `README-*.md` file.
3. Run a quick sanity check for broken markdown links and formatting.
4. Run `python3 scripts/audit_resources.py` to review coverage and link concentration.
5. Open a pull request with a clear summary of what changed.

## Pull request checklist
- [ ] Correct section/domain selected.
- [ ] Title is plain readable text.
- [ ] Canonical link opens correctly.
- [ ] Commentary/social link is secondary, not the only source, when a canonical link exists.
- [ ] No duplicate entry added.

## Reporting issues
Open an issue for broken links, incorrect categorization, or formatting regressions.
