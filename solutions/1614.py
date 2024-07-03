class Solution:
    # Asymptotic Analysis:
    # Time | O(n) - Loop through len(s) 
    # Space | O(1) - 2 Constants maxDepth & currDepth
    def maxDepth(self, s: str) -> int:
        if len(s) == 0: 
            return 0 
        
        maxDepth, currDepth = 0, 0  

        for char in s:
            if char == '(': 
                currDepth += 1 
            elif char == ')':
                currDepth -= 1
            maxDepth = max(maxDepth, currDepth) 
        return maxDepth     