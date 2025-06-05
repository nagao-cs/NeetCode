from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total//2
        n = len(nums)

        dp = [[False for _ in range(target+1)] for __ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(target+1):
                #nums[:i]までを使ってjは作れるか
                if nums[i-1] <= j:
                    dp[i][j] = (dp[i-1][j-nums[i-1]]) or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]