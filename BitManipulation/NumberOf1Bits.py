class Solution:
    def hammingWeight(self, n: int) -> int:
        cur = n
        res = 0
        while cur > 0:
            if cur % 2 == 1:
                res += 1
            cur  = cur // 2
        return res