from typing import List	


def insertionSort(nums: List[int]) -> List:
	for i in range(0, len(nums)-1):
		key = nums[i+1] 
		j = i 

		while j >= 0 and key < nums[j]:
			# traverse previous elements till this loop breaks--
			nums[j + 1] = nums[j] 
			j-=1 

		# insert key here--
		nums[j + 1] = key

	return nums


if __name__ == '__main__':

  nums = [20,5,4,1,60,45,65,32,45]

  print(insertionSort(nums))