class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if not nums: return 0 

        posNums, negNums = 0, 0 

        for num in nums: 
            if num > 0: 
                posNums += 1 
            elif num < 0:
                negNums += 1 
        return max(posNums, negNums)