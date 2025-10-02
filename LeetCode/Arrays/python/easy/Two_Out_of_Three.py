# Two Out of Three

# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.


# Example 1:

# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.

# Example 2:

# Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# Output: [2,3,1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.

# Example 3:

# Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.


class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]):

        result: list[int] = []
        nums2Set = set(nums2)
        nums3Set = set(nums3)
        for i in range(len(nums1)):
            if nums1[i] in nums2Set:
                result.append(nums1[i])
            if nums1[i] in nums3Set:
                result.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in nums3Set:
                result.append(nums2[i])

        return list(set(result))


obj = Solution()
# nums1 = [1, 1, 3, 2]
# nums2 = [2, 3]
# nums3 = [3]
nums1 = [3, 1]
nums2 = [2, 3]
nums3 = [1, 2]
print(obj.twoOutOfThree(nums1, nums2, nums3))
