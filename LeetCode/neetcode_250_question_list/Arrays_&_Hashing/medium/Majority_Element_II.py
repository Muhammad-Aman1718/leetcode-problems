# Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]

# Example 2:

# Input: nums = [1]
# Output: [1]

# Example 3:

# Input: nums = [1,2]
# Output: [1,2]


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        countFreq: dict[int, int] = {}
        for i in nums:
            countFreq[i] = countFreq.get(i, 0) + 1
        result: list[int] = []

        for i in countFreq:
            if countFreq[i] > (len(nums) // 3):
                result.append(i)

        return result


obj = Solution()
# nums = [3, 2, 3]
nums = [1, 2]
print(obj.majorityElement(nums))
