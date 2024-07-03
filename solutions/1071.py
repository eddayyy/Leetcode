class Solution:
  def gcdOfStrings(self, str1, str2):
      def check(s, pattern):
          return s == pattern * (len(s) // len(pattern))
      
      gcd_length = math.gcd(len(str1), len(str2))
      
      candidate = str1[:gcd_length]
      
      if check(str1, candidate) and check(str2, candidate):
          return candidate
      else:
          return ""