class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            lst2=nums.copy()
            lst2.remove(i)
            p=1
            for j in lst2:
                p*=j
            l.append(p)
        return l

            
        