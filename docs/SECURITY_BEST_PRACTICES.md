# Security Best Practices for AI Coding Tools

Essential security protocols to prevent accidental credential leakage, prompt injection vulnerabilities, and malicious dependency execution.

### 1. Protect API Keys and Secrets
- Always include `.env`, `credentials.json`, `*.pem`, and `id_rsa` in your project `.gitignore`.
- Set up pre-commit hooks using tools like `detect-secrets` or `trufflehog` to block commits containing sensitive strings.
- Never paste production connection strings or bearer tokens into code assistant chat prompts.

### 2. Sandbox Terminal Execution
- When using autonomous tools that execute bash commands (like Aider, OpenHands, or Cline), run them inside a containerized Docker environment or virtual machine.
- Avoid passing `-y` / `--yes` (auto-confirm execution) on unvetted repositories to prevent unintended `rm -rf` or network commands.

### 3. Review Generated Dependencies (Hallucinated Packages)
- Periodically check newly generated imports against public registries (PyPI, npm, crates.io).
- Attackers occasionally squat package names frequently hallucinated by language models. Always verify that third-party libraries are legitimate and actively maintained.
