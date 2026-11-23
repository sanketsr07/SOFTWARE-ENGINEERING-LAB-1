"""Line-coverage tests for the pet walking service."""

import pytest

from pet_walking_service import inspect_gps_collars, process_walking_routes


def _route(
    session_type="standard_30",
    walks=None,
    weekend=False,
    confirmed=True,
):
    """Build one route with explicit test inputs."""
    return {
        "route_confirmed": confirmed,
        "session_type": session_type,
        "is_weekend": weekend,
        "walks": [] if walks is None else walks,
    }


def _walk(pets=1, aggression=False, medication=False):
    """Build one scheduled walk."""
    return {
        "num_pets": pets,
        "aggression_alert": aggression,
        "needs_meds": medication,
    }


def test_rejects_invalid_routes_and_transport_fees():
    with pytest.raises(ValueError, match="Invalid routes"):
        process_walking_routes(None, 5.0)

    with pytest.raises(ValueError, match="Invalid routes"):
        process_walking_routes([], -0.01)


def test_empty_and_unconfirmed_routes_return_zero_earnings():
    assert process_walking_routes([], 5.0) == {
        "total_revenue": 0.0,
        "status": "ZERO_EARNINGS",
    }
    assert process_walking_routes(
        [_route(confirmed=False, walks=[_walk()])], 5.0
    )["status"] == "ZERO_EARNINGS"


@pytest.mark.parametrize(
    ("session", "expected"),
    [("standard_60", 40.0), ("standard_30", 27.0), ("express_15", 19.0)],
)
def test_each_session_type_uses_its_base_fee(session, expected):
    result = process_walking_routes(
        [_route(session, [_walk(pets=1)])], 5.0
    )

    assert result == {"total_revenue": expected, "status": "COMPLETED"}


def test_default_session_and_empty_walk_list_are_supported():
    route = {"route_confirmed": True, "is_weekend": False}

    assert process_walking_routes([route], 5.0)["status"] == "ZERO_EARNINGS"


def test_unknown_session_is_counted_as_an_incident():
    result = process_walking_routes([_route("overnight")], 5.0)

    assert result == {"total_revenue": 0.0, "status": "ZERO_EARNINGS"}


def test_aggression_invalid_pet_count_and_medication_paths():
    routes = [
        _route("standard_60", [_walk(aggression=True)]),
        _route("standard_30", [_walk(aggression=True, medication=True)]),
        _route("express_15", [_walk(pets=0, medication=True)]),
    ]

    assert process_walking_routes(routes, 5.0) == {
        "total_revenue": 6.0,
        "status": "COMPLETED",
    }


def test_large_pet_group_discount_meds_and_weekend_fee():
    result = process_walking_routes(
        [_route("express_15", [_walk(pets=4, medication=True)], weekend=True)],
        5.0,
    )

    assert result == {"total_revenue": 52.4, "status": "COMPLETED"}


def test_incident_audit_and_threshold_boundary():
    valid_route = _route("standard_30", [_walk()])
    four_incidents = [_route("unknown") for _ in range(4)] + [valid_route]
    five_incidents = [_route("unknown") for _ in range(5)] + [valid_route]

    assert process_walking_routes(four_incidents, 5.0)["status"] == "COMPLETED"
    assert process_walking_routes(five_incidents, 5.0)["status"] == "INCIDENT_AUDIT"


def test_gps_collars_report_empty_online_and_lost_signal_states():
    assert inspect_gps_collars([]) == "NO_DATA"
    assert inspect_gps_collars([[20, 45, 19, 30], [25]]) == "ONLINE"
    assert inspect_gps_collars([[19, 18], [50]]) == "LOST_SIGNAL_ALERT"
