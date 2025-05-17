# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = list()
        for linkedlist in lists:
            current = linkedlist
            while current:
                heap.append(current.val)
                i = len(heap)-1
                while i > 0: #ヒープの再構築
                    parent = (i-1)//2
                    if heap[i] < heap[parent]:
                        heap[i], heap[parent] = heap[parent], heap[i]
                        i = parent
                    else:
                        break
                current = current.next
        print(heap)
        if not heap:
            return 
        current = ListNode()
        head = ListNode(next=current)

        while heap:
            current.val = heap[0]
            #ヒープの再構築
            if len(heap) == 1:
                break
            heap[0] = heap.pop()
            i = 0
            while True:
                if 2*i+1 >= len(heap):#左の子がいない
                    break
                else:
                    left = 2*i+1
                if 2*(i+1) >= len(heap):
                    child = left
                else:#右の子がいる
                    right = 2*(i+1)
                    if heap[left] < heap[right]:
                        child = left
                    else:
                        child = right
                if heap[i] > heap[child]:
                    heap[i], heap[child] = heap[child], heap[i]
                    i = child
                else:
                    break
            current.next = ListNode()
            current = current.next
        return head.next