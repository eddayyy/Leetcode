# Approach: 
#   - iterate through the string keep track of the vowels through a set  
#   - iterate through the string again and reverse the vowels 
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s) 
        if n == 0: 
            return '' 
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        s = list(s) 
        left, right = 0, n - 1
    
        while left < right:
            while left < right and s[left] not in vowels: 
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            if left < right: 
                s[left], s[right] = s[right], s[left]
                left += 1 
                right -= 1
    
        return "".join(s) 