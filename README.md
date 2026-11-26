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
