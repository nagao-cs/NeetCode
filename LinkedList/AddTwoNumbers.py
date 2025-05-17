# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        carry = 0

        while True:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10
            sum = sum % 10
            current.next = ListNode(sum)
            current = current.next

            if not (l1 or l2):
                if carry == 1:
                    current.next = ListNode(carry)
                break

        return head.next 