# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0 

        counter = 0
        def dfs(root, maxValue):
            nonlocal counter
            if not root: return 0 
            
            if root.val >= maxValue: 
                maxValue = max(root.val, maxValue) 
                counter += 1 

            dfs(root.left, maxValue)
            dfs(root.right, maxValue)
            return counter 
        
        return dfs(root, root.val)        