# Approach: 
#   - Use Breadth First Search, to scan the adjacent squares and look for an exit 
#       - BFS Example:
#           - Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
#                    entrance = [1,2]
#           - Start at 1, 2 -> add the adjacent squares to a queue 
#               - (x-1, y), (x+1, y), (x, y + 1), (x, y - 1) 
#               - explore each position then move onto the next unvisited square 
#       - Data Structures:
#           - Queue for our adjacent nodes, visit set to track visited cells 
#           - Counter to keep track of our steps
#   - Call BFS on each cell, updating steps afterwards until the first exit is found 
#   - Continue the BFS Call if cell != +  and we are within the maze 
#   - Entrance does not count as an exit -> How can we keep track of this? 
#       -maybe add a check to ensure this isn't the starting celll 
from collections import deque 
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q, visited = deque(), set() 
        
        sr, sc = entrance[0], entrance[1]
        q.append((sr, sc, 0))
        visited.add((sr, sc))
        
        while q:
            r, c, d = q.popleft()
            for dr, dc in directions: 
                row, col = (r + dr), (c + dc)
                if (0 <= row < ROWS and 0 <= col < COLS) and maze[row][col] == '.' and (row, col) not in visited:
                    if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1) and ((row, col) != (sr, sc)): 
                        return d + 1
                    q.append((row, col, d+1))
                    visited.add((row, col))
        return -1