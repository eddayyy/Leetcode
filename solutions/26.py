class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      if len(nums) == 0: return 0 
      if len(nums) == 1: return 1 
      l, n = 0, len(nums)

      for r in range(1, n): 
        if nums[l] != nums[r]:
          l += 1 
          nums[l] = nums[r]
    
      print(nums[0:l+1])
      return l + 1 