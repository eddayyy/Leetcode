class Solution:
    def dfs(self, root, left, right): 
        if not left and not right: return True 
        if not left or not right: return False

        return (left.val == right.val and self.dfs(root, left.left, right.right) and self.dfs(root, left.right, right.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, root.left, root.right)