# Binary Search
# Time O(logn) | Space O(1) 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m
        return 0 

# Brute Force (Linear Time)
# Time O(n) | Space O(1) 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return 0 
        if len(nums) == 1: return 0 

        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] > nums[i + 1] and i == 0:
                return i
            if 0 < i + 1 < len(nums) and i - 1 >= 0:
                if nums[i] > nums[i - 1] and nums[i] > nums [i + 1]:
                    return i 
            elif i + 1 == len(nums) and i - 1 >= 0 and nums[i] > nums[i - 1]:
                return i 
        return 0 