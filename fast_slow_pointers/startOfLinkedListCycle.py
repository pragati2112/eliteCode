class Node():
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def has_cycle(head):
	len_of_cycle = 0
	fast,slow = head, head
	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next 
		if slow == fast:
			len_of_cycle = length_of_cycle(slow)
			break

	return find_start(head, len_of_cycle)


def length_of_cycle(slow):
	current = slow
	counter = 0
	while True:
		current = current.next
		counter+=1
		if slow==current:
			break;
	return counter		


def find_start(head, len_of_cycle):
	pointer1, pointer2 = head, head

	while len_of_cycle>0:
		pointer2 = pointer2.next
		len_of_cycle=-1

	while pointer2 != pointer1:
		pointer2 = pointer2.next
		pointer1 = pointer1.next
	return pointer1	





def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(4)
	head.next.next.next = Node(6)
	head.next.next.next.next = Node(7)
	head.next.next.next.next.next = Node(8)
	head.next.next.next.next.next.next = head.next.next

	print(str(has_cycle(head).value))

main()	