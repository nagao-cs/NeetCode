from typing import List
from pprint import pprint
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        res = [-1] * n
        tmp = list()
        for index, query in enumerate(queries):
            tmp.append((query, index))
        new_queries = sorted(tmp, key=lambda x:x[0])

        intervals.sort(key=lambda interval:interval[0])

        pointer = 0
        minHeap = list()
        for query, index in new_queries:
            while pointer < len(intervals) and intervals[pointer][0] <= query:
                left, right = intervals[pointer]
                heapq.heappush(minHeap, (right-left+1, left, right))
                pointer += 1

            while minHeap:
                size, left, right = minHeap[0]
                if left <= query <= right:
                    res[index] = size
                    break
                elif query > right:
                    heapq.heappop(minHeap)
        
        return res