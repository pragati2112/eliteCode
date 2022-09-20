def intervals(intervals):
    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])
    free_time = []

    for i in range(1, len(intervals)):
        if intervals[i][start] > intervals[i - 1][end]:
            free_time.append([intervals[i - 1][end], intervals[i][start]])

    return free_time


def main():
    print(intervals([[6, 7], [2, 4], [8, 12]]))


main()
