# AGENTS.md vs. CLAUDE.md vs. .cursor/rules: The Complete 2026 Agent Context Guide & Templates

> ⭐ **Looking for the complete 2026 AI Coding Taxonomy?** [**Return to the Main Repository & Star on GitHub**](https://github.com/mahmoudsajjadi/awesome-ai-coding-tools)

---

## Executive Summary

As developers migrate between **Claude Code**, **Cursor**, **Windsurf**, and **Aider**, maintaining redundant prompt instructions across different proprietary dotfiles creates maintenance overhead. The developer community in 2026 has converged on **`AGENTS.md`** as the open, universal project memory standard, supported by scoped rule files for tool-specific workflows.

---

## 1. Specification Comparison

| Specification | Primary Scope | Supported Agents | How It Is Processed |
| :--- | :--- | :--- | :--- |
| **`AGENTS.md`** | **Universal Open Standard** | Claude Code (v2.1.277+), Cursor, Codex CLI, Aider, Windsurf, Zed, OpenCode, Jules | Ingested at session initiation as root system instructions. Universal cross-tool format. |
| **`CLAUDE.md`** | Tool-Specific (Anthropic) | Claude Code CLI, Claude Desktop | Used for sub-agent tool execution permissions and compact build commands. |
| **`.cursor/rules/*.mdc`** | Scoped Directory (Cursor) | Cursor IDE | Triggered dynamically via glob patterns (`*.ts`, `*.py`) only when relevant files are edited. |
| **`SKILL.md`** | Task-Triggered Plugin | Antigravity, OpenCode | Procedural instructions loaded on-demand when specific user intents or slash commands fire. |

---

## 2. The 2026 Token-Saving Rule

Empirical research on context window efficiency reveals that **pasting complete directory trees or entire file dumps into root instruction files degrades agent accuracy by over 18%** and wastes 1,000–4,000 prompt tokens per turn.

Modern agents already utilize Tree-sitter parsers to build AST dependency maps. Your context files should strictly contain:
1. **Non-Inferable Build & Test Commands:** Commands the agent cannot guess by reading source files.
2. **Negative Constraints:** Explicit rules stating what the agent must **never** do.
3. **Typing & Commit Standards:** Project-wide style conventions.

---

## 3. Production-Ready `AGENTS.md` Template

Copy and paste this into an `AGENTS.md` file in the root of your project:

```markdown
# AGENTS.md — Universal Agent Context Specification

## 1. Project Overview & Architecture
- Stack: TypeScript / Node.js (or Python 3.12 / FastAPI)
- Structure: Modular services under `src/` (or `app/`), test suites under `tests/`.

## 2. Essential Commands (Non-Inferable)
- Build: `npm run build` (or `cargo build --release` / `poetry run build`)
- Fast Test Loop: `npm test -- --bail` (or `pytest -v --tb=short`)
- Lint & Format: `npm run lint` (or `ruff check .`)

## 3. Negative Constraints (What NOT to Do)
- NEVER commit secrets, API keys, or `.env` files.
- NEVER delete or overwrite existing docstrings, copyright headers, or test suites unless explicitly requested.
- DO NOT use wildcard imports (`from module import *`).
- DO NOT introduce heavy external dependencies for utilities solvable with standard libraries.

## 4. Code Style & Typing Standards
- All code must pass strict type checking without warnings (`mypy --strict` or TypeScript `strict: true`).
- Keep functions modular and under 50 lines. Keep files under 300 lines.
- Commits must adhere to Conventional Commits: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`.
```

---

> ⭐ **Looking for the complete 2026 AI Coding Taxonomy?** [**Return to the Main Repository & Star on GitHub**](https://github.com/mahmoudsajjadi/awesome-ai-coding-tools)
