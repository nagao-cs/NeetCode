from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort(key=lambda interval:interval[0])

        start, end = 0, 1
        prev = intervals[0]
        for interval in intervals[1:]:
            current = interval
            if prev[end] <= current[start]:
                prev = current
            elif prev[end] > current[start]:
                if prev[end] >= current[end]:
                    removed += 1
                    prev = current
                elif prev[end] < current[end]:
                    removed += 1
        
        return removed