from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        num_class = len(classes)
        max_average = 0.0

        maxHeap = list()
        for passed, total in classes:
            gain = (passed+1)/(total+1) - passed/total
            heapq.heappush(maxHeap, (-gain, passed, total))

        for _ in range(extraStudents):
            gain, passed, total = heapq.heappop(maxHeap)
            passed += 1
            total += 1
            gain = (passed+1)/(total+1) - passed/total
            heapq.heappush(maxHeap, (-gain, passed, total))

        total_ratio = 0
        for _, passed, total in maxHeap:
            total_ratio += passed/total
        return total_ratio/num_class

# class Heap:
#     def __init__(self, classes):
#         self.heap = list()
#         for passed, total in classes:
#             self.push(passed, total)
    
#     def __str__(self):
#         return f"{self.heap}"

#     def __iter__(self):
#         yield from self.heap

#     def __len__(self):
#         return len(self.heap)

#     def push(self, passed, total):
#         self.heap.append((passed, total))
#         current = len(self.heap) - 1
#         while current > 0:
#             parent = (current - 1) // 2
#             current_gain = ((self.heap[current][0]+1) / (self.heap[current][1]+1)) - (self.heap[current][0] / self.heap[current][1])
#             parent_gain = ((self.heap[parent][0]+1) / (self.heap[parent][1]+1)) - (self.heap[parent][0] / self.heap[parent][1])
#             if current_gain > parent_gain:
#                 self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
#                 current = parent
#             else:
#                 break
    
#     def pop(self):
#         if len(self.heap) == 0:
#             return

#         val = self.heap[0]
#         if len(self.heap) == 1:
#             self.heap.pop()
#             return val
        
#         self.heap[0] = self.heap.pop()
#         current = 0
#         while current < len(self.heap):
#             left = 2 * current + 1
#             right = 2 * (current + 1)
#             if left >= len(self.heap):
#                 break
#             if right >= len(self.heap):
#                 child = left
#             else:
#                 left_gain = ((self.heap[left][0]+1) / (self.heap[left][1]+1)) - (self.heap[left][0] / self.heap[left][1])
#                 right_gain = ((self.heap[right][0]+1) / (self.heap[right][1]+1)) - (self.heap[right][0] / self.heap[right][1])
#                 if left_gain > right_gain:
#                     child = left
#                 else:
#                     child = right
#             current_gain = ((self.heap[current][0]+1) / (self.heap[current][1]+1)) - (self.heap[current][0] / self.heap[current][1])
#             child_gain = ((self.heap[child][0]+1) / (self.heap[child][1]+1)) - (self.heap[child][0] / self.heap[child][1])
#             if current_gain > child_gain:
#                 break
#             else:
#                 self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
#                 current = child
#         return val