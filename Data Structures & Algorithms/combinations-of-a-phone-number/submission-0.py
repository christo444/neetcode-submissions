class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        result = []

        keypad = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }

        def backtrack(start_index,curr_string):

            if start_index==len(digits):
                result.append(curr_string)
                return

            curr_digit = digits[start_index]
            curr_letters = keypad[int(curr_digit)]

            for letter in curr_letters:
                backtrack(start_index+1,curr_string+letter)

        backtrack(0,"")

        return result
        