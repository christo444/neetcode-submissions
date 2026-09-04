class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []

        def backtrack(index,path,curr_sum):

            if curr_sum == target:
                result.append(path.copy())
                return

            for i in range(index,len(candidates)):

                if i > index and candidates[i]==candidates[i-1]:
                    continue

                if curr_sum > target:
                    break

                path.append(candidates[i])

                backtrack(i+1,path,curr_sum+candidates[i])

                path.pop()

        backtrack(0,[],0)
        return result