# PES1UG24AM251 SE LAB 6

## Pet Walking Service: Code and Branch Coverage

**Student:** Sanketh Shivaji Rathod  
**Assigned repository:** [L6_L7_13_pet_walking_service](https://github.com/SETAPESU26/L6_L7_13_pet_walking_service)  
**Application:** `pet_walking_service.py`

## Results

The starter test passed, but it exercised only a small part of the application. The initial run measured **47% line coverage** and **43% branch coverage**. I added separate tests for line coverage and branch coverage without changing the application logic.

| Run | Tests passed | Line coverage | Branch coverage |
|---|---:|---:|---:|
| Starter test, before additions | 1 | 47% | 43% |
| `CodeCoverageTest_PES1UG24AM251_application.py` | 11 | 100% | Not measured in this run |
| `BranchCoverageTest_PES1UG24AM251_application.py` | 8 | 100% | 100% |

The branch run covered all **40 branch outcomes** with no partially covered branches. The tests cover input validation, confirmed and unconfirmed routes, all session types, unknown sessions, pet counts, aggression alerts, medication surcharges, weekend fees, incident thresholds, zero earnings, and GPS signal paths.

## Commands

Run these from the `Lab 6` folder after installing `coverage` and `pytest`:

```bash
python -m coverage erase
python -m coverage run --source=pet_walking_service -m pytest -v CodeCoverageTest_PES1UG24AM251_application.py
python -m coverage report -m pet_walking_service.py

python -m coverage erase
python -m coverage run --branch --source=pet_walking_service -m pytest -v BranchCoverageTest_PES1UG24AM251_application.py
python -m coverage report -m pet_walking_service.py
```

## Evidence files

- `coverage_before_code.txt` and `coverage_before_branch.txt` record the starter results.
- `coverage_after_code.txt` and `coverage_after_branch.txt` record the completed runs.
- The two test modules are separate as required by the handout.
