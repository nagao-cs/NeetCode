from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_pos = dict() # charの最初と最後の場所を記録する
        start, end = 0, 1
        for index, char in enumerate(s):
            if not char in char_pos:
                char_pos[char] = [index, index]
            else:
                char_pos[char][end] = index
        # print(char_pos)
        intervals = list()
        for interval in char_pos.values():
            i = 0
            new_intervals = list()
            while i < len(intervals) and intervals[i][end] < interval[start]:
                new_intervals.append(intervals[i])
                i += 1
            if i == len(intervals):
                new_intervals.append(interval)
            else:
                l = intervals[i][start]
                while i < len(intervals) and interval[end] > intervals[i][start]:
                    i += 1
                if i == len(intervals):
                    r = max(intervals[-1][end], interval[end])
                    new_intervals.append([l, r])
                else:
                    r = max(intervals[i][end], interval[end])
                    new_intervals.append([l, r])
                    new_intervals.extend(intervals[i+1:])
            intervals = new_intervals
        # print(intervals)
        res = list()
        for l, r in intervals:
            res.append(r-l+1)

        return res
                    