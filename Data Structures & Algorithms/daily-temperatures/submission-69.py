class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if i == 0:
                stack.append((i,t))
                continue
            while stack and t > stack[-1][1]: 
                pos, val = stack.pop()
                output[pos] = i - pos
            stack.append((i,t))
        return output

        