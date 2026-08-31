class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reachable_index = 0

        for i,value in enumerate(nums):

            if i>max_reachable_index:
                return False

            max_reachable_index = max(max_reachable_index,i+value)

        return True