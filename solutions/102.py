from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [] 
        result, q = [], deque([root])

        while q:
            level_length = len(q)
            level_nodes = [] 
            for _ in range(level_length):
                node = q.pop()
                level_nodes.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            result.append(level_nodes)
        
        return result 