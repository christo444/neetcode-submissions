from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_map = defaultdict(list)
        for string in strs:
            s = [0]*26
            for i in string:
                s[ord(i)-ord('a')]+=1
            hash_map[tuple(s)].append(string)
        for i in hash_map:
            result.append(hash_map[i])

        return result


        