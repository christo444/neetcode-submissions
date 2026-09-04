class Solution:
    def countSubstrings(self, s: str) -> int:

        tot_count = 0

        if not s or len(s)<2:
            tot_count+=1
            return tot_count


        def expand_around_center(left,right):
            count = 0
            while left >=0 and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
                count+=1
            return count
        
        for i in range(len(s)):

            tot_count+=expand_around_center(i,i)

            tot_count+=expand_around_center(i,i+1)
                

        return tot_count