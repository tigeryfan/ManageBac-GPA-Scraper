def calc_gpa(scores):
    def convert_to_gpa(score):
        score = float(str(score).replace("%", ""))
        if score >= 97:
            return 4.0
        elif score >= 93:
            return 4.0
        elif score >= 90:
            return 3.7
        elif score >= 87:
            return 3.3
        elif score >= 83:
            return 3.0
        elif score >= 80:
            return 2.7
        elif score >= 77:
            return 2.3
        elif score >= 73:
            return 2.0
        elif score >= 70:
            return 1.7
        elif score >= 67:
            return 1.3
        elif score >= 65:
            return 1.0
        else:
            return 0.0

    total_points = sum(convert_to_gpa(score) for score in scores)
    gpa = total_points / len(scores)
    return f"{gpa:.2f}"

if __name__ == "__main__":
    print(calc_gpa([93.4, 85.6, 77.8, 91.1, 88.5, 82.9, 85.5, 81.1, 77.7, 95.5]))
