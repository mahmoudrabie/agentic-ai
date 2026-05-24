#!/usr/bin/env python3
"""Audit resource coverage and link concentration for the curated READMEs."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
README_PATTERN = "README-*.md"
RESOURCE_ROW = re.compile(r"^\| (?P<title>.+?) \| (?P<link>\[Link\]\((?P<url>https?://[^)]+)\)) \|$")
URL = re.compile(r"https?://[^) \n]+")
SOCIAL_HOSTS = {"www.linkedin.com", "linkedin.com", "uk.linkedin.com", "x.com", "twitter.com"}


def domain_name(path: Path) -> str:
    name = path.stem.removeprefix("README-")
    return name.replace("-", " ").title()


def main() -> int:
    resources = []
    all_hosts = Counter()

    for path in sorted(ROOT.glob(README_PATTERN)):
        if path.name == "README.md":
            continue

        count = 0
        for line in path.read_text(encoding="utf-8").splitlines():
            match = RESOURCE_ROW.match(line)
            if not match:
                for raw_url in URL.findall(line):
                    all_hosts[urlparse(raw_url).netloc] += 1
                continue

            count += 1
            url = match.group("url")
            host = urlparse(url).netloc
            all_hosts[host] += 1
            resources.append((domain_name(path), match.group("title"), url, host))

        if count == 0:
            print(f"warning: no resource rows found in {path.name}")

    by_domain = Counter(domain for domain, _, _, _ in resources)
    social_only = [item for item in resources if item[3] in SOCIAL_HOSTS]

    print(f"total_resources={len(resources)}")
    print(f"social_primary_links={len(social_only)}")
    print()
    print("resources_by_domain:")
    for domain, count in by_domain.most_common():
        print(f"  {count:3d} {domain}")

    print()
    print("top_link_hosts:")
    for host, count in all_hosts.most_common(10):
        print(f"  {count:3d} {host}")

    print()
    print("thin_domains:")
    for domain, count in sorted(by_domain.items()):
        if count < 5:
            print(f"  {count:3d} {domain}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

