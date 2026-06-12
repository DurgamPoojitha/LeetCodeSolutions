from collections import deque
from math import log2

MOD = 10**9 + 7

class Solution:
    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1

        # Build tree
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Binary Lifting Preprocessing
        LOG = (n).bit_length()
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    parent[0][nei] = node
                    q.append(nei)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:
            w = lca(u, v)

            # Number of edges in the path
            dist = depth[u] + depth[v] - 2 * depth[w]

            if dist == 0:
                ans.append(0)
            else:
                # Number of assignments with odd path cost = 2^(dist-1)
                ans.append(pow2[dist - 1])

        return ans