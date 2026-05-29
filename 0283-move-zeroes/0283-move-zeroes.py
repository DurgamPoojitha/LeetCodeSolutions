class Solution:
    def moveZeroes(self, nums):
        pos = 0  # Position for the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1