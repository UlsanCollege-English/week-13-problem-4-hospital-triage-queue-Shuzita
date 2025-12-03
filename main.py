def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Patients have:
      - "name": string
      - "severity": int (1 = most urgent)
      - "arrival_order": int (smaller = earlier)

    Sorting priority:
      1. severity ascending
      2. arrival_order ascending
    """

    # If no patients or k == 0
    if k <= 0 or not patients:
        return []

    # Sort by priority rules:
    # First severity (lower is more urgent)
    # Then arrival_order (smaller means earlier)
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Select the first k patients and return only their names
    return [p["name"] for p in sorted_patients[:k]]


if __name__ == "__main__":
    # Optional manual test
    sample_patients = [
        {"name": "Alex", "severity": 3, "arrival_order": 5},
        {"name": "Bella", "severity": 1, "arrival_order": 6},
        {"name": "Chris", "severity": 1, "arrival_order": 2},
    ]
    print(select_patients(sample_patients, 2)) 
    # Expected: ["Chris", "Bella"]
