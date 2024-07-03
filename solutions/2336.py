class SmallestInfiniteSet:

    def __init__(self):
        self.curr, self.minHeap, self.set = 1, [], set()  

    def popSmallest(self) -> int:
        if self.minHeap:
            smol = heapq.heappop(self.minHeap) 
            self.set.remove(smol)
            return smol
        temp = self.curr 
        self.curr += 1 
        return temp

    def addBack(self, num: int) -> None:
        if num not in self.set and num < self.curr:
            heapq.heappush(self.minHeap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)