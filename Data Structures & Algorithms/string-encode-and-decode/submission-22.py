class Solution:
    def encode(self, strs: List[str]) -> str:
        sendstring = ""
        for s in strs: 
            sendstring += str(len(s))+"#"+s
        print (sendstring)
        return sendstring
    def decode(self, s: str) -> List[str]:
        lis = []
        length = ""
        i = 0
        while i < len(s):
            if(s[i]!= '#'):
                length += s[i]
                i += 1
            else: 
                intlen = int(length)
                lis.append(s[i+1:i+1+intlen])
                length = ""
                i += intlen+1

        return lis
