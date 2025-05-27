from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(list(filter(lambda coin:coin <= amount, coins)))
        dp = [amount+1] * (amount+1) #dp[i]はiを作るの必要な最小のコインの枚数
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins[::-1]:
                if i-coin >= 0 and dp[i-coin] != amount+1:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                    

        return dp[-1] if dp[-1] != amount+1 else -1

