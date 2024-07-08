# Title: Flatten Binary Tree to Linked List
# Category: Binary Tree
# Difficulty: Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_tree(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node: return None 

            left       = node.left
            right      = node.right  
            left_tail  = flatten_tree(left) 
            right_tail = flatten_tree(right)

            if left: 
                node.right = left
                node.left  = None 

                if left_tail: 
                    left_tail.right = right 
            return right_tail if right_tail else (left_tail if left_tail else node)
        
        flatten_tree(root)