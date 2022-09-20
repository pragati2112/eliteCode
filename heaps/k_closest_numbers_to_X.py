from heapq import *


def find_K_closest_to_x(nums, k, X):
    hash_map = {}
    minheap = []
    result = []
    for num in nums:
        hash_map[num] = abs(num - X)

    for num, val in hash_map.items():
        heappush(minheap, (val, num))

    for i in range(k):
        val, num = heappop(minheap)
        result.append(num)

    result.sort()
    return result


def find_max_distinct_elems(nums, k):
    minheap = []
    hash_map = {}
    for num in nums:
        if num in hash_map.keys():
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    distinct_elem_counts = 0
    for num, freq in hash_map.items():
        heappush(minheap, (freq, num))

    while k > 0 and minheap:
        freq, num = heappop(minheap)
        k -= freq - 1
        if k >= 0:
            distinct_elem_counts += 1

    return distinct_elem_counts


def sum_of_elems(nums, k1, k2):
    minheap = []
    for num in nums:
        heappush(minheap, num)

    for _ in range(k1):
        heappop(minheap)

    ans = 0
    for _ in range(k2 - k1 - 1):
        ans += heappop(minheap)

    return ans


def rearrange_string(str):
    maxheap = []
    hash_map = {}
    for s in str:
        if s in hash_map.keys():
            hash_map[s] += 1
        else:
            hash_map[s] = 1

    result = ''
    for s, freq in hash_map.items():
        heappush(maxheap, (-freq, s))

    prev_char, prev_freq = '', 0
    while maxheap:
        freq, char = heappop(maxheap)
        if prev_char != '' and -prev_freq > 0:
            heappush(maxheap, (prev_freq, prev_char))
        result += char
        prev_char = char
        prev_freq = freq + 1
    return result


print(rearrange_string("Programming"))
