class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                popped = stack.pop()
                result[popped[0]] = i - popped[0]
            stack.append([i, t])
        return result
