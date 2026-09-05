class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []
        
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r,c,visited_set,prev_height):

            if (r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visited_set
                or heights[r][c] < prev_height):
                return
            
            visited_set.add((r,c))

            dfs(r+1,c,visited_set,heights[r][c])
            dfs(r-1,c,visited_set,heights[r][c])
            dfs(r,c+1,visited_set,heights[r][c])
            dfs(r,c-1,visited_set,heights[r][c])

        for c in range(COLS):

            dfs(0,c,pacific_reachable,heights[0][c])
            dfs(ROWS-1,c,atlantic_reachable,heights[ROWS-1][c])

        for r in range(ROWS):

            dfs(r,0,pacific_reachable,heights[r][0])
            dfs(r,COLS-1,atlantic_reachable,heights[r][COLS-1])

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_reachable and (r,c) in atlantic_reachable:
                    result.append((r,c))

        return result

        