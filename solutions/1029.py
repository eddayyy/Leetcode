class Solution:
  def sortCities(self, x0: int, x1: int) -> int:
    return x0 - x1 

  def twoCitySchedCost(self, costs: List[List[int]]) -> int:
      if not costs: return 0 
      
      costs.sort(key=lambda x: x[0] - x[1])
      total, n = 0, len(costs) // 2

      for i in range(n): 
          total += costs[i][0] + costs[i+n][1]
      return total 