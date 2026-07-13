class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=float('inf')
        max_profit=0
        for i in prices:
            if i<lowest:
                lowest=i
            elif i-lowest > max_profit:
                max_profit = i-lowest
        return max_profit