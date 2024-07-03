class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = Counter(chars) 
        res, same = 0, False 
        for word in words:
            wordDict = Counter(word)
            for char, freq in wordDict.items():
                if char in charsDict and charsDict[char] >= freq:
                    same = True
                    continue 
                same = False
                break
            res = res + len(word) if same else res 
        return res 
        