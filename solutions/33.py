class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1 
        left, right = 0, len(nums) - 1 
        
#       nums = [4,5,6,7,0,1,2], target = 0

        while left <= right: 
            mid = left + (right - left) // 2

            if nums[mid] == target: return mid 
            
            # Left Sorted Portion of Array
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1 

            # Right Sorted Portion of Array 
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else: 
                    left = mid + 1 
               
        return -1