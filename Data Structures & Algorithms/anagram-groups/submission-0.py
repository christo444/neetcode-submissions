class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finder = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for s in i:
                count[ord(s)-ord("a")]+=1
            finder[tuple(count)].append(i)
        return list(finder.values())

            