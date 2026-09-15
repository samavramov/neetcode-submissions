from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        queue = deque()
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course]+=1
        for course, degree in enumerate(indeg):
            if degree == 0:
                queue.append(course)
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for nextcourse in graph[course]:
                indeg[nextcourse] -= 1
                if indeg[nextcourse] == 0:
                    queue.append(nextcourse)
        return completed == numCourses

