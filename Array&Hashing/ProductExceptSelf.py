from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        leftside = [1] * n
        rightside = [1] * n
        for i in range(1, n):
            leftside[i] = leftside[i-1]*nums[i-1]
        for j in range(n-2, -1, -1):
            rightside[j] = rightside[j+1]*nums[j+1]

        for i in range(n):
            output[i] = leftside[i] * rightside[i]
        
        return output