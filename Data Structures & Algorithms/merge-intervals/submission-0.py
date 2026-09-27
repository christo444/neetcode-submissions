class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals)<=1:
            return intervals

        intervals.sort(key=lambda x:x[0])

        merged = [intervals[0]]

        for curr in intervals[1:]:

            last_merged = merged[-1]

            if curr[0]<=last_merged[1]:
                last_merged[1] = max(last_merged[1],curr[1])

            else:
                merged.append(curr)

        return merged
