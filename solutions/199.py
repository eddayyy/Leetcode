from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None 
        
        q = deque([root])
        result = []

        while q: 
            rightSide = None 
            qLen = len(q) 
            for i in range(qLen):
                node = q.popleft() 
                if node:
                    if node.left: 
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    rightSide = node
            if rightSide:
                result.append(rightSide.val)

        return result 
        