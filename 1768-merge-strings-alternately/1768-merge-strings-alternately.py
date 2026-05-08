class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        j = 0

        # Add characters alternately
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters
        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)