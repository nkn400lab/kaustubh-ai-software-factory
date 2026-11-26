# Factory Pipeline Orchestrator

Open `factory-pipeline-orchestrator.html` in a browser.

Features:
- Import a JSON file manifest
- Basic path, duplicate, secret-pattern, and destructive-command checks
- Edit and select files
- Generate basic GitHub Actions CI workflow templates for static HTML, Node, or Python
- Generate release notes
- Export manifest or individual files
- Sequential GitHub publishing using user token

Limitations:
- Static heuristics are not a security audit.
- Generated workflows are templates and may require adjustment for project dependencies.
- Does not execute, build, deploy, or validate generated project code.
- Token is only page-memory, but browser/network inspection can expose it. Use narrowly scoped tokens.
