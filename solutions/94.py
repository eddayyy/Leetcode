class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return [] 

        def dfs(node):
            if not node: return None 

            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)
        
        res = [] 
        dfs(root)
        return res 