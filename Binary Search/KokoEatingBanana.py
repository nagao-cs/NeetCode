import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        ans = 0

        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            total = 0 #すべてのバナナを食べるのにかかった時間
            for pile in piles:
                total += math.ceil(pile/mid)
            # print(f"{mid}で食べると{total}時間かかる")
            if total > h:
                #時間内に食べきれないなら、1時間で食べる量を増やす
                l = mid+1
            elif total <= h:
                #時間ちょうどかそれより早く食べきるなら、仮の答えとして1時間で食べる量を減らす
                ans = mid
                r = mid-1


        return ans