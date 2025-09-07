from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            half = [x for x in range(1, n//2 + 1)]
            minus_half = [-x for x in range(1, n//2 + 1)]
            output = half + minus_half
        else:
            half = [x for x in range(1, n//2 + 1)]
            minus_half = [-x for x in range(1, n//2 + 1)]
            output = half + minus_half + [0]
        
        return output