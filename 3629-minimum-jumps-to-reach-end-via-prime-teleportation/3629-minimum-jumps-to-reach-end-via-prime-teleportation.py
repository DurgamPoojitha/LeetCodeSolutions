from collections import deque, defaultdict
from math import isqrt

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # Search for smallest prime factor
        MAXV = max(nums)
        spf = list(range(MAXV + 1))

        for i in range(2, isqrt(MAXV) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXV + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        #  Get unique prime factors 
        def get_prime_factors(x):
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors

        #  Map prime -> indices divisible by prime
        prime_to_indices = defaultdict(list)

        for i, val in enumerate(nums):
            for p in get_prime_factors(val):
                prime_to_indices[p].append(i)

        # Prime checking
        def is_prime(x):
            return x >= 2 and spf[x] == x

        # BFS
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0

        used_prime = set()

        while q:
            i = q.popleft()

            if i == n - 1:
                return dist[i]

            # Adjacent moves
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and dist[ni] == -1:
                    dist[ni] = dist[i] + 1
                    q.append(ni)

            # Prime teleportation
            val = nums[i]

            if is_prime(val) and val not in used_prime:
                used_prime.add(val)

                for ni in prime_to_indices[val]:
                    if dist[ni] == -1:
                        dist[ni] = dist[i] + 1
                        q.append(ni)

        return -1