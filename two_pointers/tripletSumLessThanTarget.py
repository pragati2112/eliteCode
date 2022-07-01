import math

def tripletSum(nums, target):
	nums.sort()
	triplets = []

	for i in range(len(nums)):
		right = len(nums)-1
		left = i+1
		while left < right:
			curr_sum = nums[left] + nums[right] + nums[i] 

			if curr_sum < target:
				left+=1
				triplets.append([nums[left] , nums[right] , nums[i]] )

			if curr_sum > target:
				right-=1
				

	return len(triplets)


nums = [-1, 0, 2, 3]
target=3
print(tripletSum(nums, target))