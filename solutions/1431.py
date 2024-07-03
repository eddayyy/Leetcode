class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      n = len(candies)
      if n == 0: return False 

      maxCandies, result = max(candies), [] 

      for i in range(n): 
        result.append(candies[i] + extraCandies >= maxCandies)
      return result 