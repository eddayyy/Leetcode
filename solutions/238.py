class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        if n == 0: 
            return [] 
        elif n == 1:
            return [] 
        
        result = [1] * n 
        left, right = 1, 1

        for i in range(n):
            result[i] = left
            left *= nums[i]

        for i in range(n -1, -1, -1): 
            result[i] *= right
            right *= nums[i] 

        return result 

