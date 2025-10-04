from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        while n > 1:
            nums = [(nums[i] + nums[i+1]) % 10 for i in range(n-1)]
            n = len(nums)
        
        return nums[0]