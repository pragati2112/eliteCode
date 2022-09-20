def ProductLessThanTarget(nums, target):
    product = 1
    left = 0
    result = []
    for right in range(len(nums)):
        product *= nums[right]
        while product >= target and left < len(nums):
            product /= nums[left]
            left += 1

        array = []
        for i in range(right, left - 1, -1):
            array.append(nums[i])
            print(array)
            result.append(list(array))
    return result


nums = [2, 5, 3, 10]
target = 30
print(ProductLessThanTarget(nums, target))
