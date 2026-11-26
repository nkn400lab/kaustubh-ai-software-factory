# Integrated Factory CI

The `Factory Integrated CI` workflow is the main verification pipeline.

## What runs

1. **Static validation** compiles the Python validator and checks every root-level HTML page for an HTML element, populated title, duplicate IDs, and missing relative local assets/links.
2. **Browser smoke tests** launches every root-level HTML page with Playwright Chromium, checks HTTP success and non-empty body, and fails on uncaught page errors.
3. **Source package** runs only after both test jobs succeed and uploads a ZIP of the exact tested commit.

## Triggers

- Pushes to `main`
- Pull requests targeting `main`
- Manual run from GitHub Actions

## Run and inspect

Open the repository's Actions tab and select **Factory Integrated CI**. A source ZIP is available under the successful run's Artifacts section. A failed browser run may include a Playwright failure report.

## Important limits

This pipeline verifies static structure and basic browser loading only. It does not prove business logic, security, API integrations, database correctness, installer/EXE compilation, or production readiness. The uploaded ZIP is source code, not a Windows executable. Review code and run application-specific tests before release.
