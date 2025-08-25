class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat)-1, len(mat[0])-1
        output = list()
        # print(m, n)
        row, col = 0, 0
        up = True
        while row != m or col != n:
            if up:
                # print(f"right-up, (row, col) = ({row}, {col})")
                while not (row == 0 or col == n):
                    output.append(mat[row][col])
                    row -= 1
                    col += 1
                output.append(mat[row][col])
                if col < n:
                    col += 1
                else:
                    row += 1
                up = False
            else:
                # print(f"left-down, (row, col) = ({row}, {col})")
                while not (col == 0 or row == m):
                    output.append(mat[row][col])
                    row += 1
                    col -= 1
                output.append(mat[row][col])
                if row < m:
                    row += 1
                else:
                    col += 1
                up = True
            # print(output)
        output.append(mat[row][col])
        return output