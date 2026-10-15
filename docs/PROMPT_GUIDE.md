# Developer Prompting Guide for AI Pair Programming

Systematic prompting templates designed to maximize code accuracy, prevent regressions, and enforce clean architecture.

---

## 1. Feature Implementation Template

```text
Task: Implement a thread-safe caching layer for our user profile service.
Context:
- Language: Python 3.11 with FastAPI and Redis backend.
- Existing file: services/cache.py (see attached signatures).
Constraints:
- Implement TTL expiration (default 300s).
- Use asyncio with async/await syntax.
- Catch connection exceptions and fallback to DB query without crashing.
- Write 3 pytest unit tests covering happy path and connection timeout.
```

---

## 2. Refactoring & Code Smell Elimination

```text
Task: Refactor this 250-line function into modular, single-responsibility units.
Goals:
- Extract database queries into a repository layer.
- Retain existing function public signatures for backward compatibility.
- Replace nested if-else statements with guard clauses.
- Do NOT introduce external dependencies.
```

---

## 3. Bug Hunting from Traceback

```text
Task: Fix the race condition identified by the test runner below.
Traceback:
[Paste exact terminal error stack trace here]
Requirements:
- Explain root cause in 2 bullet points.
- Provide minimal diff patch using Search & Replace block format.
- Ensure all 14 related tests pass without side-effects.
```
