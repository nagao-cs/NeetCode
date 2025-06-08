from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        can_reach_pacific = [[False for _ in range(n)] for _ in range(m)]
        can_reach_atlantic = [[False for _ in range(n)] for _ in range(m)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(start, matrix, visited):
            row, col = start
            visited[row][col] = True
            matrix[row][col] = True
            for r, c in directions:
                next_row = row+r
                next_col = col+c
                if (0 <= next_row < m) and (0 <= next_col < n) and (not visited[next_row][next_col]) and (heights[row][col] <= heights[next_row][next_col]):
                    dfs([next_row, next_col], matrix, visited)
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        for col in range(n):
            dfs([0, col], can_reach_pacific, visited)
        for row in range(m):
            dfs([row, 0], can_reach_pacific, visited)
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        for col in range(n):
            dfs([m-1, col], can_reach_atlantic, visited)
        for row in range(m):
            dfs([row, n-1], can_reach_atlantic, visited)

        res = list()
        for i in range(m):
            for j in range(n):
                if can_reach_pacific[i][j] and can_reach_atlantic[i][j]:
                    res.append([i, j])
        
        return res