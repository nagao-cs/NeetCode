class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xmin, xmax, ymin, ymax = n, 0, m, 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    xmin = min(xmin, col)
                    xmax = max(xmax, col)
                    ymin = min(ymin, row)
                    ymax = max(ymax, row)
        
        return (xmax-xmin+1) * (ymax-ymin+1)