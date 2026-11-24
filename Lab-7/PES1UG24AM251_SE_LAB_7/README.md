# Lab 7 - Pet Walking Service Fuzz Testing

## Overview

This lab uses Hypothesis to fuzz the pet walking service input functions and harden them against malformed input. `processor.py` now validates schedule structure, numeric metrics, and temperament codes; invalid values return `None` rather than raising exceptions.

## Setup

From this folder, install the lab dependencies:

```bash
python -m pip install pytest hypothesis
```

## Run

Run the application with sample input:

```bash
python processor.py
```

Run the Hypothesis tests:

```bash
python -m pytest -v --tb=short test_processor.py
```

## Results

The starter run exposed crashes from empty and malformed schedule data, `None`, malformed pace values, and unknown temperament codes. It also failed to recognize the documented `PLAYFUL` code. After the defensive validation fixes, all **21 tests passed**, including the three fuzz properties, valid behavior checks, and invalid-input cases.

## Submission files

- `processor.py` - hardened Lab 7 application
- `test_processor.py` - Hypothesis fuzz tests and focused regression tests
- `PES1UG24AM251_SE_LAB_7_Report.pdf` - report with before/after terminal evidence
- `evidence_*.png` - output evidence images
- `baseline_processor_output.txt`, `fuzz_failures.txt`, `fixed_processor_output.txt`, `fuzz_passes.txt` - captured command output
