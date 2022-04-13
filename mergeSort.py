from typing import List



def merge(left: List, right: List)-> List:
	if not len(left) or not len(right):
		return left or right

	i, j = 0, 0

	result = []

	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

		if i==len(left) or j==len(right):
			result.extend(left[i:] or right[j:])	
			break

	return result		


def mergeSort(nums: List[int]) -> List:

	if len(nums)<2:
		return nums

	middle = int(len(nums)/2)
	
	left = mergeSort(nums[:middle])
	right = mergeSort(nums[middle:])

	return merge(left, right)


if __name__ == '__main__':

  nums = [20,3,4,1,22,45]

  print(mergeSort(nums))