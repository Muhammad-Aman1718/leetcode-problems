# Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        frquency: dict[int, int] = {}
        for i in nums:
            if i in frquency:
                print(i)
                frquency[i] += 1
            else:
                # print(i)
                frquency[i] = 1
        return max(frquency, key=frquency.get)


obj = Solution()
# nums = [3, 3, 2]
nums = [3, 3, 2, 3, 4, 2, 1, 4, 2, 3, 4, 2, 1, 3, 4, 2, 4, 2]
print(obj.majorityElement(nums))
