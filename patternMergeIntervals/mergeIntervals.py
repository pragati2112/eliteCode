class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    mergeIntervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            mergeIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    mergeIntervals.append(Interval(start, end))
    return mergeIntervals


def main():
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        print(i.start, i.end)


main()
