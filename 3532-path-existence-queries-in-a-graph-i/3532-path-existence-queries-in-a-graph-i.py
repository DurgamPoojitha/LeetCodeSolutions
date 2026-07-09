from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # Component ID for each node
        component = [0] * n
        comp_id = 0

        # Assign components
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp_id += 1
            component[i] = comp_id

        # Answer queries
        answer = []
        for u, v in queries:
            answer.append(component[u] == component[v])

        return answer