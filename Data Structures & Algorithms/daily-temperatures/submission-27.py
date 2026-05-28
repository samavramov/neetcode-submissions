class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures): 
            if not stack: 
                stack.append([i, t])
            else:
                    while stack and stack[-1][1] < t: 
                        popped = stack.pop()
                        distance = i - popped[0]
                        result[popped[0]]=distance
                    stack.append([i, t])
        return result



