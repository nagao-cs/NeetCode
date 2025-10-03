from typing import List
import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        minHeap = list()
        visited = set()
        m, n = len(heightMap), len(heightMap[0])
        for i in range(m):
            if i == 0 or i == m-1:
                for j in range(n):
                    visited.add((i, j))
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
            else:
                visited.add((i, 0))
                visited.add((i, n-1))
                heapq.heappush(minHeap, (heightMap[i][0], i, 0))
                heapq.heappush(minHeap, (heightMap[i][n-1], i, n-1))
                
        count = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while minHeap:
            height, x, y = heapq.heappop(minHeap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n) and ((nx, ny) not in visited):
                    visited.add((nx, ny))
                    count += max(height - heightMap[nx][ny], 0)
                    newheight = max(height, heightMap[nx][ny])
                    heapq.heappush(minHeap, (newheight, nx, ny))
                        
        return count