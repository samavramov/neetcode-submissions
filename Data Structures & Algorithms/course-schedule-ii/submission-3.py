from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        queue = deque()
        ans = []
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course] += 1
        for course, deg in enumerate(indeg):
            if deg == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            ans.append(course)
            for nextCourse in graph[course]:
                indeg[nextCourse] -= 1
                if indeg[nextCourse] == 0:
                    queue.append(nextCourse)
        if len(ans) == numCourses:
            return ans
        else:
            return []
        




        