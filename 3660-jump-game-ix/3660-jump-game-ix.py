class Solution:
    def maxValue(self, nums):
        n = len(nums)

        prefMax = [0] * n
        suffMin = [0] * n

        # Prefix maximum
        prefMax[0] = nums[0]
        for i in range(1, n):
            prefMax[i] = max(prefMax[i - 1], nums[i])

        # Suffix minimum
        suffMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(suffMin[i + 1], nums[i])

        ans = [0] * n
        start = 0

        for i in range(n - 1):

            # Correct condition: <=
            if prefMax[i] <= suffMin[i + 1]:

                mx = max(nums[start:i + 1])

                for j in range(start, i + 1):
                    ans[j] = mx

                start = i + 1

        # Last component
        mx = max(nums[start:])

        for j in range(start, n):
            ans[j] = mx

        return ans