# Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.


class Solution:

    def intersection(self, num1: list[int], num2: list[int]):
        num1Set = set(num1)
        num2Set = set(num2)

        return list(num1Set & num2Set)


obj = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(obj.intersection(nums1, nums2))
