"""Lightweight smoke validation of factory HTML files; does not execute page scripts."""
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    "index.html", "ai-workbench.html", "code-studio.html",
    "test-repair-lab.html", "windows-build-kit.html",
    "github-file-sync.html", "autonomous-agent.html"
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html = False
        self.title = False
        self.title_text = False
        self.in_title = False
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "html": self.html = True
        if tag.lower() == "title": self.title = True; self.in_title = True
    def handle_endtag(self, tag):
        if tag.lower() == "title": self.in_title = False
    def handle_data(self, data):
        if self.in_title and data.strip(): self.title_text = True

def main():
    failures = []
    for name in PAGES:
        path = ROOT / name
        if not path.is_file():
            failures.append(f"MISSING: {name}")
            continue
        parser = PageParser()
        try:
            parser.feed(path.read_text(encoding="utf-8"))
            parser.close()
        except Exception as exc:
            failures.append(f"PARSE ERROR: {name}: {exc}")
            continue
        if not parser.html: failures.append(f"No <html> tag: {name}")
        if not parser.title or not parser.title_text: failures.append(f"Missing populated <title>: {name}")
        if name not in failures: print(f"PASS: {name}")
    if failures:
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"Validated {len(PAGES)} HTML pages (static parsing only).")

if __name__ == "__main__":
    main()
