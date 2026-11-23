# PES1UG24AM251 SE LAB 5

**Student:** Sanketh Shivaji Rathod  
**Repository:** https://github.com/sanketsr07/SOFTWARE-ENGINEERING-LAB-1/tree/main/Lab-5/PES1UG24AM251_SE_LAB_5  
**Target file:** `pharmacy_system.py`

## Summary

The starter application had code quality, security, and formatting findings, along with pharmacy-specific stock defects. The final version uses parameterized patient lookup SQL, validates positive whole-number quantities, matches medicine and allergy names without case sensitivity, and preserves the original stock key when dispensing. It keeps the original pharmacy stock and prescription workflow.

## Static analysis results

| Tool | Before | After |
|---|---|---|
| Pylint | 6.90/10 | 10.00/10 |
| Bandit | 2 findings (1 medium, 1 low) | 0 findings |
| Flake8 | Multiple findings | 0 violations |

The exact outputs, including before and after text, are in `pylint_report.txt`, `bandit_report.txt`, and `flake8_report.txt`. Individual raw outputs are also retained as `*_report_before.txt` and `*_report_after.txt`.

## Behavior and coverage evidence

Three focused `unittest` checks cover allergy matching, medicine-name lookup, and positive stock/dispense quantities. Before the logic fixes, two checks failed and one passed. After the fixes, all three passed. Python's built-in `trace` line counter reported 25% coverage for the starter source and 39% for the submitted source under this same small suite. These percentages are limited to the targeted checks; they do not represent full application coverage. Captured output is in `coverage_before.txt` and `coverage_after.txt`.

Run the checks from the repository root:

```bash
python -m unittest -v
python coverage_runner.py
```

The coverage runner excludes Python's standard library from tracing and prints test results and line coverage for the application and test module.

## Files included

- `pharmacy_system.py` - cleaned pharmacy application.
- `test_pharmacy_system.py` - three focused behavior checks.
- `coverage_runner.py` - reproducible test and line-coverage command.
- `issues.md` - severity-ranked findings and fix approaches.
- `reflection.md` - answers to the four lab reflection topics.
- `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt` - before and after tool outputs.
- `coverage_before.txt`, `coverage_after.txt` - initial and final check / coverage evidence.

## Commit record

The repository history contains three commits for the static-analysis fixes and submission evidence. See `git log --oneline -3` for the commit titles.
