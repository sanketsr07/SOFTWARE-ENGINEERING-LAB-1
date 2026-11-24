import math


def parse_walk_schedule(schedule_spec):
    """Parse ``pets-minutes-weekend`` input, returning None when it is invalid."""
    if not isinstance(schedule_spec, str):
        return None

    parts = schedule_spec.strip().split("-")
    if len(parts) != 3:
        return None

    pets_str, mins_str, weekend_str = parts
    try:
        pets = int(pets_str.strip())
        mins = int(mins_str.strip())
    except (TypeError, ValueError):
        return None

    weekend = weekend_str.strip().upper()
    if pets <= 0 or mins <= 0 or weekend not in {"YES", "NO"}:
        return None

    weekend_fee = 15.0 if weekend == "YES" else 0.0
    base_fee = 20.0 if mins <= 30 else 35.0
    total = base_fee + (pets * 5.0) + weekend_fee
    return f"Walk: {pets} pets, {mins} mins - Total ${total:.2f}"

def compute_pace_per_pet(walk_metrics_str):
    """Return minutes per pet, or None for malformed or unsafe metrics."""
    if not isinstance(walk_metrics_str, str):
        return None

    parts = walk_metrics_str.split("/")
    if len(parts) != 2:
        return None

    try:
        mins = float(parts[0].strip())
        pets = float(parts[1].strip())
    except (TypeError, ValueError, OverflowError):
        return None

    if not math.isfinite(mins) or not math.isfinite(pets) or mins < 0 or pets <= 0:
        return None

    pace = mins / pets
    if not math.isfinite(pace):
        return None
    return round(pace, 2)

def lookup_temperament_surcharge(temperament_code):
    """Look up a known temperament surcharge, returning None for unknown input."""
    if not isinstance(temperament_code, str):
        return None

    prefix = temperament_code.strip().upper()[:3]
    surcharges = {
        "CAL": 0.0,
        "PLA": 5.0,
        "PLY": 5.0,
        "REA": 12.0,
        "AGG": 20.0,
    }
    return surcharges.get(prefix)

def main():
    print("==== Running parse_walk_schedule ====")
    s_input = input("Enter schedule (e.g. 2-30-YES): ")
    schedule_result = parse_walk_schedule(s_input)
    print(schedule_result if schedule_result is not None else "Invalid schedule input.")

    print("\n==== Running compute_pace_per_pet ====")
    p_input = input("Enter minutes/pets (e.g. 45/3): ")
    pace_result = compute_pace_per_pet(p_input)
    if pace_result is None:
        print("Invalid walk metrics.")
    else:
        print("Pace (min/pet):", pace_result)

    print("\n==== Running lookup_temperament_surcharge ====")
    t_input = input("Enter temperament code (e.g. CALM, PLAYFUL, AGGRESSIVE): ")
    surcharge = lookup_temperament_surcharge(t_input)
    if surcharge is None:
        print("Unknown temperament code.")
    else:
        print("Surcharge: $", surcharge)

if __name__ == "__main__":
    main()
