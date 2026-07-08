from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries):
        MOD = 10**9 + 7

        positions = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                positions.append(i)
                digits.append(int(ch))

        n = len(digits)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        hash_val = [0] * (n + 1)
        for i in range(n):
            hash_val[i + 1] = (hash_val[i] * 10 + digits[i]) % MOD

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(positions, l)
            right = bisect_right(positions, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (hash_val[right + 1] - hash_val[left] * pow10[length]) % MOD
            digit_sum = prefix_sum[right + 1] - prefix_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans