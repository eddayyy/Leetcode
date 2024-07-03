class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q, result, startLeft = deque([root]), [], True
        while q:
            level_nodes = deque() 
            for _ in range(len(q)):
                node = q.pop()
                if startLeft:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            result.append(level_nodes)
            startLeft = not startLeft
        return result 
