from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            vertices =1
            edge_count =len(graph[node])

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    v,e = dfs(neighbor)
                    vertices += v
                    edge_count += e

            return vertices,edge_count

        complete = 0

        for i in range(n):
            if not visited[i]:
                vertices,edge_count = dfs(i)

                actual_edges = edge_count // 2
                required_edges = vertices * (vertices - 1) // 2

                if actual_edges == required_edges:
                    complete += 1

        return complete