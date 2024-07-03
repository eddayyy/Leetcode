class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        if n == 0: return

        slow = 0 
        # Test Case: 
        # [0,1,0,3,12]
        for fast in range(n):
            print(f'Fast and slow index: {fast} , {slow}\n Fast and slow values: {nums[fast]} , {nums[slow]}')
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow] 
            
            if nums[slow] != 0:
                slow += 1 

        return 