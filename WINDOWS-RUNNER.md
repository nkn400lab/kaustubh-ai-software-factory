# Windows Runner / CI Phase

## What this phase adds
- A GitHub Actions workflow runs on a GitHub-hosted Windows machine when changes are pushed to `main`, or when manually dispatched.
- A lightweight Python static smoke check confirms the factory's expected HTML files exist and have basic HTML/title structure.
- The validator does **not** execute JavaScript, AI-generated code, installers, or applications.

## Run it
1. Open the repository on GitHub.
2. Select **Actions**.
3. Select **Windows Factory Smoke Test**.
4. For a manual run, click **Run workflow** and confirm the branch.

## Security
This uses a temporary GitHub-hosted runner, not your personal Windows PC. It does not require personal access tokens or secrets. Do not add workflows that execute unreviewed AI-generated programs on machines containing credentials or private client data.

## Limitations
This is a structural smoke test, not a browser test, product acceptance test, or Windows executable build. A green workflow means only that the static checks passed.
