from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list() #スタックの末尾から先頭に向けて、単調増加なスタック
        ans = [0 for _ in range(len(temperatures))]

        for day, temperature in enumerate(temperatures):
            if not stack:
                stack.append((day, temperature))
            
            elif stack[-1][1] >= temperature:
                stack.append((day, temperature))
            else:
                while stack and stack[-1][1] < temperature:
                    i, _ = stack.pop()
                    ans[i] = day - i
                stack.append((day, temperature))        
        
        return ans