class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0 

        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)): 
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        stack, visited = [], set()  
        provinceCount = 0
        for start in range(len(isConnected)): 
            if start not in visited:
                provinceCount += 1 
                dfs(start)
        return provinceCount