# Degree of an Array


# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.


# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.


# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:

        first: dict[int, int] = {}
        last: dict[int, int] = {}
        freq: dict[int, int] = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            freq[num] = freq.get(num, 0) + 1
        degree = max(freq.values())
        min_length = float("inf")

        for num in freq:
            if freq[num] == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)

        return int(min_length)


obj = Solution()
nums = [1, 2, 2, 3, 1, 4, 2]
print(obj.findShortestSubArray(nums))
