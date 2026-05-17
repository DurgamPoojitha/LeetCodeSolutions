class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, path):
            # If target becomes 0, store the combination
            if target == 0:
                result.append(path[:])
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                # If candidate exceeds target, skip
                if candidates[i] > target:
                    continue

                # Include current candidate
                path.append(candidates[i])

                # Reuse same element, so pass i again
                backtrack(i, target - candidates[i], path)

                # Backtrack
                path.pop()

        backtrack(0, target, [])
        return result