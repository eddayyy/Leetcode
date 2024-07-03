class OrderedStream:

    def __init__(self, n: int): 
        self.os = [None] * n
        self.marker = 0  

    def insert(self, idKey: int, value: str) -> List[str]:
        ID = idKey - 1 
        self.os[ID] = value
        if ID == self.marker: 
            while self.marker < len(self.os) and self.os[self.marker]:
                self.marker += 1 
            return self.os[ID:self.marker]
        return [] 
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)