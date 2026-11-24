# PES1UG24AM251 SE LAB 7

## Pet Walking Service: Fuzz Testing

**Student:** Sanketh Shivaji Rathod  
**Student ID:** PES1UG24AM251  
**Topic:** Pet Walking Service  
**Reference:** Lab 7 Fuzz Testing Student Handout

## Objective

Use Hypothesis to generate arbitrary text and `None` for the application's schedule parser, pace calculator, and temperament surcharge lookup. Observe failures before changes, fix validation defects, and rerun the same properties.

## Findings before fixes

The initial fuzz run had **4 failures and 2 passes**. Hypothesis minimized failing inputs such as empty strings and `None`, exposing:

- Schedule parsing crashed when input was missing fields or was `None`.
- Pace parsing crashed on malformed text or `None`; a zero-pet denominator was also unsafe.
- Temperament lookup raised `KeyError` for an unknown prefix and crashed on `None`.
- The documented `PLAYFUL` code used the prefix `PLA`, while the starter map only recognized `PLY`.

## Fixes

- Validate argument type and schedule/metric field counts before parsing.
- Catch invalid numeric conversions; reject non-positive pet counts/durations and non-finite pace values.
- Return `None` for invalid or unknown input rather than raising exceptions.
- Recognize both `PLA` (documented `PLAYFUL`) and the existing `PLY` alias.
- Update the interactive application to display clear messages for invalid values.

## Results after fixes

The same Hypothesis properties and focused valid/invalid regression cases passed: **21 passed**. Valid output remains correct for the sample schedule (`2-30-YES` gives `$45.00`), pace (`45/3` gives `15.0`), and known temperament codes.

## Commands

```bash
python processor.py
python -m pytest -v --tb=short test_processor.py
```

## Evidence

The PDF `PES1UG24AM251_SE_LAB_7_Report.pdf` contains the starter output, minimized fuzz findings, fixed application output, and passing test output. The raw command outputs are included alongside the images for reproducibility.
