from collections import deque

class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        visited = set()

        queue = deque([start])

        while queue:
            index = queue.popleft()

            # If reached value 0
            if arr[index] == 0:
                return True

            # Skip if visited index
            if index in visited:
                continue

            visited.add(index)

            # Forward jump
            forward = index + arr[index]

            # Backward jump
            backward = index - arr[index]

            if 0 <= forward < n:
                queue.append(forward)

            if 0 <= backward < n:
                queue.append(backward)

        return False