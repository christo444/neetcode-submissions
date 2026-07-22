class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_count=0
        for i in hash_set:
            if i-1 in hash_set:
                continue
            else:
                curr_num=i
                count=1
                while curr_num+1 in hash_set:
                    count+=1
                    curr_num+=1
                max_count = max(count,max_count)
        return max_count