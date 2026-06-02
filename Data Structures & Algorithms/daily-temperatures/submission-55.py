class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures): 
            if not stack: 
                stack.append((index, temp))
                continue
            if stack[-1][1] >= temp:
                stack.append((index, temp))
            else: 
                while stack:
                    if stack[-1][1] >= temp:
                        break
                    else: 
                        popped = stack.pop()
                        res[popped[0]] = index - popped[0]
                stack.append((index, temp))
        return res


            

        