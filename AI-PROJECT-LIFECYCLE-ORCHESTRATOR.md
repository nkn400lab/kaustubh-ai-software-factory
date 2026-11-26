# AI Project Lifecycle Orchestrator

Open `ai-project-lifecycle-orchestrator.html` to generate a starter project manifest from a written brief, review source files, run basic local manifest checks, export a JSON bundle/test plan, and optionally publish files sequentially to GitHub.

## Workflow
1. Enter a Gemini API key, project name and detailed specification.
2. Generate up to 12 files (150,000 total source characters maximum).
3. Review and edit every generated file. Run the basic path/empty-file/credential-marker/TODO checks.
4. Export the manifest and test plan, or provide a fine-grained GitHub token with Contents read/write permission and explicitly approve publishing.
5. Inspect the individual GitHub commits and manually run the Remote Test Runner. Review the CI artifact before considering a release.

## Important limitations
- Gemini receives the written brief. Never send secrets, credentials, personal/customer data or confidential source.
- The quality checks are simple browser-side heuristics. They are not a compiler, test runner, security scanner or proof of correctness.
- Publishing uses sequential GitHub Contents API calls. A failure may leave some earlier files committed; the page reports the number completed. Review commit history before retrying.
- The token is held in page memory only and is not written to local storage. Use a repository-scoped fine-grained token and revoke it after use.
- The page does not execute generated code, run CI, create releases, merge branches or deploy software.
