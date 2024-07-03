class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1) 
        count2 = Counter(word2) 
        n1 = Counter([v for v in count1.values()])
        n2 = Counter([v for v in count2.values()])
        return n1 == n2 and set(word1) == set(word2)