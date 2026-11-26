# AI Development Engine

Use this browser tool to import a source manifest or local text files, describe maintenance changes, request an AI change plan or proposals, review/edit proposed file contents, export a manifest or individual files, and optionally publish selected changes to GitHub.

Constraints and security:
- Text files only, up to 30 source files and 250 KB per local file; input context is capped.
- AI output is a proposal; review manually.
- It does not execute source, run tests, build, deploy, apply patch automatically, or certify security.
- Publishing uses a user-provided repository-scoped token, sequential commits. Token is not saved by app but may be exposed in browser/network inspection.
- Path checks are basic and not a security audit.
