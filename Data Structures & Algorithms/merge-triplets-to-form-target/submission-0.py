class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a_found = False
        b_found = False
        c_found = False
        
        for i in triplets:

            if i[0] > target[0] or i[1]>target[1] or i[2]>target[2]:
                continue

            if i[0] == target[0]:
                a_found = True
            if i[1] == target[1]:
                b_found = True
            if i[2] == target[2]:
                c_found = True

        return True if a_found and b_found and c_found else False