from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #graph theory , if it is a directed acyclic graph then possible but if there is
        #a cycle then not possible.
        #uses topological sorting

        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for dest,src in prerequisites:
            adj[src].append(dest)
            indegree[dest]+=1

        queue = deque(i for i in range(numCourses) if indegree[i]==0)
        completed = 0

        while queue:
            curr = queue.popleft()
            completed+=1

            for neighbour in adj[curr]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)

        return completed==numCourses