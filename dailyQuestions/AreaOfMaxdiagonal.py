from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = -1
        maxdiagonal = 0

        for length, width in dimensions:
            diagonal = (length**2 + width**2)**(1/2)
            if diagonal == maxdiagonal:
                area = length * width
                ans = max(ans, area)
            elif diagonal > maxdiagonal:
                area = length * width
                ans = area
                maxdiagonal = diagonal
            #     print(f"dia:{dia}, ans:{ans}")
            # print(f"area:{length*width}, diagonal:{diagonal}")
        return ans