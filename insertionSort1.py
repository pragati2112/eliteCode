from typing import List

def swap(a, b):
	c = b
	b = a
	a = c
	return a, b

def sort_insertion(nums: List):

	for item in range(1, len(nums)):
		j = item
		while j > 0 and nums[j]<nums[j-1]:
			nums[j], nums[j-1] = swap(nums[j], nums[j-1])
			j = j-1

	return nums


input = [9, 5, 1, 4, 3]
print(input)
print(sort_insertion(input))