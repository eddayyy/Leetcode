class Solution:
  def expandSubstr(self, l, r, s):
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1 
      r += 1
    return s[l+1:r]

  def longestPalindrome(self, s: str) -> str:

    result = "" 
    n = len(s)
    
    for i in range(n):
        subStr1 = self.expandSubstr(i, i, s) 
        if len(subStr1) > len(result):
          result = subStr1

        subStr2 = self.expandSubstr(i, i+1, s) 
        if len(subStr2) > len(result):
          result = subStr2
    
    return result
