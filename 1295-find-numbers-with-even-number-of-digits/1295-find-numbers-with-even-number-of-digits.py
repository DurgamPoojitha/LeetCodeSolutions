class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            # Convert number to string and check digit count
            if len(str(num)) % 2 == 0:
                count += 1

        return count