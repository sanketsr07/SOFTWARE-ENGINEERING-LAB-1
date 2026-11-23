# L6_L7_13 — Pet Walking Service

Lab 6: Code and Branch Coverage

## About

A small Python module that bills pet walking appointments based on duration, pet count, behavioral flags, and medication needs, and verifies collar GPS tracker signals.

## Files

| File | Description |
|------|-------------|
| `pet_walking_service.py` | The module under test |
| `test_pet_walking.py` | Original starter test |
| `CodeCoverageTest_PES1UG24AM251_application.py` | Tests targeting line coverage |
| `BranchCoverageTest_PES1UG24AM251_application.py` | Tests targeting branch coverage |
| `report.md` | Before-and-after coverage results and analysis |
| `coverage_before_*.txt`, `coverage_after_*.txt` | Captured terminal output for both coverage runs |

## Run the Lab 6 checks

From this folder, run the line coverage suite:

```bash
python -m coverage erase
python -m coverage run --source=pet_walking_service -m pytest -v CodeCoverageTest_PES1UG24AM251_application.py
python -m coverage report -m pet_walking_service.py
```

Then run branch coverage:

```bash
python -m coverage erase
python -m coverage run --branch --source=pet_walking_service -m pytest -v BranchCoverageTest_PES1UG24AM251_application.py
python -m coverage report -m pet_walking_service.py
```

The line suite reaches 100% line coverage, and the branch suite reaches 100% line and branch coverage for the application module. The starter test reached 47% line coverage and 43% branch coverage before the additional cases.

Keep all your Lab 6 work in this `LAB6` folder. Lab 7 will be added to this repo later.

Refer to the lab handout for instructions.

## Screenshot evidence

Terminal output images: `coverage_before_code.png`, `coverage_after_code.png`, `coverage_before_branch.png`, and `coverage_after_branch.png`.
