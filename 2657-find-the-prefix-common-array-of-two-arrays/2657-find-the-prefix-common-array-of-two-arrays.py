class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        seenA = set()
        seenB = set()
        result = []

        for i in range(n):
            seenA.add(A[i])
            seenB.add(B[i])

            # Count common elements
            common_count = len(seenA & seenB)
            result.append(common_count)

        return result