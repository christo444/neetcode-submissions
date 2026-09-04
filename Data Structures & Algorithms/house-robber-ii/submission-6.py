class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        def robbing(arr):
            prev1 , prev2 = 0 , 0

            for money in arr:

                temp = max(money+prev2,prev1)
                prev2 = prev1
                prev1 = temp

            return temp

        return max(robbing(nums[:-1]),robbing(nums[1:]))