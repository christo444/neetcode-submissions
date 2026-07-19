class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        freq = [[] for i in range(len(nums)+1)]

        for n,i in d.items():
            freq[i].append(n)

        res=[]

        for i in range(len(nums),0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res

