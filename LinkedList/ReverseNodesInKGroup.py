# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #headからk個のノードを逆向きにして、残りは次の関数に渡す
        #headからノードがk個なければそのままheadを返す
        # print_linkedlist(head)
        stack = list()
        current = head
        count = k
        while count > 0:
            if not current:
                return head
            stack.append(current)
            count -= 1
            current = current.next
        
        reverse_head = ListNode()
        prev = reverse_head
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        prev.next = self.reverseKGroup(current, k)
        # print(reverse_head)
        return reverse_head.next

def print_linkedlist(node):
    while node:
        print(node.val, end=' -> ')
        node = node.next
    print('None')