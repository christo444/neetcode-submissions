class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #a valid tree must contain n nodes and n-1 edges.If there are less than n-1 edges then it is disconnected
        #if there are more than n-1 edges then it has  a cycle

        if len(edges)!=n-1:
            return False

        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        queue = [0]
        visited.add(0)

        while queue:

            current_node = queue.pop(0)
            
            for neighbour in adj[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return len(visited)==n