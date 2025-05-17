from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def binary_search(intervals: List[List[int]], target: int) -> int:
            low, high = 0, len(intervals)
            while low < high:
                mid = (low + high) // 2
                if intervals[mid][0] < target:
                    low = mid + 1
                else:
                    high = mid
            return low  # 挿入すべき位置

        # 2分探索で newInterval の挿入位置を決定
        insert_pos = binary_search(intervals, newInterval[0])
        intervals.insert(insert_pos, newInterval)

        # 挿入後、マージ処理
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
