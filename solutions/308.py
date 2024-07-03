class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix  

    def update(self, row: int, col: int, val: int) -> None:
        if (row < len(self.matrix) and row >= 0) and (col < len(self.matrix[0]) and col >= 0):
            self.matrix[row][col] = val 
        return 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        regionSum = 0 
        for i in range(row1, row2+1): 
            regionSum += sum(self.matrix[i][col1:col2+1])
        return regionSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)