from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = Counter(nums)

        count_list = [[] for _ in range(len(nums)+1)]

        for letter,count in hash_map.items():
            count_list[count].append(letter)

        result = []

        for i in range(len(count_list)-1,0,-1):
            for j in count_list[i]:
                result.append(j)
                if len(result)==k:
                    return result