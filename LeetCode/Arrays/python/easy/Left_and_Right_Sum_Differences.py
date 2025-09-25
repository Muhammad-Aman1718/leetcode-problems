# Left and Right Sum Differences

# You are given a 0-indexed integer array nums of size n.

# Define two arrays leftSum and rightSum where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.


# Example 1:

# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# Example 2:

# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].


class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:

        leftSum = [0] * len(nums)
        leftValueSum = 0
        for i in range(0, len(nums) - 1):
            leftValueSum += nums[i]
            leftSum[i + 1] = leftValueSum

        rightSum = [0] * len(nums)
        rightValueSum = 0
        for n in range(len(nums) - 1, 0, -1):
            rightValueSum += nums[n]
            rightSum[n - 1] = rightValueSum

        result: list[int] = []
        for i in range(len(leftSum)):
            result.append(abs(leftSum[i] - rightSum[i]))

        return result


obj = Solution()
# nums = [10, 4, 8, 3]
nums = [1]
print(obj.leftRightDifference(nums))
