from typing import List
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        dp = [[values[i]*values[i+1]*values[i+2] if j-i==2 else 0 for j in range(n)] for i in range(n)]
        for level in range(3, n):
            for i in range(n):
                j = i + level
                if j >= n:
                    continue
                min_val = 100 ** 4
                for k in range(i+1, j):
                    # print(i, j, k)
                    val = values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]
                    min_val = min(val, min_val)
                dp[i][j] = min_val
        
        return dp[0][n-1]