class Solution:
    def climbStairs(self, n: int) -> int:
        
        #we use a fibonacci approach here
        #for the first and second steps we just return the n
        #for the third step onward we take the sum of the two steps backwards

        if n<=2:
            return n

        one_back = 1
        two_back = 2

        for _ in range(3,n+1):
            current = one_back+two_back
            one_back = two_back
            two_back = current

        return current