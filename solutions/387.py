from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = collections.Counter(s) 

        for idx, char in enumerate(s): 
            if hashmap[char] == 1: 
                return idx

        return -1 