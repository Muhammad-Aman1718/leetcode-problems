# Divide Array Into Equal Pairs


# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.


# Example 1:

# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation:
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.


# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.


class Solution:
    def divideArray(self, nums: list[int]) -> bool:

        freq: dict[int, int] = {}
        count = 0
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in freq:
            rem = int(freq[i] / 2)
            if freq[i] % 2 == 0:
                count += rem

        if count == len(nums) / 2:
            return True

        return False


obj = Solution()
# nums = [3, 2, 3, 2, 2, 2]
nums = [1, 2, 3, 4]
print(obj.divideArray(nums))
