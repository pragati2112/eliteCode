from heapq import *


def max_heapify(nums, i):
	largest = i
	left_c = (2*i)
	right_c = (2*i)+1

	if nums[left_c]<nums[largest] and left_c<len(nums):
		largest = left_c

	if nums[right_c]<nums[largest] and right_c<len(nums):
		largest = right_c	

	if largest != i:
		nums[largest], nums[i] = nums[i], nums[largest]
		# heapify(nums, largest)



def k_largets_nums(nums, k):
	start_idx = (len(nums)//2)-1

	for i in range(start_idx, -1, -1):
		max_heapify(nums, i)

	# i = len(nums)-k
	print(nums[k-1])	



def point_closest_to_the_origin(points, k):
	minheap = []
    res = []
    for i in range(len(points)):
        heappush(minheap, (distance_from_origin(points[i]), points[i]))
    
    for x in range(k):
        a,b = heappop(minheap)
        res.append(b)
    
    return res


def distance_from_origin(point):
	# point will be like - [x, y]
	# we have to figure out Eucleadian distance
	return math.sqrt(point[0]*point[0]+point[1]*point[1])




print(k_largets_nums([5, 12, 11, -1, 12], 3))	