class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(index,path,current_sum):

            if current_sum == target:
                result.append(path.copy())
                return

            if index == len(nums) or current_sum > target:
                return

            path.append(nums[index])

            backtrack(index,path,current_sum+nums[index])

            path.pop()

            backtrack(index+1,path,current_sum)

        backtrack(0,[],0)

        return result