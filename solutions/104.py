class Solution:
    def dfs(self, node):
        if node == None: 
            return 0 
        left = self.dfs(node.left) 
        right = self.dfs(node.right)

        return max(left, right) + 1 

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root) 