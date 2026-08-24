class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        COLS=len(matrix[0])
        ROWS=len(matrix)
        r = ROWS * COLS -1

        while l<=r:

            mid = (l+r)//2
            row = mid // COLS
            cols = mid % COLS

            if matrix[row][cols]==target:
                return True

            elif matrix[row][cols]>target:
                r=mid-1

            else:
                l=mid+1

        return False