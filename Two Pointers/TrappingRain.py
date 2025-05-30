from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            j = n - i - 1
            left[i] = max(left[i-1], height[i-1])
            right[j] = max(right[j+1], height[j+1])
        for i in range(n):
            res += max(min(left[i], right[i]) - height[i], 0)
        
        return res