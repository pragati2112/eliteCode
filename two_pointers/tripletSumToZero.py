
def tripletSum(nums):

	# x+y+z = 0
	# OR
	# x+y = -z

	nums.sort()
	triplets = []

	for i in range(len(nums)):
		if i>0 and nums[i] == nums[i-1]:
			continue
		search_pair(nums, -nums[i], i+1, triplets)
	return triplets




def search_pair(nums, target_num, left, triplets):
	right = len(nums)-1
	while left<=right:
		current_sum = nums[left] + nums[right]

		if current_sum==target_num:
			triplets.append([nums[left], nums[right], -target_num])
			left+=1
			right-=1

		elif target_num > current_sum:
			left+=1	#sum needs to be bigger 
		else:
			right-=1 #sum needs to be smaller			






nums = [-5, 2, -1, -2, 3]

print(tripletSum(nums))