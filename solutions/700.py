class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val: return root 

        while root and root.val != val: 
            if root.val > val: 
                root = root.left 
            elif root.val < val: 
                root = root.right
        return root