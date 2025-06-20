from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        res = 1
        def dfs(row, col): # 現在地([row][col]から何回深ぼれるか)
            if dp[row][col] != 0:
                return dp[row][col]
            depth = 1
            current = matrix[row][col]
            for dr, dc in directions:
                next_row = row+dr
                next_col = col+dc
                if (0 <= next_row < m and 0 <= next_col < n) and current < matrix[next_row][next_col]:
                    depth = max(depth, dfs(next_row, next_col)+1)
            dp[row][col] = depth
            return dp[row][col]

        for row in range(m):
            for col in range(n):
                dfs(row, col)
                res = max(res, dp[row][col])
        
        return res