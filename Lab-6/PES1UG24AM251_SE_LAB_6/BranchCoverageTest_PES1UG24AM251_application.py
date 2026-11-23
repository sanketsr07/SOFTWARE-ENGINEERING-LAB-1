"""Branch-coverage tests for the pet walking service."""

import pytest

from pet_walking_service import inspect_gps_collars, process_walking_routes


def _route(
    session_type="standard_30",
    walks=None,
    weekend=False,
    confirmed=True,
):
    """Build a route record for a test case."""
    return {
        "route_confirmed": confirmed,
        "session_type": session_type,
        "is_weekend": weekend,
        "walks": [] if walks is None else walks,
    }


def _walk(pets=1, aggression=False, medication=False):
    """Build a walk record for a test case."""
    return {
        "num_pets": pets,
        "aggression_alert": aggression,
        "needs_meds": medication,
    }


def test_input_validation_true_and_false_paths():
    with pytest.raises(ValueError):
        process_walking_routes("not a list", 5.0)
    with pytest.raises(ValueError):
        process_walking_routes([], -1.0)

    assert process_walking_routes([], 0.0)["status"] == "ZERO_EARNINGS"


def test_route_confirmation_and_empty_iteration_paths():
    routes = [
        _route(confirmed=False, walks=[_walk()]),
        {"route_confirmed": True, "walks": []},
    ]

    assert process_walking_routes(routes, 5.0) == {
        "total_revenue": 0.0,
        "status": "ZERO_EARNINGS",
    }


def test_all_session_selection_branches_and_unknown_session():
    routes = [
        _route("standard_60", [_walk()]),
        _route("standard_30", [_walk()]),
        _route("express_15", [_walk()]),
        _route("unknown", [_walk()]),
    ]

    result = process_walking_routes(routes, 5.0)

    # 40 + 27 + 19 = 86; unknown session adds one incident and no revenue.
    assert result == {"total_revenue": 86.0, "status": "COMPLETED"}


def test_walk_validation_aggression_and_aggression_session_branch():
    routes = [
        _route("standard_60", [_walk(aggression=True)]),
        _route("standard_30", [_walk(aggression=True)]),
        _route("standard_30", [_walk(pets=0)]),
        _route("standard_30", [_walk(pets=1, aggression=False)]),
    ]

    result = process_walking_routes(routes, 5.0)

    assert result == {"total_revenue": 27.0, "status": "COMPLETED"}


def test_pet_count_discount_medication_and_weekend_branches():
    routes = [
        _route("standard_30", [_walk(pets=3, medication=False)]),
        _route("express_15", [_walk(pets=4, medication=True)], weekend=True),
        _route("express_15", [_walk(pets=1, medication=False)], weekend=False),
    ]

    result = process_walking_routes(routes, 5.0)

    # 37 + (14 + 32) * .90 + 6 + 5 + 19 = 108.4
    assert result == {"total_revenue": 108.4, "status": "COMPLETED"}


def test_incident_audit_branch_and_four_incident_boundary():
    valid = _route("standard_30", [_walk()])
    four = [_route("invalid") for _ in range(4)] + [valid]
    five = [_route("invalid") for _ in range(5)] + [valid]

    assert process_walking_routes(four, 5.0)["status"] == "COMPLETED"
    assert process_walking_routes(five, 5.0)["status"] == "INCIDENT_AUDIT"


def test_zero_revenue_and_positive_revenue_status_branches():
    assert process_walking_routes([_route(confirmed=False)], 5.0)["status"] == "ZERO_EARNINGS"
    assert process_walking_routes([_route("standard_30", [_walk()])], 5.0)["status"] == "COMPLETED"


def test_gps_empty_online_streak_reset_and_loss_branches():
    assert inspect_gps_collars([]) == "NO_DATA"
    assert inspect_gps_collars([[]]) == "ONLINE"
    assert inspect_gps_collars([[19]]) == "ONLINE"
    assert inspect_gps_collars([[19, 20, 19, 18]]) == "LOST_SIGNAL_ALERT"
