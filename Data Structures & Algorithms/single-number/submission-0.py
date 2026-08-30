class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #we have to do the XOR operation here
        #in XOR operation if a ^ a = 0 , a ^ 0 = a

        result = 0
        for i in nums:
            result^=i

        return result