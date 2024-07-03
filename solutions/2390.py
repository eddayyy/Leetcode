class Solution:
    def removeStars(self, s: str) -> str:
        stack = [] 
        n = len(s) 
        for i in range(n):
            print(stack) 
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)