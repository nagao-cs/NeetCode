from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = list()
        uf = UnionFind(n)
        for x, y in edges:
            if uf.root(x) != uf.root(y):
                uf.union(x, y)
            else:
                res = [x, y]

        return res


class UnionFind:
    def __init__(self, n):
        self.par = {i:i for i in range(1, n+1)}
        # print(self.par)
    
    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.par[rx] = ry
        # print(self.par)