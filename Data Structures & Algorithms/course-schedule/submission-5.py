class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) < 1:
            return True
        
        graph = {}

        for pair in prerequisites:

            curr = pair[0]
            pre = pair[1]

            if curr not in graph:
                graph[curr] = []

            graph[curr].append(pre)
        
        visited = set()
        taken = set()

        visiting = set()
        done = set()

        def dfs(course):
            if course in done:
                return True
            
            if course not in graph:
                return True
                
            if course in visiting:
                return False

            visiting.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            done.add(course)
            return True

        for course in range(numCourses):

            if dfs(course) == False:
                return False

        return True
