from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        # Build graph
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # BFS function
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited = set()
            queue = deque([(start, 1.0)])

            while queue:
                node, product = queue.popleft()

                if node == end:
                    return product

                visited.add(node)

                for neighbor, value in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))

            return -1.0

        # Solve queries
        result = []

        for c, d in queries:
            result.append(bfs(c, d))

        return result