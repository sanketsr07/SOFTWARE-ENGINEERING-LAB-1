from hypothesis import given, strategies as st
import pytest
from processor import parse_walk_schedule, compute_pace_per_pet, lookup_temperament_surcharge

@given(st.text() | st.none())
def test_parse_walk_schedule_no_crash(s):
    try:
        parse_walk_schedule(s)
    except Exception as exc:
        pytest.fail(f"parse_walk_schedule crashed for {s!r}: {exc}")

@given(st.text() | st.none())
def test_compute_pace_per_pet_safe(s):
    try:
        compute_pace_per_pet(s)
    except Exception as exc:
        pytest.fail(f"compute_pace_per_pet crashed for {s!r}: {exc}")

@given(st.text() | st.none())
def test_lookup_temperament_surcharge_safe(s):
    try:
        lookup_temperament_surcharge(s)
    except Exception as exc:
        pytest.fail(f"lookup_temperament_surcharge crashed for {s!r}: {exc}")


def test_valid_schedule_keeps_expected_fee():
    assert parse_walk_schedule("2-30-YES") == "Walk: 2 pets, 30 mins - Total $45.00"


def test_valid_pace_is_rounded_to_two_decimals():
    assert compute_pace_per_pet("10/3") == 3.33


def test_valid_temperament_codes_keep_expected_surcharges():
    assert lookup_temperament_surcharge("CALM") == 0.0
    assert lookup_temperament_surcharge("PLAYFUL") == 5.0
    assert lookup_temperament_surcharge("PLY") == 5.0
    assert lookup_temperament_surcharge("REACTIVE") == 12.0
    assert lookup_temperament_surcharge("AGGRESSIVE") == 20.0


@pytest.mark.parametrize("value", [None, "", "2-30-MAYBE", "2-0-NO", "1-30-YES-extra"])
def test_invalid_schedules_return_none(value):
    assert parse_walk_schedule(value) is None


@pytest.mark.parametrize("value", [None, "", "30/0", "nan/1", "10/inf", "-1/2", "1/2/3"])
def test_invalid_metrics_return_none(value):
    assert compute_pace_per_pet(value) is None


@pytest.mark.parametrize("value", [None, "", "UNKNOWN"])
def test_unknown_temperaments_return_none(value):
    assert lookup_temperament_surcharge(value) is None
