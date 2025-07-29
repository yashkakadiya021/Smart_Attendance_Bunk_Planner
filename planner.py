# planner.py

def calculate_current_attendance(attended_classes, total_classes):
    if total_classes == 0:
        return 0
    return round((attended_classes / total_classes) * 100, 2)


def calculate_bunkable_classes(attended, conducted, upcoming, min_required_percent):
    max_bunks = 0
    for bunks in range(upcoming + 1):
        future_attended = attended + (upcoming - bunks)
        future_total = conducted + upcoming
        projected_attendance = (future_attended / future_total) * 100

        if projected_attendance >= min_required_percent:
            max_bunks = bunks
        else:
            break

    return max_bunks


def project_attendance_if_all_attended(attended, conducted, upcoming):
    total_classes = conducted + upcoming
    total_attended = attended + upcoming
    return round((total_attended / total_classes) * 100, 2)
