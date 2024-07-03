# Solution 1:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [[]], [] 
        
        def backtrack(i): 
            if i >= len(nums): 
                res.append(subset.copy())
            
            subset.append(nums[i])
            backtrack(i + 1) 

            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return res

# Solution 2: 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        res = [[]] 
        for num in nums:
            res += [curr + [num] for curr in res]
        return res