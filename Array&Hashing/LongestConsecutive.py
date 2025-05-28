from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_to_index = {}
        nums = list(set(nums))  # 重複除去
        nums.sort()
        uf = UnionFind(nums)

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                uf.unite(i-1, i)

        return max(uf.get_size(i) for i in range(len(nums)))

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(len(n))]
        self.size = [1] * len(n)

    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x]) 
        return self.par[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.par[rx] = ry
        self.size[ry] += self.size[rx]

    def get_size(self, x):
        return self.size[self.root(x)]
