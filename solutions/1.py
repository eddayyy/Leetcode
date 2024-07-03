class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) 
        if n < 2: 
            return []
        
        collection = {} 
        for i, num in enumerate(nums): 
            compliment = target - num 
            if compliment in collection: 
                return [collection[compliment], i]
            else:
                collection[num] = i
        
        return [] 