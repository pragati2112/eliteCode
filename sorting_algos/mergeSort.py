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

	m = int(len(nums)/2)
	
	left = mergeSort(nums[:m])
	right = mergeSort(nums[m:])

	return merge(left, right)


##### OR you can use this ######


def mergeSort1(nums, l, r):
	if l>r:
		return

	m = l+r//2

	mergeSort1(nums, l, m)
	mergeSort1(nums, m+1, r)	

	return merge(nums, l, m, r)  ## look merge function in iterative merge sort ###

	# n1 = m - l + 1
	# n2 = r - m
	# L = [0] * n1
	# R = [0] * n2

	# for i in range(0, n1):
	# 	L[i] = a[l + i]
	# for i in range(0, n2):
	# 	R[i] = a[m + i + 1]

	# i, j, k = 0, 0, l



if __name__ == '__main__':

  nums = [20,3,4,1,22,45]

  print(mergeSort(nums))