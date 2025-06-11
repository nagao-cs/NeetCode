from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.res = list()

        def duplicate(board, col) -> bool:
            row = len(board)
            if col in board:
                return True
            for x, y in enumerate(board):
                if abs(row-x) == abs(col-y):
                    return True
            return False
        
        def addboard(board):
            ans = list()
            for col in board:
                left = "."*(col)
                right = "."*(self.n-col-1)
                ans.append(left+'Q'+right)
            self.res.append(ans)
        def Nqueen(board, row):
            # boardはクイーンがすでに置かれているマスのリスト(board[i]はi+1行目の列番号)
            # rowはこれからクイーンを置く行
            if row == self.n:
                addboard(board)
            else:
                for col in range(self.n):
                    #colはこれからクイーンを置く列(左から順に調べる)
                    if not duplicate(board, col):
                        board.append(col)
                        Nqueen(board, row+1)
                        board.pop()
                    else:
                        continue

        
        Nqueen(list(), 0)
        return self.res
