class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        brackets = {'(' : ')', '[' : ']', '{' : '}'}
        for bracket in s:
            # Check if we encountered an opening bracket 
            if bracket in brackets.keys(): 
                stack.append(bracket)
            # Else we encountered a closing bracket
            else: 
                # Check if the bracket at the top of the stack is the same bracket 
                if stack and brackets[stack[-1]] == bracket:
                    # Pop the opening bracket off the stack
                    stack.pop()
                else:
                    # Otherwise we have an invalid order 
                    return False
        
        return len(stack) == 0 