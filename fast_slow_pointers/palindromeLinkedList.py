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


def reverse(head):
    prev = None
    while (head is not None):
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def palindromeLinkedList(head):
    mid = find_middle_of_list(head)
    head_reversed_second_half = reverse(mid)
    copy_second_half = head_reversed_second_half

    while head is not None and head_reversed_second_half is not None:
        if head != head_reversed_second_half:
            break

        head = head.next
        head_reversed_second_half = head_reversed_second_half.next

    if head is not None and head_reversed_second_half is not None:
        return True

    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    print(mid_linked_list(head))


main()
