class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1 

        s, f, n  = 0, len(needle) - 1, len(haystack) # The start and end of our needle 
        for i in range(n):
            if s in range(n) and f in range(n) and haystack[s:f+1] == needle:
                return s
            s += 1 
            f += 1 
        return -1 