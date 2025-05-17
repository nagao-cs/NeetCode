class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1   # 金額 0 を作る方法は 1 通り
        
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j - coin]
        return dp[amount]
