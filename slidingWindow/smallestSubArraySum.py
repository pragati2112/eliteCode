import math


def smallestSubArraySum(s, arr):
    _sum = 0.0
    start = 0
    min_len = math.inf
    for i in range(len(arr)):
        _sum += arr[i]
        while _sum >= s:
            min_len = min(min_len, i - start + 1)
            _sum -= arr[start]
            start += 1
    if min_len == math.inf:
        return 0
    return min_len


arr = [2, 1, 5, 2, 3, 2]
s = 7
print(smallestSubArraySum(s, arr))
