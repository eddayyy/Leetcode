class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return max(self.dfs(root.left, True, 0), self.dfs(root.right, False, 0)) 

    def dfs(self, root, goLeft, depth):
        if not root: return depth 

        if goLeft: 
            depth = max(
                depth, 
                self.dfs(root.right, False, depth + 1),  
                self.dfs(root.left, True, 0) 
            )
    
        else: 
            depth = max(
                depth, 
                self.dfs(root.left, True, depth + 1),
                self.dfs(root.right, False, 0) 
            )
        return depth