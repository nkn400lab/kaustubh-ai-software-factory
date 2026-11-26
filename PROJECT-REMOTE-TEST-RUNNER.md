# Project Remote Test Runner

Open project-test-runner.html for the workflow launcher.

## Start a run
1. Commit project files to main.
2. Open Actions → Project Remote Test Runner → Run workflow.
3. Choose static-html, node, or python.
4. Inspect job logs and download the project-test-report artifact.

## Modes
- static-html runs the repository Python HTML validator.
- node uses Node 22, runs npm ci when package-lock.json exists, requires a test script, then runs npm test.
- python uses Python 3.12, installs requirements.txt when present, then runs unittest discovery.

## Safety and limits
- Manual dispatch only; no automatic execution on every push.
- Workflow has read-only repository contents permission.
- No arbitrary command input is accepted.
- Node/Python tests execute repository code on GitHub-hosted runners. Run only code you trust.
- Static validation is not a full browser test, security audit, or production build.
- Detailed failure diagnostics remain in Actions logs.
