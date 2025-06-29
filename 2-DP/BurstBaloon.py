from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for length in range(2, n):
            for i in range(n-length):
                j = i + length
                # print(i, j)
                dp[i][j] = max(dp[i][k]+dp[k][j]+(nums[i]*nums[k]*nums[j]) for k in range(i+1, j))
                # pprint(dp)
        # pprint(dp)
        return dp[0][n-1]