# Part one
import numpy as np

def check_safety(levels) -> bool:
    diffs = np.diff(levels)
    result = ((0 < diffs) & (diffs <= 3)).all() | ((-3 <= diffs) & (diffs < 0)).all()
    return result

def check_partial_safety(levels) -> bool:
    for i in range(len(levels)):
        if check_safety(np.delete(levels, i)):
            return True
    return False
    

def safety_score(report: str) -> tuple:
    levels = report.split()
    levels = list(map(int, levels))
    levels = np.array(levels)
    result1 = check_safety(levels)
    result2 = check_partial_safety(levels)
    return int(result1), int(result2)
    

def count_safe_levels(reports: list[str]) -> tuple:
    counts1 = 0
    counts2 = 0
    for report in reports:
        results = safety_score(report)
        counts1 += results[0]
        counts2 += results[1]
    return (counts1, counts2)

with open("2024/day2/input.txt") as file:
    reports = file.readlines()

print(count_safe_levels(reports))