class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += (i+"~")
        return string

    def decode(self, s: str) -> List[str]:
        string = ""
        l=[]
        for i in s:
            if i=="~":
                l.append(string)
                string=""
            else:
                string+=i
        return l



