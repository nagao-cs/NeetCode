class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [1 for _ in range(n+1)]

        #i-1段目から1stepでくるパターンと,
        #i-2段目から2stepでくるパターン
        """
        n = 4
        1. 1 * 4          3段目から1step
        2. 1*2 * 2        2段目から2step
        3. 1 + 2 + 1   -> 3段目から1step
        4. 2 + 1*2        3段目から1step
        4. 2*2            2段目から2step
        """
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]