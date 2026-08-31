class Solution:
    def rob(self, nums: List[int]) -> int:

        #on reaching each house we can take a decision either to rob it and add with the
        #i-2 house or keep the cash of i-1 house

        prev1 = 0
        prev2 = 0

        for i in nums:

            current = max(prev1,prev2+i)

            prev2=prev1
            prev1=current

        return current