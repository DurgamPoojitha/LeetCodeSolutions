class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7

        from collections import Counter

        # Count of elements to the right
        right = Counter(nums)

        # Count of elements to the left
        left = Counter()

        ans = 0

        for num in nums:
            # Current element is now being processed
            right[num] -= 1

            target = num * 2

            # Count valid i and k
            left_count = left[target]
            right_count = right[target]

            ans = (ans + left_count * right_count) % MOD

            # Add current element to left side
            left[num] += 1

        return ans