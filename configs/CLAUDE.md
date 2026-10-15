# Repository Guidelines & Quality Standards for Claude Code

## Architecture Principles
1. Maintain clean separation between business logic, data models, and external APIs.
2. Favor explicit, strongly-typed interfaces over dynamic object passing.
3. Keep external dependencies minimal and vetted.

## Git & Development Workflow
- **Commit Style:** Use Conventional Commits format: `<type>(<scope>): <concise description>`.
- **Atomic Commits:** Make single-concern, bisectable commits. Never mix refactors with feature changes.
- **Verification First:** Before opening a PR or submitting a fix, execute the test suite:
  ```bash
  # Python
  pytest -v --tb=short
  # JavaScript/TypeScript
  npm test -- --bail
  ```

## Anti-Hallucination & Verification Checklist
- Always verify file paths exist before importing or deleting.
- When generating diffs, preserve all existing docstrings, copyright headers, and formatting comments.
- Do not invent non-existent flags or CLI options.
