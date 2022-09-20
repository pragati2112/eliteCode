def quadreplesSum(nums, target):
    # w+x+y+z = target
    # OR
    # w+x+y = target-z

    nums.sort()
    quadreples = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            search_pair(nums, target, i, j, quadreples)
    return quadreples


def search_pair(nums, target, first, second, quadreples):
    left = second + 1
    right = len(nums) - 1
    while left <= right:
        current_sum = nums[left] + nums[right] + nums[first] + nums[second]

        if current_sum == target:
            quadreples.append([nums[left], nums[right], nums[first], nums[second]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif current_sum < target:
            left += 1  # sum needs to be bigger
        else:
            right -= 1  # sum needs to be smaller


nums = [2, 0, -1, 1, -2, 2]
target = 2
print(quadreplesSum(nums, target))
