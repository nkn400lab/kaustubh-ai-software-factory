# AI Auto Repair Integration Hub

Open `ai-auto-repair-integration.html` to connect CI failure logs with a reviewed repair proposal.

## Workflow
1. Paste a CI log and the complete current source file; remove secrets and personal data first.
2. Enter a Gemini API key and request diagnosis. The page asks Gemini for a complete replacement file plus root-cause, risk and test notes.
3. Review and edit the entire replacement. Download it or the JSON review report if preferred.
4. Optionally provide a fine-grained GitHub token with Contents read/write access limited to the target repository. After checking the explicit approval box, the page fetches the current file SHA and commits that one reviewed file.
5. Inspect the commit and manually dispatch the Remote Test Runner workflow. Review the artifact and logs.

## Safety and limitations
- This is a browser-side helper, not an autonomous coding agent. It does not fetch CI artifacts, execute code, run tests, open pull requests, merge changes, or dispatch workflows.
- Gemini receives the pasted log and source. Remove credentials, tokens, customer data and other secrets before submitting.
- AI-generated patches can be wrong or insecure. Review the complete diff/source and test independently.
- GitHub token is held in page memory only; it is not written to local storage. Use a fine-grained repository-scoped token and revoke it after use.
- The GitHub API operation updates one file only. If the target file does not exist, publishing stops rather than creating it.
