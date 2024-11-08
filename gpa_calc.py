def calc_gpa(scores):
    total_points = 0
    for score in scores:
        total_points += score
    gpa = total_points / len(scores)
    return gpa

if __name__ == "__main__":
    print(calc_gpa([2.34, 3.56, 2.78, 3.21, 4.00, 2.89, 3.45, 3.11, 2.67, 3.85]))