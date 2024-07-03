# 2D Array
# Count the number of islands in the graph
# Alogorithms to use
#  DFS / BFS
from collections import deque
class Solution:
    def breadthFirstSearch(self, row: int, col: int, seen: set, grid: list[list[str]]) -> int:
        # Create a queue for the adjacent cells 
        queue = deque()
        # Add the current cell to our seen set
        # this way we won't explore it again
        seen.add((row, col))
        # Add our current cell to the queue so we
        # can explore it in ur while loop
        queue.append((row, col))

        while queue:
            # row, col is our cell to be explored
            row, col = queue.popleft()
            # this will check the adjacent cells, 
            #            right     left     up      down
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            # Iterate through each adjacent cells 
            for dr, dc in direction:
                # Arithmetic will move our coordinates to adjacent cells 
                r, c = (row + dr), (col + dc)
                # Ensure that the cell is in within the bounds of the grid and is an island or '1' and 
                # it hasn't been explored yet
                if (r in range(len(grid))) and (c in range(len(grid[0]))) and (grid[r][c] == '1') and (r, c) not in seen:
                    # We do not increment the count here as adjacent cells with 1 are a part of the same island 
                    queue.append((r, c))
                    # Add to the seen set 
                    seen.add((r, c))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        # Store the number of rows and columns to iterate through 
        row, col = len(grid), len(grid[0])
        # Seen will ensure that we don't revisit the same cells again
        seen = set()
        islands = 0
        # Iterate through the grid 
        for r in range(row):
            for c in range(col):
                # If we find an island and we haven't visited it 
                # call BFS on it and explore the adjacent nodes 
                if grid[r][c] == '1' and (r, c) not in seen:
                    self.breadthFirstSearch(r, c, seen, grid)
                    # Increment our island count 
                    islands += 1
        return islands