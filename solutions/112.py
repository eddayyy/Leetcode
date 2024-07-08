# Title: Path Sum 
# Category: Binary Tree
# Difficulty: Easy 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], currentSum: int) -> bool: 
            if not node: return False

            currentSum -= node.val

            if not node.left and not node.right: 
                return currentSum == 0 
            
            return dfs(node.left, currentSum) or dfs(node.right, currentSum) 
        return dfs(root, targetSum)