from heapq import *


def intervals(intervals):
    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])
    min_number = 0
    minHeap = []

    for meeting in intervals:
        # meeting[start]>=minHeap[0][end] that means previous meeting is over
        while len(minHeap) > 0 and meeting[start] >= minHeap[0][end]:
            heappop(minHeap)
        heappush(minHeap, meeting)

        min_number = max(min_number, len(minHeap))

    return min_number


def main():
    print(intervals([[1, 4], [2, 5], [7, 9]]))


main()
