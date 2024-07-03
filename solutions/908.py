from collections import defaultdict
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        smol = min(nums)
        big = max(nums)
        return (big-k) - (smol+k) if (big-k) - (smol+k) > 0 else 0 