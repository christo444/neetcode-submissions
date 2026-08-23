class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in {"+","-","*","/"}:
                stack.append(int(i))

            else:
                right_operand = stack.pop()
                left_operand = stack.pop()

                if i=="+":
                    stack.append(left_operand+right_operand)
                elif i=="-":
                    stack.append(left_operand-right_operand)
                elif i=="*":
                    stack.append(left_operand*right_operand)
                else:
                    stack.append(int(left_operand/right_operand))

        return stack.pop()
            
