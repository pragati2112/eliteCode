from heapq import*
import math
def kth_smallest_number_in_sorted_lists(lists, k):
	minheap = []
	result = []
	count = 0
	for i in range(len(lists)):
		heappush(minheap, (lists[i][0], 0 , lists[i]))

	while minheap:
		num, i, _list = heappop(minheap)

		if count!=k:
			result.append(num)
			count +=1
		else:
			break	

		if len(_list)>i+1:
			heappush(minheap, (_list[i+1], i+1, _list))	

	print(result[-1])




def smallest_rumber_range(lists):
	minheap = []
	rangestart, rangend = 0, math.inf
	currentmax = -math.inf
	
	for i in range(len(lists)):
		heappush(minheap, (lists[i][0], 0, lists[i]))
		currentmax=max(currentmax, _list[i+1])

	while minheap:
		num, i , _list = heappop(minheap)
		if rangend-rangestart>currentmax-num:
			rangend=currentmax
			rangestart=num	

		if len(_list)>i+1:
			heappush(minheap, (_list[i+1], i+1, _list))	
			currentmax=max(currentmax, _list[i+1])

	print([rangestart, rangend])





print(kth_smallest_number_in_sorted_lists([[2,6,8],[3,6,7],[1,3,4]], 5))

print(smallest_rumber_range([[1, 5, 8], [4, 12], [7, 8, 10]]))