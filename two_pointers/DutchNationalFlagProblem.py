def DutchFlagProb(nums):
    start = 0
    end = len(nums) - 1
    i = 0

    while i < len(nums):
        if nums[i] == 0:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
        elif nums[i] == 1:
            i += 1
        else:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1


nums = [1, 0, 2, 1, 0]

print(DutchFlagProb(nums))
