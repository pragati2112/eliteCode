
def removeDuplicates(nums):
	start = 1
	end = 1

	while end < len(nums):
		if nums[start-1] != nums[end]:
			nums[start] = nums[end] 
			start+=1
		end+=1	

	return start	





nums = [2, 3, 3, 3, 6, 9, 9]

print(removeDuplicates(nums))