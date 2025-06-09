from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(row:int, col:int, visited:set):
            #端からたどり着ける'O'を'Y'に変えていく
            board[row][col] = 'Y'
            visited.add((row, col))
            for dr, dc in directions:
                nd, nc = row+dr, col+dc
                if (0 <= nd < m) and (0 <= nc < n) and (board[nd][nc] == 'O') and ((nd, nc) not in visited):
                    dfs(nd, nc, visited)
        
        for row in [0, m-1]:
            for col in range(n):
                if board[row][col] == 'O':
                    dfs(row, col, set())
        # print(board)
        # print()
        for col in [0, n-1]:
            for row in range(m):
                if board[row][col] == 'O':
                    dfs(row, col, set())
        # print(board)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'Y':
                    board[row][col] = 'O'