from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if a common divisor string exists
        if str1 + str2 != str2 + str1:
            return ""

        # Find GCD of lengths
        length = gcd(len(str1), len(str2))

        # Return the common substring
        return str1[:length]