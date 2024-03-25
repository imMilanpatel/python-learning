'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Dummy node to simplify the code
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Calculate sum and carry
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        
        carry = sum_val // 10
        sum_val %= 10

        # Create new node with the sum and append it to the result linked list
        current.next = ListNode(sum_val)
        current = current.next

    return dummy.next

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Test cases
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
printLinkedList(result)