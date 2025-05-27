from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        def rob2(nums:list, l:int, r:int) -> int:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[:2])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
            return dp[-1]

        
        return max(rob2(nums[0:n-1], 0, n-2), rob2(nums[1:], 1, n-1))