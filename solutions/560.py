class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCollection = {0:1}
        prefix = total = 0 
        
        for num in nums:
            prefix += num 
            diff = prefix - k 

            total += prefixCollection.get(diff, 0) 
            prefixCollection[prefix] = 1 + prefixCollection.get(prefix, 0)  

        return total 