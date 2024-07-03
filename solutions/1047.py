class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s: return '' 

        stack = [] 
        for char in s: 
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)