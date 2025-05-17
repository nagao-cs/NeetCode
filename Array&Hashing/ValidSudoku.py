class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_set = set()
            for cell in row:
                if cell == '.':
                    continue
                if cell not in row_set:
                    row_set.add(cell)
                else:
                    print(cell, row_set)
                    return False
        print("Ok row")
        collum = 0
        while collum < 9:
            collum_set = set()
            row = 0
            while row < 9:
                cell = board[row][collum]
                if cell == '.':
                    pass
                elif cell not in collum_set:
                    collum_set.add(cell)
                else:
                    return False
                row += 1
            collum += 1
        print("Ok collum")

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                subboard_set = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[row+i][col+j]
                        if cell == '.':
                            pass
                        elif cell not in subboard_set:
                            subboard_set.add(cell)
                        else:
                            return False
        print("Ok sub_board")

        return True