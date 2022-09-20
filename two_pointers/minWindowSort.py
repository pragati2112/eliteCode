import math


def minimumWindowSort(nums):
    low = 0
    right = len(nums) - 1

    while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
        low += 1

    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    sub_array_max = -math.inf
    sub_array_min = math.inf

    for i in range(low, right + 1):
        sub_array_min = min(sub_array_min, nums[i])
        sub_array_max = max(sub_array_max, nums[i])

    while low > 0 and nums[low - 1] > sub_array_min:
        low -= 1
    while right < len(nums) - 1 and nums[right + 1] < sub_array_max:
        right += 1

    return right - low + 1


nums = [2, 5, 3, 10]
print(minimumWindowSort(nums))
