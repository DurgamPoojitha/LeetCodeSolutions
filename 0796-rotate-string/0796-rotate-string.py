class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # Lengths must be equal
        if len(s) != len(goal):
            return False

        # goal must be a substring of s+s
        return goal in (s + s)