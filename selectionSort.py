from typing import List	


def selectionSort(nums: List[int]) -> List:

	# select min element firts elem of nums
	for i in range(len(nums)):
		min_idx = i

		for j in range(i+1, len(nums)):
			# and then iterate over nums to compare minimum element from i+1 to len(nums)

			if nums[min_idx] > nums[j]:
				min_idx = j # found min_idx at j

		nums[i], nums[min_idx] = nums[min_idx], nums[i]	 # swapping

	return nums

	


if __name__ == '__main__':

  nums = [20,5,4,1,60,45,65,32,45]

  print(selectionSort(nums))