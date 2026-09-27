class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals)<=1:
            return 0

        intervals.sort(key=lambda x:x[0])

        removed = 0
        prev_end = intervals[0][1]

        for i in range(1,len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if curr_start<prev_end:
                removed+=1
                prev_end = min(prev_end,curr_end)

            else:
                prev_end = curr_end

        return removed