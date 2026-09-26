class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        visited=set()

        def dfs(node):
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        for i in range(n):
            if i not in visited:
                count+=1
                visited.add(i)
                dfs(i)

        return count