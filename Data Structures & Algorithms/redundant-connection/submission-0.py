class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #Union-Find (Disjoint Set Union) algorithm.

        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(node):
            root = node
            
            while root!=parent[root]:
                parent[root] = parent[parent[root]]
                root = parent[root]

            return root

        def union(n1,n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1==root2:
                return False

            if rank[root1]>rank[root2]:
                parent[root2]=root1
                rank[root1]+=root2
            else:
                parent[root1]=root2
                rank[root2]=root1

            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]