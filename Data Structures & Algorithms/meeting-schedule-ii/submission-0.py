"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0
        max_room = 0

        s_ptr = 0
        e_ptr = 0

        while s_ptr<len(intervals):

            if start[s_ptr]<end[e_ptr]:
                count+=1
                max_room = max(max_room,count)
                s_ptr+=1

            else:
                count-=1
                e_ptr+=1

        return max_room