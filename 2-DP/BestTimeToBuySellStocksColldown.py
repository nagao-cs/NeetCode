from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]
        # dp[i][0]はi日目に株を保持、dp[i][1]はi日目に売る、dp[i][2]はi日目に買える状態の利益の最大値

        dp[0][0] = -prices[0]
        dp[0][1] = -1000


        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0]+prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        # print(dp)
        return max(dp[-1][1], dp[-1][2])