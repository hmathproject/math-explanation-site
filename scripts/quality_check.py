#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
SITEMAP_PATH = ROOT / "sitemap.xml"

FRONT_MATTER_REQUIRED = ("layout", "title", "permalink", "description")
FORBIDDEN_TERMS = ("公開中", "準備中", "解説PDF準備中")
RAW_UNICODE_MATH = ("≤", "≥", "√", "∈")
WARN_PATTERNS = (
    (re.compile(r"\\lvert|\\rvert|\\\|"), r"inline absolute value can break markdown tables; prefer display math"),
    (re.compile(r"\\dfrac"), r"\\dfrac in inline math can disturb line height; prefer \\frac"),
    (re.compile(r"\$[^$\n]+\$"), r"dollar-delimited inline math found; repo standard is \\( ... \\)"),
)
LINK_RE = re.compile(r"\[[^\]]*]\((/[^)\s#]+/?)(?:#[^)]+)?\)|href=\"(/[^\"\s#]+/?)(?:#[^\"]+)?\"")
IMAGE_RE = re.compile(r"/assets/images/[^)\s\"']+")
PDF_RE = re.compile(r"/assets/pdf/[^)\s\"']+")
PDF_BTN_RE = re.compile(r'<a[^>]*class="[^"]*\bpdf-btn\b[^"]*"[^>]*href="([^"]+)"')
SINGLE_BACKSLASH_INLINE_RE = re.compile(r"(?<!\\)\\\((?!\\)")
SINGLE_BACKSLASH_CLOSE_RE = re.compile(r"(?<!\\)\\\)(?!\\)")
PERMALINK_RE = re.compile(r"^/$|^/[A-Za-z0-9/_-]*/$")


@dataclass
class Finding:
    level: str
    path: Path
    message: str
    line: int | None = None

    def render(self) -> str:
        location = self.path.relative_to(ROOT).as_posix()
        if self.line is not None:
            location = f"{location}:{self.line}"
        return f"{self.level}: {location}: {self.message}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def line_number(text: str, needle: str) -> int | None:
    idx = text.find(needle)
    if idx == -1:
        return None
    return text.count("\n", 0, idx) + 1


