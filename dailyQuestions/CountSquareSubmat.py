class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0
        dp = [[0 for _ in range(n)] for __ in range(m)]

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    continue
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1]) + 1
                count += dp[row][col]
        # print(dp)
        return count
