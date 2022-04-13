from typing import List


def merge(a, l, m, r)-> List:

	# first create left and right list of size n1 and n2 initialise with 0
	# calculate n1 and n2 by using m,l,r positions
	# and insert elements of 'a' in L and R lists

	# and then do the merging-- by comparing L[i] and R[j] elements 

	n1 = m - l + 1
	n2 = r - m
	L = [0] * n1
	R = [0] * n2

	for i in range(0, n1):
		L[i] = a[l + i]
	for i in range(0, n2):
		R[i] = a[m + i + 1]

	i, j, k = 0, 0, l

	while i< n1 and j<n2:
		if L[i] <= R[j]	:
			a[k] = L[i]
			i+=1
		else:
			a[k] = R[j]
			j+=1

		k+=1	

	# Remaining elements
	while i<n1:
		a[k] = L[i]
		k+=1
		i+=1

	while j<n2:
		a[k] = R[j]
		k+=1
		j+=1		



def iterativeMergeSort(nums: List[int]) -> List:

	# find l, m, r positions of elements to sort
	# increase width of list in each pass by 2


	width = 1
	n = len(nums)
	while width < n:
		l=0;
		while (l < n):
			m = min(l+(width-1), n-1)
			r = min(l+(2*width-1), n-1)
			merge(nums, l, m, r)

			# shift l after merging 2 lists
			l+= width*2

		width *= 2
	return nums	




if __name__ == '__main__':

  nums = [20,3,4,1,22,45, 0]

  print(iterativeMergeSort(nums))