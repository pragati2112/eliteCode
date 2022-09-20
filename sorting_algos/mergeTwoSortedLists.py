class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    if max(l1) > max(l2):
        sorted_arr = l2 + l1
    else:
        sorted_arr = l1 + l2

    i = 0
    j = 0
    k = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            sorted_arr[k] = l1[i]
            i = i + 1
        else:
            sorted_arr[k] = l2[j]
            j = j + 1

        k = k + 1

    return sorted_arr


l1 = [0, 1]
l2 = [0]

l1 = ListNode(l1)
l2 = ListNode(l2)


def mergeTwoLists1(l1, l2):
    sorted_arr = ListNode(0)
    current = sorted_arr

    while (l1 != None and l2 != None):
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next

        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    if l1:
        sorted_arr.next = l1
    if l2:
        sorted_arr.next = l2

    return current.next


print(mergeTwoLists1(l1, l2))
