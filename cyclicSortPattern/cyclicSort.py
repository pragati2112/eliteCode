def cyclicSort(nums):
	i = 0
	while i<len(nums):
		j = nums[i]-1
		if nums[i]< len(nums) and nums[i] != nums[j]:
			print(nums[i], nums[j])
			nums[i], nums[j] = nums[j], nums[i]
		else:
			i+=1

	print(nums)
	for i in range(len(nums)):
		if nums[i] !=i:
			return i

	return len(nums)		


def main():
	print(cyclicSort([4,0,3,1]))
main()		