class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        Input: 
            - an integer array 'nums'
        Output: 
            - integer 'answer' 
        '''

        n = len(nums)
        if n == 0:
            return 0 
        elif n == 1:
            if nums[0] == 1:
                return 1 
        
        left = 0
        for right in range(n):
            k -= 1 - nums[right]

            if k < 0:
                k += 1 - nums[left]
                left += 1 
            
        return right - left + 1