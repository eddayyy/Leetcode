# Approach: 
#   - 2 Pointer approach: 
#       - use the isspace() method to solve this 
#   - Use a list to keep track of the string
#   - modify the list in place with the letters and such 

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        if n == 0: 
            return ''
        
        left, right = 0, n-1 
        while left <= right and s[left] == ' ': 
            left += 1
        while left <= right and s[right] == ' ': 
            right -= 1
        
        d, word = deque(), [] 
        while left <= right: 
            if s[left] == ' ' and word: 
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1

        d.appendleft(''.join(word)) 
        return ' '.join(d)