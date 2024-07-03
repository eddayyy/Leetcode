class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms: return True

        stack = [0]
        seen = set(stack) 

        while stack:
            i = stack.pop()

            for key in rooms[i]:
                if key not in seen:
                    seen.add(key)
                    stack.append(key) 
        
        return len(seen) == len(rooms)
