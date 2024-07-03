class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s) 
        vowels = set(['a','e','i','o','u'])
        # Edge Cases: 
        if  n == 0:
            return 0 
        elif n == 1:
            if s[0] in vowels:
                return 1 

        # Implementation 
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)

        answer = count 

        for i in range(k, n):
            count += int(s[i] in vowels) - int(s[i-k] in vowels) 
            answer = max(answer, count)
            
        return answer 