class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def backtrack(index,current_path):

            if index == len(nums):
                result.append(current_path.copy())
                return

            current_path.append(nums[index])

            backtrack(index+1,current_path)

            current_path.pop()

            backtrack(index+1,current_path)

        backtrack(0,[])
        return result