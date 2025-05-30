from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind(grid)
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or grid[i][j] == '0':
                    continue
                #grid[i][j]=='1'
                if j > 0:
                    #左隣がいる
                    if grid[i][j-1] == '1':
                        uf.union((i,j-1), (i,j))
                if i > 0:
                    if grid[i-1][j] == '1':
                        uf.union((i-1, j), (i,j))
        return uf.size

class UnionFind:
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.size = 0
        self.par = list()
        for i in range(m):
            self.par.append([(-1, -1)]*n)
            for j in range(n):
                if grid[i][j] == '1':
                    self.par[i][j] = (i,j)
                    self.size += 1
        
    def root(self, cell:tuple) -> tuple:
        x, y = cell
        if self.par[x][y] == (x, y):
            return (x, y)
        root_val = self.root(self.par[x][y])
        self.par[x][y] = root_val
        return root_val

    def union(self, cell_1, cell_2):
        r1 = self.root(cell_1)
        r2 = self.root(cell_2)
        if r1 == r2:
            return
        else:
            if r1 < r2:
                self.par[r2[0]][r2[1]] = r1
                self.size -= 1
            else:
                self.par[r1[0]][r1[1]] = r2
                self.size -= 1