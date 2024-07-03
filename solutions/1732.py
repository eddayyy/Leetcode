class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain) 
        if n == 0: 
            return 0  
            
        maxAltitude, curr = 0, 0
        
        for altitude in gain:
            curr += altitude
            maxAltitude = max(maxAltitude, curr) 
        
        return maxAltitude
