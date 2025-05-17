class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = dict()

        for i in range(n):
            for j in range(i+1, n):
                edges[(i, j)] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        edges = sorted(edges.items(), key=lambda x:x[1])

        uf = UnionFind(n)
        total_cost = 0 

        for (x, y), cost in edges:
            if uf.root(x) != uf.root(y):
                uf.union(x, y)
                total_cost += cost
        
        return total_cost


class UnionFind:
    def __init__(self, numNode):
        self.par = [i for i in range(numNode)]
        #node_iの親ノード,最初は各ノードの親は自身
    
    def root(self, x: int) -> int:
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def union(self, x: int, y: int) -> None:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.par[rx] = ry