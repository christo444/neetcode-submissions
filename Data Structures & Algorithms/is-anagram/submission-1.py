class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 = {}
        for i in s:
            if i not in hash_1:
                hash_1[i]=1
            else:
                hash_1[i]+=1
        hash_2 = {}
        for i in t:
            if i not in hash_2:
                hash_2[i]=1
            else:
                hash_2 [i]+=1
        if hash_1==hash_2:
            return True
        return False       