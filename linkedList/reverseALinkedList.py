class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    prev, current, next = None, head, None
    while current.next is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def reverseASubList(head, p, q):
    i = 0
    prev = None
    current = None
    while head.next is not None and i < p - 1:
        head = head.next
        current = head
        i += 1

    i = 0
    while current.next is not None and i < q - p + 1:
        next = current.next
        current.next = prev
        prev = current
        current = next
        i += 1


def reverseKelements(head, k):
    prev, current, temp = None, head, None
    count = 0
    while current.next is not None and count < k:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        count += 1

    # 1,2,3,4,5,6
    # 3,2,1,6,5,4
    # 1 will be head in both case and the data stored in temp is 4
    # so my head.next should be point to 4,5,6 to reverse these three elems
    # use recursion
    # -----------------------------------

    # extra condition to alternate reverse
    i = 0
    while temp.next is not None and i < k:
        temp = temp.next
        i += 1
    # ------------------------------------

    if temp is not None:
        head.next = reverseKelements(temp, k)
    return prev


def rotateALinkedList(head, k):
    current = head
    length = 0
    while current.next is not None:
        current = current.next
        length += 1

    current.next = head

    # if k > length, do---- k = k%(length+1)
    jump = length - k

    temp = head
    while jump:
        temp = temp.next
        jump -= 1

    head = temp.next
    temp.next = None
    return head



def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
   # Check if we need to reverse the group
    curr = head
    for _ in range(k):
        if not curr: return head
        curr = curr.next
                
    # Reverse the group (basic way to reverse linked list)
    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    # After reverse, we know that `head` is the tail of the group.
    # And `curr` is the next pointer in original linked list order
    head.next = self.reverseKGroup(curr, k)
    return prev






def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(7)
    head.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next = head.next.next
    print(reverse(head))


main()
