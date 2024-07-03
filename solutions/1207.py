class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = len(arr) 
        if n == 0 or n == 1: 
            return True 
        
        ocurrences = defaultdict(int) 
        uniqueOcurrences = set() 

        for num in arr: 
            ocurrences[num] += 1 
        
        for k, v in ocurrences.items(): 
            uniqueOcurrences.add(v) 
        
        return len(uniqueOcurrences) == len(ocurrences)