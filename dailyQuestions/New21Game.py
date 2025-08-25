class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        # n以下になる確率
        # k以上になるまで続ける
        # 1~maxPtsが出る
        dp = [0 for _ in range(0, n+1)] # dp[i]は合計がiになる確率
        dp[0] = 1 # 0からスタートだから0になる確率は1

        prob = 1/maxPts
        prev = 1
        left, right = 0, 0
        for i in range(1, n+1):
            if i-maxPts > k:
                break
            dp[i] = prev*prob

            if i < k:
                prev += dp[i]
            if i-maxPts >= 0:
                prev -= dp[i-maxPts]
            # dp[i] = sum(dp[max(0, i-maxPts):min(i, k)])*prob
            # print(dp)
        
        return sum(dp[k:n+1])
