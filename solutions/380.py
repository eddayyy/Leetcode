class RandomizedSet:

    def __init__(self):
        self.randomList = [] 
        self.randomMap = {} 

    def insert(self, val: int) -> bool:
        if val in self.randomMap:
            return False
        
        self.randomMap[val] = len(self.randomList)
        self.randomList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomMap: 
            idx, lastElement = self.randomMap[val], self.randomList[-1]
            self.randomList[idx], self.randomMap[lastElement] = lastElement, idx
            self.randomList.pop()
            del self.randomMap[val] 
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.randomList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()