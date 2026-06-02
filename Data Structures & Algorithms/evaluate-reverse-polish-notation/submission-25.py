class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens: 
            if not stack: 
                stack.append(int(t))
            elif t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else: 
                stack.append(int(t))
        return int(stack.pop())
        