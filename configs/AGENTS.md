# AGENTS.md — Universal Agent Context Specification (2026)

## 1. Project Overview & Architecture
- Stack: [Specify Languages / Core Frameworks, e.g., TypeScript / Node.js or Python 3.12 / FastAPI]
- Structure: Modular services under `src/` (or `app/`), test suites under `tests/`.

## 2. Essential Commands (Non-Inferable)
```bash
# Build
npm run build        # or: cargo build --release / poetry run build

# Fast Test Loop (Always run before submitting changes)
npm test -- --bail   # or: pytest -v --tb=short

# Lint & Format
npm run lint         # or: ruff check .
```

## 3. Negative Constraints (What NOT to Do)
- NEVER commit secrets, API keys, or `.env` files.
- NEVER delete or overwrite existing docstrings, copyright headers, or test suites unless explicitly requested.
- DO NOT use wildcard imports (`from module import *`).
- DO NOT introduce heavy external libraries for tasks solvable with standard library utilities.

## 4. Code Style & Typing Standards
- All code must pass strict type checking without warnings (`mypy --strict` or TypeScript `strict: true`).
- Keep functions modular and under 50 lines. Keep files under 300 lines.
- Commits must adhere to Conventional Commits: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`.
