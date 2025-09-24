# Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        result: list[int] = []
        n = len(nums)
        for i in range(0, n):
            multiple = 0
            for n in range(0, i + 1):
                multiple += nums[n]
            result.append(multiple)

        return result


obj = Solution()
nums = [1, 2, 3, 4]
# nums = [3, 1, 2, 10, 1]
print(obj.runningSum(nums))
