from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = {i for i in range(n+1)}

        for num in nums:
            res.discard(num)
        
        res = list(res)
        return res[0]