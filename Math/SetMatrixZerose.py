from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        MAX = 2**31
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for col in range(n):
                        if matrix[i][col] != 0:
                            matrix[i][col] = MAX
                    for row in range(m):
                        if matrix[row][j] != 0:
                            matrix[row][j] = MAX
                    
                    
        print(matrix)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == MAX:
                    matrix[i][j] = 0
