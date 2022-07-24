class Node():
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def mid_linked_list(head):
	fast,slow = head, head
	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next 

	return slow


def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(4)
	head.next.next.next = Node(6)
	head.next.next.next.next = Node(7)
	head.next.next.next.next.next = Node(8)
	head.next.next.next.next.next.next = head.next.next
	print(mid_linked_list(head))

main()	