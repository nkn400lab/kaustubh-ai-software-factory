# CI Failure Analyzer

Open `ci-failure-analyzer.html` and paste the test output or upload `test-output.log` from the Project Remote Test Runner artifact.

Features:
- Local keyword-based classification for common Node/Python/CI errors.
- Optional Gemini diagnosis with root-cause hypothesis, log evidence, minimal fix proposal and verification steps.
- Downloadable plain-text analysis report.

Limitations and safety:
- The local scan is heuristic and may miss or misclassify failures.
- Optional AI sends the pasted log (up to the last 18,000 characters) to Google's Gemini API. Do not send secrets, tokens, personal data, or private logs without authorization.
- API key is held only in page memory and is not saved, but browser/network inspection may expose direct API requests.
- This tool does not fetch GitHub logs, change repository files, apply patches, or run tests. Review any proposed fix and rerun CI yourself.
