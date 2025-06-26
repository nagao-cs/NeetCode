import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def reach(time):
            for row, col in reachable:
                current_depth = max(grid[row][col], time)
                for dr, dc in directions:
                    next_row = row + dr
                    next_col = col + dc
                    if 0 <= next_row < n and 0 <= next_col < n:
                        next_depth = max(grid[next_row][next_col], time)
                        if current_depth == next_depth and (next_row, next_col) not in reachable:
                            reachable.append((next_row, next_col))
                        elif time < next_depth and next_depth not in minheap:
                            heapq.heappush(minheap, next_depth)
        n = len(grid)
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        minheap = list()
        heapq.heappush(minheap, max(grid[0][0], grid[n-1][n-1]))
        reachable = [(0,0)]
        time = 0
        while True:
            reach(time)
            if (n-1, n-1) not in reachable:
                time = heapq.heappop(minheap)
            else:
                return time