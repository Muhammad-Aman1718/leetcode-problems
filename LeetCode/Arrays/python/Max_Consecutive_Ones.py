# Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        consecutiveOnes: list[int] = []
        count = 0

        for i in nums:
            if i == 1:
                count += 1
            if i == 0:
                consecutiveOnes.append(count)
                count = 0
        consecutiveOnes.append(count)
        return max(consecutiveOnes)


obj = Solution()
nums = [1, 1, 0, 1, 1, 1]
# nums = [1, 0, 1, 1, 0, 1]

print(obj.findMaxConsecutiveOnes(nums))
