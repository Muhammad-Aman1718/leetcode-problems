# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        prefix = [1] * n

        for i in range(n - 1):
            prefix[i + 1] = prefix[i] * nums[i]

        suffix = [1] * n

        for i in range(n - 1, 0, -1):
            suffix[i - 1] = suffix[i] * nums[i]

        result: list[int] = []

        for i in range(n):
            result.append(prefix[i] * suffix[i])

        return result


obj = Solution()
nums = [1, 2, 3, 4]
print(obj.productExceptSelf(nums))
