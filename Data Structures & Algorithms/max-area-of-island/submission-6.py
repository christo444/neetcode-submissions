class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        max_count = 0

        def dfs(r,c):

            nonlocal area_count

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return
            
            grid[r][c]=0
            area_count+=1

            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area_count=0
                    dfs(r,c)
                    max_count=max(max_count,area_count)
        return max_count



        