# One-Click Project Creator

Open `one-click-project-creator.html` in a browser. Fill a project brief and Gemini key, generate a JSON file manifest, review/edit each file, then download the manifest or publish selected files to GitHub.

- Uses Gemini API directly from the browser; API key is page-memory only but may be exposed in network/browser inspection. Avoid shared/public computers.
- GitHub publishing uses a user-provided token. Use repository-scoped Contents permissions, never paste unrelated credentials, and revoke token after use.
- Generates up to 15 source files per request. File-path checks block absolute paths, parent traversal, backslashes, and empty path segments.
- Publishing updates or creates files sequentially. A partial publish is possible; review the status and repository.
- Generated source is not executed, tested, built, or security certified by this tool. Review before use.
