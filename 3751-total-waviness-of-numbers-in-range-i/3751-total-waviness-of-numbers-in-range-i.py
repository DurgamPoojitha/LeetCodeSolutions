class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num):
            s = str(num)
            if len(s) < 3:
                return 0

            count = 0
            for i in range(1, len(s) - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    count += 1  # Peak
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    count += 1  # Valley
            return count

        total = 0
        for num in range(num1, num2 + 1):
            total += waviness(num)

        return total