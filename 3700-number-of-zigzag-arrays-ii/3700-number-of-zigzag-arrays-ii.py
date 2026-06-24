MOD = 10**9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        if n == 1:
            return m

        size = 2 * m

        T = [[0] * size for _ in range(size)]

        # state:
        # 0..m-1     -> last move was UP, ending at value v
        # m..2m-1    -> last move was DOWN, ending at value v

        for v in range(m):
            for u in range(v):
                T[v][m + u] = 1          # DOWN -> UP

            for u in range(v + 1, m):
                T[m + v][u] = 1          # UP -> DOWN

        # vector for length 2
        init = [0] * size

        for v in range(m):
            init[v] = v                  # pairs ending at v with last move UP
            init[m + v] = m - 1 - v      # pairs ending at v with last move DOWN

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]

            for i in range(n):
                for k in range(n):
                    if A[i][k] == 0:
                        continue
                    aik = A[i][k]

                    for j in range(n):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD

            return C

        def mat_pow(M, p):
            n = len(M)

            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)

                M = mat_mul(M, M)
                p >>= 1

            return R

        if n == 2:
            return sum(init) % MOD

        P = mat_pow(T, n - 2)

        ans = 0

        for i in range(size):
            for j in range(size):
                ans = (ans + P[i][j] * init[j]) % MOD

        return ans