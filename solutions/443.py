class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars) 
        if n == 0: 
            return 0 
        elif n == 1:
            return 1
        
        i, counter = 0, 0,

        while i < n:
            groupLen = 1
            while i + groupLen < n and chars[i] == chars[ i + groupLen ]:
                groupLen += 1 
            chars[counter] = chars[i] 
            counter += 1 
            if groupLen > 1:  
                groupLenStr = str(groupLen)
                chars[counter:counter+len(groupLenStr)] = list(groupLenStr)
                counter += len(str(groupLen))
            i += groupLen
        
        return counter
            