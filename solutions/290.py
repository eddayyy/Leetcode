# Title: Word Pattern 
# Category: Hashmap
# Difficulty: Easy 

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() 

        if len(pattern) != len(words): return False 

        char_to_word = {}

        for char, word in zip(pattern, words): 
            if char in char_to_word: 
                if char_to_word[char] != word:
                    return False
            else:
                if word in char_to_word.values():
                    return False 
                char_to_word[char] = word
            
        return True
