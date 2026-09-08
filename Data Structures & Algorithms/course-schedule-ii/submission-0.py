class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for dest,src in prerequisites:
            adj[src].append(dest)
            indegree[dest]+=1

        queue = deque(i for i in range(numCourses) if indegree[i]==0)
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbour in adj[curr]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)

        if len(result)==numCourses:
            return result
        else:
            return []