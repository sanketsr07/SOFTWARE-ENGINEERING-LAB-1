# Reflection on Static Code Analysis

## 1. What is static analysis, and how is it different from running tests?

Static analysis inspects source code without executing the program. Pylint checks code quality and likely mistakes, Flake8 checks Python style, and Bandit looks for common security risks. Tests execute selected scenarios and show whether those specific behaviors work. The tools and tests found different kinds of problems in this pharmacy tracker.

## 2. Which findings mattered most, and why?

The SQL string interpolation was the most important security finding because patient input could affect a database query. The pharmacy-specific review also exposed a stock correctness issue: negative quantities were accepted, so a negative dispense could increase inventory. Case-sensitive medicine lookup caused a valid medicine name to fail when its capitalization differed. These issues could affect data integrity or prescription handling, so they deserved priority over formatting warnings.

## 3. How did Pylint, Bandit, and Flake8 complement each other?

Pylint identified maintainability and correctness risks such as the shared mutable default, missing documentation, and broad exception handlers. Bandit highlighted the interpolated SQL and unsafe exception pattern. Flake8 identified unused imports, spacing, line length, and naming issues. Using all three gave a broader review than any one tool alone.

## 4. What did you learn, and how will you use static analysis?

Static analysis is most useful as a repeated feedback loop: scan, rank findings by impact, fix them, and scan again. A clean tool report is not proof that the application behaves correctly, so I also added focused checks for case-insensitive stock lookup, allergy matching, and positive quantities. I will use the tools during development and keep behavior tests for important pharmacy rules.

## Coverage evidence

The starter version had **25% line coverage** over `pharmacy_system.py` under the three targeted checks; two checks failed. After the fix, the same checks passed and line coverage was **39%**. The coverage figures describe only these focused checks, not full application coverage; expiry handling, file persistence, and the interactive `main()` path are outside this small suite. See `coverage_before.txt` and `coverage_after.txt` for the captured output.
