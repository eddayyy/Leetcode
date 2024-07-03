class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]: 
          def kSum(start, target, k):
              if k != 2:
                  for i in range(start, n - k + 1):
                      if i > start and nums[i] == nums[i - 1]:
                          continue
                      quad.append(nums[i])
                      kSum(i + 1, target - nums[i], k - 1)
                      quad.pop()
                  return
                  pass
              else:
                  left, right = start, n - 1
                  while left < right: 
                      curr = nums[right] + nums[left] 
                      if curr == target:
                          res.append(quad + [nums[right], nums[left]])
                          left += 1 
                          while left < right and nums[left] == nums[left - 1]:
                              left += 1 
                      elif curr > target:
                          right -= 1 
                      elif curr < target:
                          left += 1 
          nums.sort()
          res, quad, n = [], [], len(nums)
          kSum(0, target, 4) 
          return res 