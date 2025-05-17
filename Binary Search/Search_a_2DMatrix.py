class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            for cell in matrix[0]:
                print(cell, target)
                if cell == target:
                    return True
            return False
        pivot = matrix[len(matrix)//2][0]
        if target < pivot:
            return self.searchMatrix(matrix[0:len(matrix)//2], target)
        elif target >= pivot:
            return self.searchMatrix(matrix[len(matrix)//2:], target)
        
