# Auto Fix Engine (prototype)

The page `auto-fix-engine.html` sends user-provided context, test logs, and optional source to Gemini for diagnosis and a unified-diff patch proposal.

## Workflow
1. Run CI/browser tests independently.
2. Paste failure logs and relevant source/context into the page.
3. Review root cause, patch, risks, and retest instructions.
4. Apply changes manually or through a separately authorized code-review workflow.
5. Run tests again; do not accept fixes based only on the model's claim.

## Limits and safety
- This page does not fetch CI logs, read repository contents, execute generated code, apply patches, commit, or trigger workflows.
- The key is held in page memory, but browser-based API requests can be inspected. Avoid shared computers and consider provider quota/privacy implications.
- Never paste secrets, personal data, or credentials into prompts.
- Suggested patch is untrusted; review and test it in an isolated environment.
