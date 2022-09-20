def squaringAnArray(nums):
    end = len(nums) - 1
    result = [0 for x in range(len(nums))]
    start = 0
    highestSquareIdx = len(nums) - 1

    while start <= end:

        left_sq = nums[start] * nums[start]
        right_sq = nums[end] * nums[end]

        if left_sq > right_sq:
            result[highestSquareIdx] = left_sq
            start += 1
        else:
            result[highestSquareIdx] = right_sq
            end -= 1
        highestSquareIdx -= 1
    return result


nums = [-3, -1, 0, 1, 2]

print(squaringAnArray(nums))
