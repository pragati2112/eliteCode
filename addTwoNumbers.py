class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2, carry=0):
    result = ListNode(0)
    current = result
    
    while l1 or l2 or carry:

        if l1.val:
            val1 = l1.val
        else:
            val1 = 0 

        if l2.val:
            val2 = l2.val
        else:
            val2 = 0       


        carry, last_digit = divmod(l1+l2+carry, 10)

        current.next = ListNode(last_digit)
        current = current.next

        if l1:
            l1= l1.next
        else:
            None 

        if l2:
            l2= l2.next
        else:
            None  
                 
    return result.next


l1 = [ 9, 9, 9, 9, 9,9]
l2 = [7, 8, 8]

print(addTwoNumbers(l1, l2))
