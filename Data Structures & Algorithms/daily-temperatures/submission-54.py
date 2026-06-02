class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures): 
            if not stack: 
                stack.append((index, temp))
                continue
            top = stack[-1][1]
            if top >= temp:
                stack.append((index, temp))
            else: 
                while stack:
                    if stack[-1][1] >= temp:
                        break
                    else: 
                        popped = stack.pop()
                        top = popped[1]
                        ind = popped[0]
                        res[popped[0]] = index - ind
                stack.append((index, temp))
        return res


            

        