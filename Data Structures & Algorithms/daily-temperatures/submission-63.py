class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][1]:
                oldind, oldtemp = stack.pop()
                res[oldind] = index - oldind
            stack.append((index, temp))
        return res


            

        