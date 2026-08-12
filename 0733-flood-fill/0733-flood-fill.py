from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original = image[sr][sc]
        if original == color:
            return image
        rows = len(image)
        cols = len(image[0])
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # Check boundaries and original color
                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == original:
                        image[nr][nc] = color
                        queue.append((nr, nc))
        return image
        