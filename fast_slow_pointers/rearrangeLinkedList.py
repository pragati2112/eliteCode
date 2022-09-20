class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_list(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def rearrange_list(head):
    mid = find_middle_of_list(head)
    second_half = reverse(mid)
    first_half = head
    while first_half is not None and second_half is not None:
        tmp = first_half.next
        first_half.next = second_half
        first_half = tmp

        tmp = second_half.next
        second_half.next = first_half
        second_half = tmp


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(8)
    head.next.next.next.next.next = Node(10)
    print(rearrange_list(head))


main()
