from heapq import *

def min_heapify(nums, i):
	minimum = i
	left_c = (2*i)
	right_c = (2*i)+1

	print(left_c, right_c)

	if nums[left_c]<nums[minimum] and left_c<len(nums):
		minimum = left_c

	if nums[right_c]<nums[minimum] and right_c<len(nums):
		minimum = right_c	

	if minimum != i:
		nums[minimum], nums[i] = nums[i], nums[minimum]
		# heapify(nums, largest)


def k_largets_nums(nums, k):
	start_idx = (len(nums)//2)-1
	for i in range(start_idx, -1, -1):
		min_heapify(nums, i)

	i = len(nums)-k
	print(nums[i:])	



def min_cost_to_connect_ropes(nums):
	minheap = []
	for i in range(len(nums)):
		heappush(minheap, nums[i])

	temp, result = 0,0
	for i in range(minheap):
		temp = heappop(minheap)+heappop(minheap)
		result+=temp
		heappush(minheap, temp)		
	return result



def top_k_frequent_numbers(nums, k):
	hash_map = {}
	minheap = []
	for num in nums:
		if num in hash_map.keys():
			hash_map[num] +=1
		else: hash_map[num] = 1	

	for num, val in hash_map.items():
		heappush(minheap, (val,num))
		if len(minheap)>k:
			heappop(minheap)

	top_numbers = []
	for i in range(k):
		top_numbers.append(minheap[i][1])

	return top_numbers


def sort_decreasing_order(str):
	hash_map = {}
	for s in str:
		if s in hash_map.keys():
			hash_map[s] +=1
		else: hash_map[s] = 1

	maxheap = []
	for s, val in hash_map.items():
		heappush(maxheap, (-val, s))


	new_s = ''
	while maxheap:
		freq, char = heappop(maxheap)
		for _ in range(-freq):
			new_s+=char
	print(new_s)




class kthLargestNumberInStream:
	minheap=[]

	def __init__(self, nums, k):
		self.nums = nums
		self.k = k
		for i in self.nums:
			self.add(i)

	def add(self, num):
		heappush(self.minheap, num)
		
		if len(self.minheap) > self.k:
			heappop(self.minheap)

		return self.minheap[0]	
		


find = kthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)

print(find.add(6))	