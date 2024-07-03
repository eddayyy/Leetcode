class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        sHashmap = defaultdict(int) 
        tHashmap = defaultdict(int) 

        for i in range(len(s)): 
            sHashmap[s[i]] += 1
            tHashmap[t[i]] += 1
        
        for k, val in sHashmap.items():
            if tHashmap.get(k) != val: 
                return False
        return True 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t) 
        return sorted_s == sorted_t