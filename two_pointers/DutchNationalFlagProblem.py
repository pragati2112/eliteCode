def DutchFlagProb(nums):

	start = 0
	end = len(nums)-1
	i=0

	while i < len(nums):
		print(start)
		if nums[start] > nums[end]:
			nums[start], nums[end] = nums[end], nums[start] 
			start+=1
		else:
			end-=1	

	return nums






nums = [1, 0, 2, 1, 0]

print(DutchFlagProb(nums))