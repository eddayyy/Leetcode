class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph: return [[]]
        res, target = [], len(graph) - 1
        
        def dfs(vertex, path): 
            if vertex == target:
                res.append(list(path))
                return 
            
            for vertices in graph[vertex]:
                path.append(vertices)
                dfs(vertices, path)
                path.pop()
        
        path = [0]
        dfs(0, path) 
        return res