class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        sort=[[] for i in range(len(nums)+1)]
        for key,value in count.items():
            sort[value].append(key)
        result=[]
        for i in range(len(sort)-1,0,-1):
            for j in sort[i]:
                result.append(j)
                if len(result)==k:
                    return result