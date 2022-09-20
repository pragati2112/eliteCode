import math


def order_agnostic_binary_search(nums, k):
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = (high + low) // 2

        if k < nums[mid]:
            high = mid - 1

        if k > nums[mid]:
            low = mid + 1

        if k == nums[mid]:
            return mid
    return -1


def find_ceiling_of_number(nums, k):
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if k <= nums[mid]:
            return mid

        if k > nums[mid]:
            low = mid + 1

        if k < nums[mid]:
            high = mid - 1

    return -1


def find_next_letter(arr, char):
    for i in range(len(arr)):
        if ord(char) < ord(arr[i]):
            return arr[i]

    return arr[0]


def search_index(arr, k, findMaxIndex):
    # this is also correct----

    # start,end = -1, -1

    # for i in range(len(arr)):
    # 	if arr[i]==k and start ==-1:
    # 		start = i

    # 	if arr[i]>k:
    # 		end = i-1
    # 		return [start, end]

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            key_index = mid

        if k > arr[mid]:
            low = mid + 1

        if k < mid:
            high = mid - 1

        if findMaxIndex:
            low = mid + 1
        else:
            high = mid - 1

    return key_index


def number_range(nums, k):
    result = [-1, -1]
    result[0] = search_index(nums, k, False)
    if result[0] != -1:
        result[1] = search_index(nums, k, True)

    return result


def search_in_infinite_array(nums, k):
    bound_size = 2
    start, end = 0, bound_size
    bounded_arr = nums[start:end]

    while k > nums[end]:
        start = bound_size
        bound_size = bound_size * 2
        end = bound_size - 1
        bounded_arr = nums[start:end]

    return order_agnostic_binary_search(bounded_arr, k)


def min_difference(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2

        if k == nums[mid]:
            return nums[mid]

        if k < nums[mid]:
            high = mid - 1

        if k > nums[mid]:
            low = mid + 1

        # at the end exit of while loop , low == high+1

    if (nums[low] - k) < (nums[high] - k):
        return nums[low]
    else return nums[high]


def find_max_in_bitonic_array(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2

        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return nums[low]


print(min_difference([4, 6, 10], 4))
