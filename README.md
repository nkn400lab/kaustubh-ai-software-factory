# KAUSTUBH AI SOFTWARE FACTORY

Starter dashboard and task manager. Open `index.html` in a browser to use it.

Roadmap: AI planning (API credentials needed), code generation, debug/test workflow, GitHub automation, Windows build pipeline, mobile remote interface.

Never commit API keys. Generated code/commands must be reviewed before execution.

## AI planning workbench
Open [`ai-workbench.html`](./ai-workbench.html) in a browser (or download it and open locally). Add your own Gemini API key in the page to request a project plan. Key is page-memory only; this prototype does not save it or run generated code. API access and quotas may apply.


## AI Code Studio

Open [`code-studio.html`](./code-studio.html) to generate downloadable project files using Gemini or analyze/debug pasted code. It displays generated files and allows individual downloads or a text bundle. It does not execute generated code. API key is entered in the page and held only in page memory; direct browser API calls may expose it to browser/network inspection and should be used cautiously.


## Test & Repair Lab

Open [`test-repair-lab.html`](./test-repair-lab.html) for AI test-plan creation, code/error diagnosis, and basic heuristic static checks. It does not execute code or certify security/correctness. Use generated recommendations as review aids.


## Windows Build Kit

[`windows-build-kit.html`](./windows-build-kit.html) creates packaging blueprints, commented build-script suggestions, and checklists for Windows/portable/installer/Electron/Python/Web/Android projects. It does not run scripts or verify actual builds; inspect outputs before executing locally.


## GitHub File Sync

Open [`github-file-sync.html`](./github-file-sync.html) to upload a JSON manifest of files to a repository using a user-provided fine-grained GitHub token (repository Contents read/write). The token is not saved by the page. Uploads are sequential, separate commits, and existing paths are updated. Use a repository-scoped token, inspect the file list before upload, and revoke the token when done. This is a browser-based helper, not a persistent secret vault.


## Autonomous Software Agent

[`autonomous-agent.html`](./autonomous-agent.html) provides a single flow to submit a software specification, ask Gemini for a JSON file manifest of source files, validate file paths and manifest shape, review/download the output, and publish reviewed files to GitHub after an explicit confirmation. Publishing uses a user-provided repository-scoped token and commits files sequentially. Generated code is not executed and tests/builds are not performed by this page.


## Windows Runner / CI Smoke Test

GitHub Actions workflow [`windows-factory-smoke.yml`](./.github/workflows/windows-factory-smoke.yml) runs a static smoke check on a hosted Windows runner after pushes to `main` or on manual dispatch. See [`WINDOWS-RUNNER.md`](./WINDOWS-RUNNER.md). It checks basic HTML/title structure only; it is not browser testing or a Windows build.


## Automatic Windows Source Package Builder

[`package-builder.html`](./package-builder.html) links to the Windows packaging workflow. The workflow [`windows-package.yml`](./.github/workflows/windows-package.yml) creates a ZIP source snapshot as a downloadable GitHub Actions artifact. It is not an EXE compiler. Instructions: [`PACKAGE-BUILDER.md`](./PACKAGE-BUILDER.md).


## Browser Testing & Repair Advisor

Run [`browser-test-agent.html`](./browser-test-agent.html) to submit logs or snippets for Gemini diagnosis and a reviewed patch suggestion (it does not apply changes or execute code). Playwright smoke tests are in [`tests/browser-smoke.spec.js`](./tests/browser-smoke.spec.js), run by [`browser-test.yml`](./.github/workflows/browser-test.yml) on relevant pushes or manual dispatch. Details: [`BROWSER-TESTING.md`](./BROWSER-TESTING.md).


## Auto Fix Engine

Open [`auto-fix-engine.html`](./auto-fix-engine.html) to send pasted test logs and optional code/context to Gemini for a diagnosis and unified-diff patch proposal. Review and apply patches manually, then rerun CI. The prototype does not fetch logs, apply changes, execute code, or trigger builds. Guide: [`AUTO-FIX-ENGINE.md`](./AUTO-FIX-ENGINE.md).


## Factory Control Center

Launch [`factory-control-center.html`](./factory-control-center.html) to access the module shortcuts and a browser-local project checklist. Notes/checklist are stored in the browser and are not synced. Guide: [`CONTROL-CENTER.md`](./CONTROL-CENTER.md).


## One-Click Project Creator

Launch [`one-click-project-creator.html`](./one-click-project-creator.html) to turn a brief into a reviewed source-file manifest, test-plan file, downloads, or sequential GitHub publishing. See [`ONE-CLICK-CREATOR.md`](./ONE-CLICK-CREATOR.md). It requires a Gemini API key and optional repository-scoped GitHub token; files are not executed or tested automatically.


## Factory Pipeline Orchestrator

[`factory-pipeline-orchestrator.html`](./factory-pipeline-orchestrator.html) imports manifests, applies basic quality checks, generates CI workflow templates and release notes, and exports or sequentially publishes reviewed files. Guide: [`PIPELINE-ORCHESTRATOR.md`](./PIPELINE-ORCHESTRATOR.md). Checks are heuristic only; workflow templates may need adaptation.
