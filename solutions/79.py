from collections import defaultdict, Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board and word: return False 
        ROWS, COLS = len(board), len(board[0])

        wordDict, boardDict = Counter(word), defaultdict(int) 
        for r in range(ROWS):
            for c in range(COLS):
                boardDict[board[r][c]] += 1 
        
        for c in word: 
            if c not in boardDict or boardDict[c] < wordDict[c]:
                return False 
        
        def dfs(r, c, k, board): 
            if r not in range(ROWS) or c not in range(COLS) or k >= len(word) or word[k] != board[r][c]:
                return False 

            if k == len(word) - 1:
                return True 

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions: 
                temp = board[r][c]
                board[r][c] = float('-inf')
                if dfs(r + dr, c + dc, k + 1, board):
                    return True 
                board[r][c] = temp 
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, board):
                        return True
        return False 