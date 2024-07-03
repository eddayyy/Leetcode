class RecentCounter:

    def __init__(self):
        self.requests = deque() 

    def ping(self, t: int) -> int:
        self.requests.append(t) 
        
        boundary = t - 3000 
        while self.requests[0] < boundary: 
            self.requests.popleft()
        
        return len(self.requests)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)