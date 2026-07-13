class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=="(":
                l.append(i)
            elif i=="[":
                l.append(i)
            elif i=="{":
                l.append(i)
            elif i==")":
                if len(l)==0:
                    return False
                s=l.pop()
                if s!="(":
                    return False
                else:
                    continue
            elif i=="]":
                if len(l)==0:
                    return False
                s=l.pop()
                if s!="[":
                    return False
                else:
                    continue
            elif i=="}":
                if len(l)==0:
                    return False
                s=l.pop()
                if s!="{":
                    return False
                else:
                    continue
        if len(l)==0:
            return True
        else:
            return False

        