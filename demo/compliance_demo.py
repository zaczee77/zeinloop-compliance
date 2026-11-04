"""Reference demo for the Zeinloop compliance workflow pattern.

Synthetic sample buildings only. No real building data. No network.
The threshold is illustrative only, not a legal limit.
"""

THRESHOLD = 0.020


def validate(building):
    missing = []
    for field in ("building_id", "square_feet", "emissions_kg"):
        if building.get(field) in (None, ""):
            missing.append(field)
    if building.get("square_feet") is not None and building["square_feet"] <= 0:
        missing.append("square_feet_positive")
    return missing


def summarize(building):
    intensity = building["emissions_kg"] / building["square_feet"]
    status = "above threshold" if intensity > THRESHOLD else "within threshold"
    return intensity, status


def main():
    buildings = [
        {"building_id": "BLDG001", "square_feet": 50000, "emissions_kg": 800},
        {"building_id": "BLDG002", "square_feet": 40000, "emissions_kg": None},
        {"building_id": "BLDG003", "square_feet": 30000, "emissions_kg": 900},
    ]
    summarized = 0
    flagged = 0
    for building in buildings:
        missing = validate(building)
        if missing:
            flagged += 1
            print(f"{building['building_id']}: flagged for review, missing {', '.join(missing)}")
            continue
        intensity, status = summarize(building)
        summarized += 1
        print(f"{building['building_id']}: {intensity:.4f} kg per square foot, {status}")
    print(f"Summary: {summarized} summarized, {flagged} flagged for review.")


if __name__ == "__main__":
    main()
