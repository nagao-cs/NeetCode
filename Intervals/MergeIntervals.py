from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = list()

        intervals.sort()

        l = intervals[0][0]
        r = intervals[0][1]
        for interval in intervals[1:]:
            print(interval)
            if l <= interval[0] <= r:
                r = max(r, interval[1])
            else:
                output.append([l,r])
                l = interval[0]
                r = interval[1]

        output.append([l, r]) #最後の一組を追加

        return output