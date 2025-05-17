# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        stack = list()
        current = head
        while current:
            stack.append(current)
            current = current.next

        n = len(stack)
        mid = n // 2

        l = head
        for _ in range(mid):
            r = stack.pop()
            next_l = l.next
            l.next = r
            r.next = next_l
            l = next_l
        
        l.next = None