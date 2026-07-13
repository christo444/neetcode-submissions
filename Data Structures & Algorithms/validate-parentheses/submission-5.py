class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                stack.append(i)
            elif i==")":
                if stack==[]:
                    return False
                else:
                    temp=stack.pop()
                    if temp=="(":
                        continue
                    else:
                        return False
            elif i=="}":
                if stack==[]:
                    return False
                else:
                    temp=stack.pop()
                    if temp=="{":
                        continue
                    else:
                        return False
            elif i=="]":
                if stack==[]:
                    return False
                else:
                    temp=stack.pop()
                    if temp=="[":
                        continue
                    else:
                        return False
        if stack==[]:
            return True
        else:
            return False
        