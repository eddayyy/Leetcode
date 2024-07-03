# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafHelper(self, node, arr): 
        if node and not node.left and not node.right: 
            arr.append(node.val)
        if node.left: 
            self.leafHelper(node.left, arr)
        if node.right: 
            self.leafHelper(node.right, arr) 
        return arr
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        treeA = self.leafHelper(root1, [])
        treeB = self.leafHelper(root2, [])
        return treeA == treeB 