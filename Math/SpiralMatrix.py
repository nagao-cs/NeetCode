from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = list()
        for row in matrix: print(row)
        if not matrix:
            return []
        m = len(matrix[0]) #列数
        n = len(matrix) #行数
        if m == 0:
            return []

        #0行目を追加
        output.extend(matrix[0])
        if n == 1:
            return output
        
        #-1列目を追加
        output.extend([row[-1] for row in matrix[1:]])
        if m == 1:
            return output
        #-1行目を追加
        i = n-1
        output.extend(matrix[i][-2::-1])
        #0列目を追加
        i -= 1
        while i > 0:
            output.append(matrix[i][0])
            i -= 1

        small_matrix = [[cell for cell in row[1:m-1]] for row in matrix[1:n-1]]
        output.extend(self.spiralOrder(small_matrix))

        return output