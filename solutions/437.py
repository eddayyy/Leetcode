# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        
        def dfs(root, prefix): 
            nonlocal result
            if not root: return 
            prefix += root.val
            diff = prefix - targetSum 
            
            if prefix == targetSum:
                result += 1 

            result += prefixSums[diff]
            prefixSums[prefix] += 1 
            
            dfs(root.left, prefix) 
            dfs(root.right, prefix) 

            prefixSums[prefix] -= 1 
        
        result = 0
        prefixSums = defaultdict(int)
        dfs(root, 0)
        return result