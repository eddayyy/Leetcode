# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []

        def dfs(root):
            if not root: return None

            if len(elements) < k: 
                dfs(root.left)
                elements.append(root.val)
                dfs(root.right)

        dfs(root)
        return elements[k-1]