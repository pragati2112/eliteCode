class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers1(l1, l2):
    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)

        val2 = (l2.val if l2 else 0)

        carry, out = divmod(val1 + val2 + carry, 10)

        result_tail.next = ListNode(out)

        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next


list1 = 1
list2 = 2

l1 = ListNode(list1)
l2 = ListNode(list2)

print(addTwoNumbers1(l1, l2))
