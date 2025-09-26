# Monotonic Array

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


# Example 1:

# Input: nums = [1,2,2,3]
# Output: true

# Example 2:

# Input: nums = [6,5,4,4]
# Output: true

# Example 3:

# Input: nums = [1,3,2]
# Output: false


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        increasingOrder = sorted(nums)
        decreasingOrder = sorted(nums, reverse=True)

        increasingCount = 0
        decreasingCount = 0
        for i in range(len(nums)):
            if nums[i] == increasingOrder[i]:
                increasingCount += 1
            if nums[i] == decreasingOrder[i]:
                decreasingCount += 1

        if increasingCount == len(nums) or decreasingCount == len(nums):
            return True

        return False

        #  Optimize Code

        increase = True
        decrease = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decrease = False
            if nums[i] < nums[i - 1]:
                increase = False

        return increase or decrease


obj = Solution()
# nums = [1, 2, 2, 3]
# nums = [6, 5, 4, 4]
nums = [1, 3, 2]
print(obj.isMonotonic(nums))
