from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            if dp[i-1] < 0:
                continue
            dp[i] = dp[i-1]+dp[i]
        
        return max(dp)