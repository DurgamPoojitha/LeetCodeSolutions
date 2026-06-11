from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n = len(edges) + 1

        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to find maximum depth from root 1
        q = deque([(1, 0)])
        visited = {1}
        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, depth + 1))

        # Number of odd-sum assignments
        return pow(2, max_depth - 1, MOD)