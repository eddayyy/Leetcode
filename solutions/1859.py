class Solution:
    def sortSentence(self, s: str) -> str:
        # Get the words into a list for easier iteration
        words = s.split()
        # New list for us to put the words in order 
        sortedSentence = [0] * len(words)

        # iterate through sentence
        for word in words:
            # Get the number in each word and subtract 1 to make it 0-indexed
            # Set that index to the word excluding the number 
            sortedSentence[int(word[-1]) -1] = word[:-1]
        
        # Return the list of our sorted sentence 
        return " ".join(sortedSentence)