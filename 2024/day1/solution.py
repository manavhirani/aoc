# Basic solution

# Part one
def sorted_paired_abs_diff(arr0: list, arr1: list) -> int:
    # Sort
    arr0.sort()
    arr1.sort()
    sum_diffs = 0
    for i, j in zip(arr0, arr1):
        sum_diffs += abs(i - j)
    return sum_diffs


# Part two
def similarity_scores(arr0: list, arr1: list) -> int:
    # Calculate frequency from arr1
    frequencies1 = {}
    for key in arr1:
        frequencies1[key] = 1 + frequencies1.get(key, 0)
    sim_score = 0
    for num in arr0:
        if num in frequencies1:
            sim_score += num * frequencies1[num]
    return sim_score


with open("2024/day1/input.txt") as file:
    arrays = file.readlines()
    arr0, arr1 = [], []
    for line in arrays:
        e0, e1 = line.split()
        arr0.append(int(e0))
        arr1.append(int(e1))

    print(arr0[:5], arr1[:5])

print(sorted_paired_abs_diff(arr0, arr1))
print(similarity_scores(arr0, arr1))
