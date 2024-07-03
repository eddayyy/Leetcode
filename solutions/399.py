from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (a, b) in enumerate(equations): 
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]]) 
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1 
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w 
                
                for neighbor, weight in adj[n]:
                    if neighbor not in visit:
                        q.append([neighbor, w * weight])
                        visit.add(neighbor) 


            return -1 

        return [bfs(q[0], q[1]) for q in queries]