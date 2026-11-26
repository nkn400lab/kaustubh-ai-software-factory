"""Static validation for every root-level factory HTML page."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.has_html = False
        self.has_title = False
        self.title_text = False
        self.in_title = False
        self.ids = set()
        self.duplicates = set()
        self.local_links = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attrs = dict(attrs)
        if tag == "html":
            self.has_html = True
        if tag == "title":
            self.has_title = True
            self.in_title = True
        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicates.add(element_id)
            self.ids.add(element_id)
        for attr in ("href", "src"):
            value = attrs.get(attr, "")
            if not value or value.startswith(("#", "data:", "javascript:", "mailto:", "tel:")):
                continue
            parsed = urlparse(value)
            if parsed.scheme or parsed.netloc:
                continue
            path = value.split("#", 1)[0].split("?", 1)[0]
            if path:
                self.local_links.append(path)

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title and data.strip():
            self.title_text = True


def main():
    pages = sorted(ROOT.glob("*.html"))
    failures = []
    if not pages:
        print("FAIL: no root-level HTML pages found")
        return 1

    for path in pages:
        name = path.name
        parser = PageParser()
        try:
            parser.feed(path.read_text(encoding="utf-8"))
            parser.close()
        except Exception as exc:
            failures.append(f"PARSE ERROR: {name}: {exc}")
            continue

        if not parser.has_html:
            failures.append(f"MISSING <html>: {name}")
        if not parser.has_title or not parser.title_text:
            failures.append(f"MISSING populated <title>: {name}")
        for duplicate in sorted(parser.duplicates):
            failures.append(f"DUPLICATE id={duplicate!r}: {name}")
        for link in parser.local_links:
            target = (path.parent / link).resolve()
            if not target.exists():
                failures.append(f"BROKEN LOCAL LINK: {name} -> {link}")
        if not any(item.endswith(f": {name}") or item.startswith(f"DUPLICATE id=") and item.endswith(f": {name}") or item.startswith(f"BROKEN LOCAL LINK: {name} ->") for item in failures):
            print(f"PASS: {name}")

    if failures:
        print("\n".join(failures))
        return 1
    print(f"Validated {len(pages)} HTML pages: structure, title, duplicate IDs and local assets/links.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
