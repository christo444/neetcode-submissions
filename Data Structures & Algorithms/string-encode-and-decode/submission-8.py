class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for i in strs:
            enc_str+=str(len(i))+"#"+i
        return enc_str

    def decode(self, s: str) -> List[str]:
        i=0
        l=[]
        while i<len(s):
            temp_str=""
            num_str=""
            while s[i]!="#":
                num_str+=s[i]
                i+=1
            length=int(num_str)
            i+=1
            temp_str = s[i:(i+length)]
            i=(i+length)
            l.append(temp_str)
        return l
