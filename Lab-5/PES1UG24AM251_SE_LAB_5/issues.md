# Static analysis findings and fixes

The line references below point to the starter version scanned before changes.
Findings are ordered by severity, with security and stock correctness first.

| Issue | Type / severity | Line(s) | Description | Fix approach |
|---|---|---:|---|---|
| SQL built with patient input | Security / Medium (Bandit B608) | 21 | A patient name was interpolated into SQL, allowing malformed input to alter the query. | Use a parameterized query with `?` placeholders. |
| Negative quantities accepted | Bug / High (manual review) | 35, 72 | Negative stock was seeded, and dispensing a negative count increased stock. | Reject non-positive quantities; use a positive demo stock count. |
| Medicine names compared case-sensitively | Bug / Medium (manual review) | 32, 35, 75 | `ibuprofen` did not match the `Ibuprofen` stock key and could bypass the intended lookup behavior. | Compare normalized names for both allergy and stock lookup; update the canonical stock key. |
| Mutable list default | Bug / Medium (Pylint W0102) | 24 | The default batch log was shared between calls. | Default to `None` and create a list inside the function. |
| Broad exception handling | Reliability / Medium (Pylint W0702, Flake8 E722; Bandit B110 in stock loading) | 38, 58 | Bare handlers hid unrelated failures and made invalid behavior hard to diagnose. | Catch only the expected exception classes and handle them explicitly. |
| Files opened without context managers or encoding | Reliability / Low (Pylint W1514/R1732) | 50, 57 | Handles could remain open, and text encoding depended on the machine. | Use `with open(..., encoding="utf-8")`. |
| Style and maintainability violations | Style / Low (Pylint, Flake8) | 3, 11-80 | Unused import, missing docstrings, long lines, spacing, and non-snake-case naming made the file harder to maintain. | Remove unused imports, document functions, use snake_case, and format to Flake8 rules. |

## Verification

- Pylint: 6.90/10 before; 10.00/10 after.
- Bandit: two findings before; zero findings after.
- Flake8: style violations before; no output after.
- Three pharmacy behavior checks: two failures before the logic fix; all three pass after it.
