class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)-1
        cols = len(matrix[0]) -1
        for i in range(row):
            for j in range(cols):
                if matrix[i][j]!= matrix[i+1][j+1]:
                    return False
        return True
