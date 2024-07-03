class Solution:
    # Asymptotic Analysis: 
    # Time O(n)
    # Space O(1) 
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0 
        elif n == 1:
            return nums[0]

        # nums = [-2, -1]
        currSum = 0 
        maxSum = nums[0] 
        
        for i in range(n): 
            currSum = max(0, currSum) + nums[i] 
            maxSum = max(maxSum, currSum)
        
        return maxSum