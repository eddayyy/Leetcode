class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if not senate: return '' 

        r, d = deque(), deque() 

        senators = list(senate)
        
        for i in range(len(senate)):
            if senators[i] == 'D':
                d.append(i)
            elif senators[i] == 'R':
                r.append(i)
        
        while d and r: 
            dTurn = d.popleft()
            rTurn = r.popleft() 
            if rTurn < dTurn: 
                r.append(rTurn + len(senate))
            else:
                d.append(dTurn + len(senate))     

        return 'Radiant' if r else 'Dire'