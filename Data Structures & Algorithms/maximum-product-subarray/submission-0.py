class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0

        global_max = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1,len(nums)):

            num = nums[i]

            temp_max = max(num,curr_max*num,curr_min*num)
            curr_min = min(num,curr_max*num,curr_min*num)
            curr_max = temp_max

            global_max = max(global_max,curr_max)

        return global_max
        