class Solution:
    def reverse(self, x: int) -> int:
        
        max_int = 2147483647

        sign = -1 if x<0 else 1
        x = abs(x)
        res = 0

        while x>0:
            pop = x%10
            x = x//10

            if res>max_int//10 or (res==max_int//10 and pop>7):
                return 0
            
            res = (res*10)+pop

        return res*sign