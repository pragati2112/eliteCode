import math

def tripletSum(nums, target):
	min_output = math.inf
	nums.sort()

	for i in range(len(nums)):
		right = len(nums)-1
		left = i+1
		while left<right:
			target_diff = target - nums[left] - nums[right] - nums[i]

			if target_diff == 0:
				return target_diff - target

			if abs(target_diff) < abs(min_output) or (abs(target_diff) == abs(min_output)):
				min_output = target_diff

			if target_diff > 0:
				left+=1
			else:
				right=-1

	return target - min_output


nums = [1, 0, 1, 1]	
target = 100
print(tripletSum(nums, target))