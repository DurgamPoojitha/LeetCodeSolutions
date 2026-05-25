class Solution:
    def shuffle(self, nums, n):
        result = []

        for i in range(n):
            result.append(nums[i])      # xi
            result.append(nums[i + n])  # yi

        return result