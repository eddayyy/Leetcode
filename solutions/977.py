from collections import deque 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        if n == 0:
            return []

        
        result = [0] * n 
        front = 0
        back = n - 1
        reverseIter = n - 1

        while front <= back and reverseIter >= 0:
            if abs(nums[front]) > abs(nums[back]): 
                result[reverseIter] = pow(nums[front], 2)
                front += 1
            
            else: 
                result[reverseIter] = pow(nums[back], 2) 
                back -= 1
            reverseIter -= 1

        return result 