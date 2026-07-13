class Solution:
    def isPalindrome(self, s: str) -> bool:
        dup = ""
        lo = s.lower()
        for i in lo:
            if i.isalnum():
                dup+=i
        rev = dup[::-1]
        return rev==dup
        
        