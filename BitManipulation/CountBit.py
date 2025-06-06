from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(n+1):
            val = i
            while val > 0:
                ans[i] += int(val & 1)
                val = val >> 1

        return ans 