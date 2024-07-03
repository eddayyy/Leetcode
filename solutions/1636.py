class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numsFrequency = Counter(nums)
        return sorted(nums, key=lambda x: (-numsFrequency[x], x), reverse=True)