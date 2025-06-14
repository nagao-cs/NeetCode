from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total <  target:
            return 0

        # Pを+のグループの和、Nを-のグループの和とする
        # P - N = target
        # P + N = total
        # P = (target + total) / 2
        # targetの正負はPとNを入れ替えるだけなので絶対値で考える
        #このPを作れる組み合わせが何通りあるか
        P = (abs(target)+total)/2
        if not P.is_integer():
            return 0
        else:
            P = int(P)
        
        dp = [[0 for j in range(P+1)] for i in range(n)]
        #dp[i][j]はnumsのi番目まででjを作る組み合わせの数
        for j in range(P+1):
            if j == 0:
                if nums[0] == 0:
                    dp[0][j] = 2
                else:
                    dp[0][j] = 1
            elif nums[0] == j:
                dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(P+1):
                if j-nums[i] > -1:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n-1][P]
        