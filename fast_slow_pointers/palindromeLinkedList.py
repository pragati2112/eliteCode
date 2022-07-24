class Node():
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def palindromeLinkedList():
	pass


def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(4)
	head.next.next.next = Node(5)
	head.next.next.next.next = Node(2)
	head.next.next.next.next.next = Node(1)
	head.next.next.next.next.next.next = head.next.next
	print(mid_linked_list(head))

main()	