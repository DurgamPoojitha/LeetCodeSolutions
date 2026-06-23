class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1  # number of possible values

        # Length = 2
        up = [0] * (m + 1)     # up[v] = count ending at value v with last move up
        down = [0] * (m + 1)   # down[v] = count ending at value v with last move down

        for v in range(1, m + 1):
            up[v] = v - 1          # previous value < v
            down[v] = m - v        # previous value > v

        # Build lengths 3..n
        for _ in range(3, n + 1):
            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            # prefix sums of down
            prefix = [0] * (m + 1)
            for v in range(1, m + 1):
                prefix[v] = (prefix[v - 1] + down[v]) % MOD

            for v in range(1, m + 1):
                # last move becomes up, so previous move must be down
                new_up[v] = prefix[v - 1]

            # suffix sums of up
            suffix = [0] * (m + 2)
            for v in range(m, 0, -1):
                suffix[v] = (suffix[v + 1] + up[v]) % MOD

            for v in range(1, m + 1):
                # last move becomes down, so previous move must be up
                new_down[v] = suffix[v + 1]

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD