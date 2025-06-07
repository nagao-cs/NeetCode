from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_line = len(grid)
        num_row = len(grid[0])
        current = grid
        minute = 0
        num_rotten = 0
        num_orange = 0
        for line in range(num_line):
            for row in range(num_row):
                if grid[line][row] > 0:
                    num_orange += 1
                    if grid[line][row] == 2:
                        num_rotten += 1
        prev = [row[:] for row in current]
        while True:
            if num_rotten == num_orange:
                return minute
            elif minute != 0 and prev == current:
                return -1
            prev = [row[:] for row in current]
            for line in range(num_line):
                for row in range(num_row):
                    if prev[line][row] == 1:
                        if line == 0:
                            upper = 0 #上は空
                        else:
                            upper = prev[line-1][row]
                        if line == num_line-1:
                            under = 0 #下は空
                        else:
                            under = prev[line+1][row]
                        if row == 0:
                            left = 0
                        else:
                            left = prev[line][row-1]
                        if row == num_row-1:
                            right = 0
                        else:
                            right = prev[line][row+1]

                        if upper == 2 or under == 2 or left == 2 or right == 2:
                            current[line][row] = 2
                            num_rotten += 1
            minute += 1
        