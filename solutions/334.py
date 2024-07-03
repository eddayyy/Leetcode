class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums) 
        if n < 3: 
            return False
        first_num, second_num = float('inf'), float('inf')
        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num 
            else:
                return True
        
        return False