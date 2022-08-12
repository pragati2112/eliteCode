from heapq import *


class Node():
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __lt__(self, other):
		return self.value < other.value


def merge_lists(lists):
	resulthead, resulttail = None, None

	minheap = []

	for root in lists:
		if root is not None:
			heappush(minheap, root)


	while minheap:
		node = heappop(minheap)
		if resulthead is None:
			resulthead = resulttail = node
		else:
			resulttail.next = node	
			resulttail = resulttail.next

		if node.next is not None:
			heappush(minheap, node.next)
			# or we can keep count here---- how many
			# elems we have inserted already--if it is equal to K retun that elem. 

	# it will return merged lists
	return resulthead


def kth_smallest_number_in_sorted_lists(resulthead, k):
	result = []
	while resulthead is not None:
		result.append(resulthead.value)
		resulthead = resulthead.next
	return result[k-1]




def main():
	l1 = Node(2)
	l1.next = Node(6)
	l1.next.next = Node(8)

	l2 = Node(3)
	l2.next = Node(6)
	l2.next.next = Node(7)

	l3 = Node(1)
	l3.next = Node(3)
	l3.next.next = Node(4)

	result = merge_lists([l1,l2,l3])
	# while result is not None:
	# 	print(result.value)
	# 	result = result.next

	
	print('****',kth_smallest_number_in_sorted_lists(result, 5))


main()			
