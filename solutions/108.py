class Solution:
    # Time: O(n) | Space: O(logn) 
    # Recursion height is O(logn) since that is the height of our tree thus it is that much space in the function call stack
    def helper (self, nums: List[int], l, r):
        if l > r: return None
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = self.helper(nums, l, m - 1)
        root.right = self.helper(nums, m + 1, r)
        return root


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)