#!/usr/bin/env python3
"""Validate the public catalog without requiring third-party packages."""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "data" / "apps"
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_STATUS = {"existing", "planned", "consolidate"}
ALLOWED_OPEN_SOURCE_STATUS = {"open-source", "license-needed", "planned"}
ALLOWED_EVIDENCE = {"author-claimed", "maintainer-verified", "unverified"}
REQUIRED = {
    "slug",
    "name",
    "status",
    "category",
    "repoUrl",
    "license",
    "openSourceStatus",
    "maintainer",
    "paidAlternatives",
    "sourceDirectory",
    "description",
    "features",
    "limitations",
    "dependencies",
    "vibeCodedEvidence",
    "vibeCodedEvidenceUrl",
    "lastVerified",
}
def fail(path: Path, message: str) -> None:
    raise ValueError(f"{path.relative_to(ROOT)}: {message}")


def is_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def require_string(record: dict, key: str, path: Path, minimum: int = 1) -> str:
    value = record.get(key)
    if not isinstance(value, str) or len(value.strip()) < minimum:
        fail(path, f"{key} must be a non-empty string")
    return value


def require_list(record: dict, key: str, path: Path, minimum: int = 0) -> list:
    value = record.get(key)
    if not isinstance(value, list) or len(value) < minimum:
        fail(path, f"{key} must be a list with at least {minimum} item(s)")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        fail(path, f"{key} must contain non-empty strings")
    return value


def validate_record(path: Path, record: object) -> str:
    if not isinstance(record, dict):
        fail(path, "top-level value must be an object")
    missing = REQUIRED - record.keys()
    if missing:
        fail(path, f"missing required fields: {', '.join(sorted(missing))}")

    unknown = set(record) - REQUIRED - {"demoUrl", "notes"}
    if unknown:
        fail(path, f"unknown fields: {', '.join(sorted(unknown))}")

    slug = require_string(record, "slug", path)
    if not SLUG_PATTERN.fullmatch(slug):
        fail(path, "slug must use lowercase letters, numbers, and hyphens")
    if path.stem != slug:
        fail(path, "slug must match the filename")

    require_string(record, "name", path, 2)
    require_string(record, "category", path, 2)
    require_string(record, "maintainer", path)
    description = require_string(record, "description", path, 20)
    require_string(record, "license", path)
    require_list(record, "paidAlternatives", path, 1)
    require_list(record, "features", path, 1)
    require_list(record, "limitations", path, 1)
    require_list(record, "dependencies", path)

    status = record["status"]
    if status not in ALLOWED_STATUS:
        fail(path, f"status must be one of {sorted(ALLOWED_STATUS)}")

    open_source_status = record["openSourceStatus"]
    if open_source_status not in ALLOWED_OPEN_SOURCE_STATUS:
        fail(
            path,
            "openSourceStatus must be one of "
            f"{sorted(ALLOWED_OPEN_SOURCE_STATUS)}",
        )

    repo_url = record["repoUrl"]
    if repo_url is not None and not is_url(repo_url):
        fail(path, "repoUrl must be an http(s) URL or null")
    if status in {"existing", "consolidate"} and repo_url is None:
        fail(path, "existing and consolidate entries need a repoUrl")
    if status == "planned" and repo_url is not None:
        fail(path, "planned entries must use repoUrl: null")
    if status == "planned" and open_source_status != "planned":
        fail(path, "planned entries must use openSourceStatus: planned")
    if open_source_status == "open-source" and record["license"].strip().lower() in {
        "tbd",
        "unknown",
        "no license",
        "license needed",
    }:
        fail(path, "open-source entries need a recognizable license")

    demo_url = record.get("demoUrl")
    if demo_url is not None and not is_url(demo_url):
        fail(path, "demoUrl must be an http(s) URL or null")

    source = record["sourceDirectory"]
    if not isinstance(source, dict) or set(source) != {"name", "url", "slugs"}:
        fail(path, "sourceDirectory must contain name, url, and slugs only")
    require_string(source, "name", path)
    if not is_url(source.get("url")):
        fail(path, "sourceDirectory.url must be an http(s) URL")
    slugs = source.get("slugs")
    if not isinstance(slugs, list) or any(
        not isinstance(item, str) or not item.strip() for item in slugs
    ):
        fail(path, "sourceDirectory.slugs must be a list of non-empty strings")

    evidence = record["vibeCodedEvidence"]
    if evidence not in ALLOWED_EVIDENCE:
        fail(path, f"vibeCodedEvidence must be one of {sorted(ALLOWED_EVIDENCE)}")
    evidence_url = record["vibeCodedEvidenceUrl"]
    if evidence_url is not None and not is_url(evidence_url):
        fail(path, "vibeCodedEvidenceUrl must be an http(s) URL or null")
    if evidence != "unverified" and evidence_url is None:
        fail(path, "documented evidence needs vibeCodedEvidenceUrl")

    try:
        dt.date.fromisoformat(require_string(record, "lastVerified", path))
    except ValueError as exc:
        fail(path, f"lastVerified must be an ISO date: {exc}")

    if not description.strip().endswith((".", "!", "?")):
        fail(path, "description should be a complete sentence")

    return slug


def main() -> int:
    paths = sorted(APPS_DIR.glob("*.json"))
    if not paths:
        print("No catalog entries found.", file=sys.stderr)
        return 1

    slugs: set[str] = set()
    try:
        for path in paths:
            try:
                record = json.loads(path.read_text())
            except json.JSONDecodeError as exc:
                fail(path, f"invalid JSON: {exc}")
            slug = validate_record(path, record)
            if slug in slugs:
                fail(path, f"duplicate slug: {slug}")
            slugs.add(slug)
    except ValueError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} catalog entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
