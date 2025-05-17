# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 1
        while current.next != None:
            current = current.next
            length += 1
        i = 1
        n = length - n + 1
        start = ListNode(val=0, next=head)
        prev = start
        current = head
        #iは今いるノードがスタートから何個目か
        #nはスタートから何個目のノードを消すか
        while i != n:
            prev = current
            current = current.next
            i += 1
        if current.next:
            prev.next = current.next
        else:
            prev.next = None
        return start.next
        