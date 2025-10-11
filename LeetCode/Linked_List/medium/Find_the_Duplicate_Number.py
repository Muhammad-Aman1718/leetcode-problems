# Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        freq: dict[int, int] = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in freq:
            if freq[i] > 1:
                return i


obj = Solution()
nums = [3, 1, 3, 4, 2]
print(obj.findDuplicate(nums))
