# Automatic Software Package Builder

This workflow creates a downloadable ZIP snapshot of the repository on a hosted Windows runner.

## Start
1. Go to the repository's **Actions** tab.
2. Choose **Windows Software Package**.
3. Use **Run workflow**. Optionally enter a package name.
4. After the workflow finishes, open its run page and download the **source-package** artifact.

The workflow also runs on pushes to main and creates an artifact, subject to GitHub Actions availability/limits.

## Scope
This is a source ZIP packaging workflow, not a compiled EXE installer. It does not install dependencies, run project scripts, or execute AI-generated code. Review code before running it locally. Artifact retention is set to 7 days.
