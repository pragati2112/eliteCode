def targetSum(nums, t):
    start = 0
    end = len(nums) - 1

    while start < end:

        if nums[start] + nums[end] == t:
            return [start, end]

        if nums[start] + nums[end] > t:
            end -= 1

        if nums[start] + nums[end] < t:
            start += 1


nums = [1, 2, 3, 4, 6]
t = 6

print(targetSum(nums, t))
