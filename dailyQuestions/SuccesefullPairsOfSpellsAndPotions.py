import bisect
from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_potions = sorted(potions)
        n = len(sorted_potions)
        ans = list()
        for spell in spells:
            required = success / spell
            idx = bisect.bisect_left(sorted_potions, required)
            ans.append(n - idx)
        
        return ans