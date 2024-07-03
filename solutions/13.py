class Solution:
    def romanToInt(self, s: str) -> int:
        total, i, n = 0, 0, len(s)
        numerals = {
            "I": 1,
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100,
            "D": 500, 
            "M": 1000, 
        }

        while i < n:
            if i + 1 < n and numerals[s[i]] < numerals[s[i+1]]:
                total += numerals[s[i+1]] - numerals[s[i]]
                i += 2 
            else: 
                total += numerals[s[i]] 
                i += 1 

        return total 