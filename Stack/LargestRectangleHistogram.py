from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        stack = list() #高さが昇順に並んだmonotonic stack
        maxArea = 0
        for i in range(n):
            j = 0
            while stack and heights[stack[-1]] > heights[i]:
                #現在の棒よりも高い棒は、その棒の次に高い棒の位置+1から現在の位置-1まで伸ばせる
                j = stack.pop()
                height = heights[j]
                if not stack:
                    bottom = i
                else:
                    bottom = i - stack[-1] - 1
                maxArea = max(maxArea, height*bottom)
            height = heights[i]
            if not stack:
                #スタックが空なら、現在の棒は左端から現在の位置まで伸ばせる
                bottom = i + 1
            else:
                #スタックが空でないなら、現在の棒はスタックのトップにある棒+1から現在の位置まで伸ばせる
                bottom = i - stack[-1]
            maxArea = max(maxArea, height*bottom)
            stack.append(i)
        
        return maxArea