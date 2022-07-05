import math

def tripletSum(nums, target):
	nums.sort()
	triplets = []
	count = 0

	for i in range(len(nums)):
		right = len(nums)-1
		left = i+1
		while left < right:
			if nums[i] + nums[left] + nums[right] < target:
				print([nums[i], nums[left] , nums[right]], 'true')
				count+=right-left
				left+=1
			else:
				print([nums[i], nums[left] , nums[right]], 'false')
				right-=1

	return count


nums = [-1, 0, 2, 3]
target=3
print(tripletSum(nums, target))