class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums) 

        if n == 0: 
            return 0

        collection = defaultdict() 
        operations = 0
        
        for num in nums: 
            complement = k - num

            if num in collection: 
                collection.pop(num) 
                operations += 1 
            else: 
                collection[complement] = 1

        return operations 