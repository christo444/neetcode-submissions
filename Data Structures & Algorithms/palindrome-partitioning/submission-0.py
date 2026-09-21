class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(left,right):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def backtrack(start_index,curr_path):

            if start_index>=len(s):
                result.append(curr_path.copy())
                return

            for i in range(start_index,len(s)):

                if is_palindrome(start_index,i):

                    curr_path.append(s[start_index:i+1])

                    backtrack(i+1,curr_path)

                    curr_path.pop()

        backtrack(0,[])
        return result

        