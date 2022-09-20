def intervals(intervals):
    start, end, load = 0, 1, 2
    intervals.sort(key=lambda x: x[start])
    current_load = 0

    for i in range(1, len(intervals)):
        greater_load = max(current_load, intervals[i][load])
        if intervals[i][start] <= intervals[i - 1][end]:
            current_load = intervals[i][load] + intervals[i - 1][load]

    return greater_load if current_load == 0 else current_load


def main():
    print(intervals([[6, 7, 10], [2, 4, 11], [8, 12, 15]]))


main()
