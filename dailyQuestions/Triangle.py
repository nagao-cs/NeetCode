from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[num for num in row] for row in triangle]
        
        for r_idx in range(1, len(triangle)):
            dp[r_idx][0] += dp[r_idx-1][0]
            for i in range(1, len(triangle[r_idx])-1):
                dp[r_idx][i] += min(dp[r_idx-1][i-1], dp[r_idx-1][i])
            dp[r_idx][-1] += dp[r_idx-1][-1]

        return min(dp[-1])