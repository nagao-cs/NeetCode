import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        time_from_start = [[n**2 for _ in range(n)] for _ in range(n)]
        time_from_start[0][0] = grid[0][0]
        
        minHeap = list()
        heapq.heappush(minHeap, (grid[0][0], (0, 0)))
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        while minHeap:
            time, (row, col) = heapq.heappop(minHeap)
            
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < n and 0 <= nc < n:
                    take_time = max(time, grid[nr][nc])
                    if take_time < time_from_start[nr][nc]:
                        time_from_start[nr][nc] = take_time
                        heapq.heappush(minHeap, (take_time, (nr, nc)))
        
        return time_from_start[n-1][n-1]
            