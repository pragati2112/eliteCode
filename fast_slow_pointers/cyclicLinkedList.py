class Node():
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def has_cycle(head):
	fast,slow = head, head
	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next 

		if slow == fast:
			return True
	return False


def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(4)
	head.next.next.next = Node(6)
	head.next.next.next.next = Node(7)
	head.next.next.next.next.next = Node(8)
	head.next.next.next.next.next.next = head.next.next
	print(has_cycle(head))

main()	


