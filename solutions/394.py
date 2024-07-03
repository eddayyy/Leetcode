class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return '' 
        
        stack, decoded, k, base = [], '', 0, 1 
        for char in s:
            if char == ']':
                decoded = '' 
                while stack[-1] != '[':
                    decoded += stack.pop() 
                # Pop the opening bracket 
                stack.pop() 
                k, base = 0, 1
                while len(stack) > 0 and stack[-1].isdigit(): 
                    k += int(stack.pop()) * base 
                    base *= 10 
                while k != 0: 
                    for i in range(len(decoded) - 1, -1, -1): 
                        stack.append(decoded[i])
                    k -= 1
            else:
                stack.append(char) 
        
        return ''.join(stack)