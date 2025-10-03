# Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)  # fast lookup
        longest = 0

        for num in num_set:
            # check if it's the start of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                # expand sequence
                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


obj = Solution()
# nums = [10, 4, 20, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(obj.longestConsecutive(nums))
