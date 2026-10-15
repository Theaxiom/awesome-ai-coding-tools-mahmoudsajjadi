# Public Benchmarks for Code Generation & Editing

An empirical reference guide to standardized benchmarks used by researchers to evaluate language models on software engineering tasks.

### 1. SWE-bench & SWE-bench Verified
- **Scope:** 2,294 real-world GitHub issues extracted from 12 popular open-source Python repositories (e.g. Django, SymPy, scikit-learn).
- **Evaluation:** Evaluates end-to-end repository modification. Patches are evaluated against hidden test suites using `FAIL_TO_PASS` and `PASS_TO_PASS` validation.
- **Metric:** $pass@1$ percentage of resolved issues.

### 2. HumanEval & HumanEval+
- **Scope:** 164 handwritten programming problems evaluating docstring comprehension and unit-test verification.
- **HumanEval+:** Augments original unit tests with 80x more rigorous mutation test cases (EvalPlus) to expose false-positive model passes.

### 3. MBPP (Mostly Basic Python Problems) & MBPP+
- **Scope:** 974 crowd-sourced Python programming challenges targeting basic algorithms, string parsing, and numeric operations.

### 4. CrossCodeEval
- **Scope:** Cross-file completion benchmark testing repository-level dependency comprehension across Python, Java, C#, and TypeScript.
