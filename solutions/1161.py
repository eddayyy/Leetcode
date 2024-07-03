# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
         
        levelSums, q = {}, deque([root])
        level, levelSum = 0, 0  
        maxSum = float('-inf')
        maxLevel = 0

        while q:
            levelSum = 0 
            level += 1             
            qLen = len(q) 

            for i in range(qLen): 
                node = q.popleft() 

                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    levelSum += node.val

            maxLevel = level if levelSum > maxSum else maxLevel
            maxSum = max(maxSum, levelSum) 

        return maxLevel


class Solution:
    def dfs(self, node: Optional[TreeNode], level: int, levelSums: List[int]) -> None: 
        if not node: return None 

        if len(levelSums) == level:
            levelSums.append(node.val)
        else: 
            levelSums[level] += node.val

        self.dfs(node.left, level + 1, levelSums) 
        self.dfs(node.right, level + 1, levelSums)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        levelSums = [] 
        self.dfs(root, 0, levelSums) 
        
        return 1 + levelSums.index(max(levelSums))