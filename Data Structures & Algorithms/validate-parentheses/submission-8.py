class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictkey = {"]" : "[",  "}":"{",  ")":"("}
        if len(s) % 2 != 0:
            return False
        else: 
            for i in s:
                if i in dictkey:
                    if stack: 
                        if stack[-1] == dictkey[i]:
                            stack.pop()
                        else: 
                            return False
                    else: 
                        return False
                else: 
                    stack.append(i)
            return True if not stack else False
