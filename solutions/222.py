# Title: Count Complete Tree Nodes
# Category: Binary Tree
# Difficulty: Easy 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 
        left_count  = self.countNodes(root.left) 
        right_count = self.countNodes(root.right) 
        return 1 + left_count + right_count