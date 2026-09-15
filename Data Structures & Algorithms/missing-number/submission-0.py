class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #other way-> take sum of natural number from 0 to n and take sum of nums array and then subtract.
        
        result = len(nums)

        for i in range(len(nums)):
            result^=i^nums[i]

        return result