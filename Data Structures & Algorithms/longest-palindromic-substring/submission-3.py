class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s or len(s)<2:
            return s

        longest = ""

        def expand_around_center(left,right):

            while left >=0 and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        for i in range(len(s)):

            odd_pal = expand_around_center(i,i)

            even_pal = expand_around_center(i,i+1)

            if len(odd_pal)>len(longest):
                longest = odd_pal

            if len(even_pal)>len(longest):
                longest = even_pal

        return longest