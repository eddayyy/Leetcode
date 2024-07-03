from sortedcontainers import SortedList
class MRUQueue:
    # O(n) Constructor 
    # O(logn) fetch | add and pop are logn operations for the sorted list 
    def __init__(self, n: int):
        self.queue = SortedList()
        self.size = n 
        for i in range(1, n+1,): 
            self.queue.add((i, i)) 

    def fetch(self, k: int) -> int:
        idx, val = self.queue.pop(k-1) 
        self.queue.add((self.size+1, val))
        self.size  += 1 
        return val 


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)