def line_number_from_index(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


def front_matter_and_body(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    raw = parts[0][4:]
    body = parts[1]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def public_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.glob("*.md")
        if path.name != "README.md"
    )


def docs_markdown_files() -> list[Path]:
    return sorted(DOCS_DIR.glob("*.md"))


def build_permalink_map(paths: list[Path]) -> tuple[dict[str, Path], list[Finding]]:
    mapping: dict[str, Path] = {}
    findings: list[Finding] = []
    for path in paths:
        text = read_text(path)
        front_matter, _ = front_matter_and_body(text)
        permalink = front_matter.get("permalink", "")
        if permalink:
            if permalink in mapping:
                findings.append(Finding("ERROR", path, f"duplicate permalink {permalink}", line_number(text, f"permalink: {permalink}")))
            mapping[permalink] = path
    return mapping, findings


def check_front_matter(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    front_matter, _ = front_matter_and_body(text)
    if not front_matter:
        findings.append(Finding("ERROR", path, "missing front matter", 1))
        return findings

    for key in FRONT_MATTER_REQUIRED:
        if not front_matter.get(key):
            findings.append(Finding("ERROR", path, f"missing front matter field: {key}", 1))

    permalink = front_matter.get("permalink")
    if permalink and not PERMALINK_RE.fullmatch(permalink):
        findings.append(Finding("ERROR", path, f"invalid permalink format: {permalink}", line_number(text, f"permalink: {permalink}")))

    return findings


def check_forbidden_terms(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for term in FORBIDDEN_TERMS:
        if term in text:
            findings.append(Finding("ERROR", path, f"forbidden term found: {term}", line_number(text, term)))
    return findings


def check_assets_and_links(path: Path, text: str, permalink_map: dict[str, Path]) -> list[Finding]:
    findings: list[Finding] = []

    for target in sorted(set(IMAGE_RE.findall(text))):
        if not (ROOT / target.lstrip("/")).exists():
            findings.append(Finding("ERROR", path, f"missing image asset: {target}", line_number(text, target)))

    pdf_targets = set(PDF_RE.findall(text))
    for target in sorted(pdf_targets):
        if not (ROOT / target.lstrip("/")).exists():
            findings.append(Finding("ERROR", path, f"missing PDF asset: {target}", line_number(text, target)))

    for match in PDF_BTN_RE.finditer(text):
        href = match.group(1)
        if href.startswith("/assets/pdf/") and not (ROOT / href.lstrip("/")).exists():
            findings.append(Finding("ERROR", path, f"pdf-btn target does not exist: {href}", line_number(text, href)))

    for match in LINK_RE.finditer(text):
        target = match.group(1) or match.group(2)
        if target.startswith("/assets/"):
            continue
        if target not in permalink_map:
            findings.append(Finding("ERROR", path, f"missing linked public page: {target}", line_number(text, target)))

    return findings


def check_math_notation(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []

    for char in RAW_UNICODE_MATH:
        if char in text:
            findings.append(Finding("ERROR", path, f"raw Unicode math symbol found: {char}", line_number(text, char)))

    opener = SINGLE_BACKSLASH_INLINE_RE.search(text)
    if opener:
        findings.append(
            Finding(
                "ERROR",
                path,
                r"single backslash inline math opener found: \( ... use \\(",
                line_number_from_index(text, opener.start()),
            )
        )

    closer = SINGLE_BACKSLASH_CLOSE_RE.search(text)
    if closer:
        findings.append(
            Finding(
                "ERROR",
                path,
                r"single backslash inline math closer found: \) ... use \\)",
                line_number_from_index(text, closer.start()),
            )
        )

    for pattern, message in WARN_PATTERNS:
        match = pattern.search(text)
        if match:
            findings.append(Finding("WARN", path, message, line_number(text, match.group(0))))

    return findings


def check_sitemap(permalink_map: dict[str, Path]) -> list[Finding]:
    findings: list[Finding] = []
    if not SITEMAP_PATH.exists():
        return [Finding("ERROR", SITEMAP_PATH, "sitemap.xml not found", 1)]

    raw_text = read_text(SITEMAP_PATH)
    _, xml_body = front_matter_and_body(raw_text)
    root = ET.fromstring(xml_body.lstrip())
    urls = [elem.text.strip() for elem in root.iter() if elem.tag.endswith("loc") and elem.text]
    if not urls:
        return [Finding("ERROR", SITEMAP_PATH, "no <loc> entries found", 1)]

    base_prefix = None
    actual_paths: set[str] = set()
    for url in urls:
        if "://" not in url:
            findings.append(Finding("ERROR", SITEMAP_PATH, f"invalid sitemap URL: {url}", line_number(raw_text, url)))
            continue
        _, remainder = url.split("://", 1)
        slash = remainder.find("/")
        path = "/" if slash == -1 else remainder[slash:]
        if base_prefix is None:
            base_prefix = url[:-len(path)] if path != "/" else url[:-1]
        actual_paths.add(path)

    expected_paths = set(permalink_map)
    missing = sorted(expected_paths - actual_paths)
    extra = sorted(actual_paths - expected_paths)

    if len(actual_paths) != len(expected_paths):
        findings.append(
            Finding(
                "ERROR",
                SITEMAP_PATH,
                f"sitemap page count mismatch: sitemap={len(actual_paths)} public_pages={len(expected_paths)}",
                1,
            )
        )

    for path in missing:
        findings.append(Finding("ERROR", SITEMAP_PATH, f"missing sitemap entry for {path}", line_number(raw_text, "</urlset>")))
    for path in extra:
        findings.append(Finding("ERROR", SITEMAP_PATH, f"sitemap has extra entry {path}", line_number(raw_text, path)))

    return findings


def main() -> int:
    findings: list[Finding] = []
    public_files = public_markdown_files()
    _ = docs_markdown_files()

    permalink_map, permalink_findings = build_permalink_map(public_files)
    findings.extend(permalink_findings)

    for path in public_files:
        text = read_text(path)
        findings.extend(check_front_matter(path, text))
        findings.extend(check_forbidden_terms(path, text))
        findings.extend(check_assets_and_links(path, text, permalink_map))
        findings.extend(check_math_notation(path, text))

    findings.extend(check_sitemap(permalink_map))

    findings.sort(key=lambda item: (item.level != "ERROR", str(item.path), item.line or 0, item.message))
    for finding in findings:
        print(finding.render())

    error_count = sum(1 for finding in findings if finding.level == "ERROR")
    warn_count = sum(1 for finding in findings if finding.level == "WARN")
    print(f"Summary: {error_count} error(s), {warn_count} warning(s)")
    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
