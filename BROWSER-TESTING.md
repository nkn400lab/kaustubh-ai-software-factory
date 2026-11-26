# Browser testing and repair advisor

- **Factory Browser Tests**: GitHub Actions workflow uses Playwright and Chromium to visit factory HTML pages and report page-level errors.
- Trigger manually from Actions or automatically when relevant HTML/test files are pushed.
- **Browser Test & Repair Advisor**: `browser-test-agent.html` accepts pasted logs/snippets and asks Gemini for a diagnosis and suggested patch.
- Advisor does not execute code or apply patches. API key is used in-memory for the request and not persisted by this page.
- CI tests are smoke tests, not proof of functional correctness or security.