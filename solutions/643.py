class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums) 
        if n == 1 and n == k: 
            return nums[n-1] 
        elif n == 0: 
            return 0

        curr = maxSum = sum(nums[:k])

        for i in range(k, n): 
            curr += nums[i] - nums[i-k]
            maxSum = max(maxSum, curr)

        return maxSum / k  