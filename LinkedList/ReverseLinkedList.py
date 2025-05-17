# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        
        nodes = list()
        while current:
            nodes.append(current.val)
            current = current.next
        rev_head = ListNode()
        current = rev_head
        while nodes:
            current.val = nodes.pop()
            if len(nodes) == 0:
                current.next = None
                break
            current.next = ListNode()
            current = current.next
        return rev_head