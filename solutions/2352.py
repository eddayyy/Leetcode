class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0: 
            return 0 

        rowMap, colMap = defaultdict(int), defaultdict(int) 
        counter = 0 

        for row in grid: 
            rowMap[tuple(row)] += 1

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            counter += rowMap[tuple(col)]

        return counter    