class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return nums 

        count = Counter(nums)
        print(count.items())
        return heapq.nlargest(k, count.keys(), key=count.get)