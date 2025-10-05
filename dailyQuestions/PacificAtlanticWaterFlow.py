from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m:int = len(heights)
        n:int = len(heights[0])

        directions:list = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        pacific_reachable = set()
        def is_reachable_pacific(row:int, col:int, visited:set, reachable:set):
            if row == 0 or col == 0:
                return True
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if (nr, nc) in visited:
                    continue
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] <= heights[row][col]:
                        if (nr, nc) in reachable:
                            return True
                        visited.add((nr, nc))
                        if is_reachable_pacific(nr, nc, visited, reachable):
                            return True
            return False

        atlantic_reachable = set()
        def is_reachable_atlantic(row:int, col:int, visited:set, reachable:set):
            if row == m-1 or col == n-1:
                return True
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if (nr, nc) in visited:
                    continue
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] <= heights[row][col]:
                        if (nr, nc) in reachable:
                            return True
                        visited.add((nr, nc))
                        if is_reachable_atlantic(nr, nc, visited, reachable):
                            return True
            return False

        res = list()
        for row in range(m):
            for col in range(n):
                if is_reachable_pacific(row, col, set(), pacific_reachable):
                    pacific_reachable.add((row, col))
                if is_reachable_atlantic(row, col, set(), atlantic_reachable):
                    atlantic_reachable.add((row, col))
                
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    res.append([row, col])
        return res
        