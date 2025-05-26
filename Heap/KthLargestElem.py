import heapq
from typing import Optional, List
class KthLargest:
    k: int
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = list()
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

class Heap:
    def __init__(self):
        self.heap = list()
    
    def insert(self, val) -> None:
        self.heap.append(val)
        current = len(self.heap)-1
        par = (current-1)//2
        while current > 0 and self.heap[current] < self.heap[par]:
            self.heap[current], self.heap[par] = self.heap[par], self.heap[current]
            current = par
    
    def pop(self) -> Optional[int]:
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        popped = self.heap[0]
        self.heap[0] = self.heap.pop()
        current = 0
        while 2*current+1 < len(self.heap):
            left, right = 2*current+1, 2*(current+1)
            if not right < len(self.heap):
                child = left
            else:
                if self.heap[left] < self.heap[right]:
                    child = left
                else:
                    child = right
            if self.heap[current] > self.heap[child]:
                self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
                current = child
            else:
                break
        return popped
    
    def size(self) -> int:
        return len(self.heap)
    
    def top(self) -> Optional[int]:
        if not self.heap:
            return None
        return self.heap[0]
    
    def show(self) -> None:
        print(self.heap)




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)