class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0  # pointer for name
        j = 0  # pointer for typed

        while j < len(typed):
            # Characters match
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1

            # Long press case
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1

            # Invalid character
            else:
                return False

        # All characters in name should be matched
        return i == len(name)