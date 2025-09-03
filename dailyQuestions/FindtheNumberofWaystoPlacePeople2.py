from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        x, y = 0, 1
        points.sort(key=lambda point: (point[x], -point[y]))

        count = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                alice = points[i]
                bob = points[j]

                if alice[y] < bob[y]:
                    continue
                is_inside = False
                for k in range(i+1, j):
                    staranger = points[k]
                    if alice[y] >= staranger[y] >= bob[y]:
                        is_inside = True
                        break
                if not is_inside:
                    count += 1
        
        return count