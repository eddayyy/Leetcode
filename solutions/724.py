class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) 

        leftSum, rightSum = 0, sum(nums) 

        for i, num in enumerate(nums): 
            if leftSum == rightSum - leftSum - num: 
                return i 
            leftSum += num 
        return -1 