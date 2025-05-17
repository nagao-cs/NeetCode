class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        MAX = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            MAX = max(MAX, area)
            # print(l, r, area, MAX)

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return MAX
        