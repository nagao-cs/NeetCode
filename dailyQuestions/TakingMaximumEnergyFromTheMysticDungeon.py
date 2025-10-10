from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        dp = [0 for _ in range(n)]

        for i in range(n-1, -1, -1):
            if i + k >= n:
                dp[i] = energy[i]
            else:
                dp[i] = dp[i+k] + energy[i]

        return max(dp)