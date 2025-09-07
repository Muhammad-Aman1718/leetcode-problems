# Sum of Unique Elements

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.


# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.

# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq: dict[int, int] = {}
        sumOfValues = 0
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in freq:
            if freq[i] == 1:
                sumOfValues += i

        return sumOfValues


obj = Solution()
# nums = [1, 2, 3, 4, 5]
# nums = [1, 2, 3, 2]
nums = [1, 1, 1, 1, 1]
print(obj.sumOfUnique(nums))
