# Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        setNum1 = set(nums1)
        nums: list[int] = []
        median: float = 0

        for i in nums2:
            setNum1.add(i)

        for i in setNum1:
            nums.append(i)
        n = len(nums)

        if n % 2 == 1:
            median = nums[int((n + 1) / 2) - 1]
        else:
            median = (nums[int(n / 2) - 1] + nums[int((n / 2) + 1) - 1]) / 2

        result = f"{median:.5f}"

        return result


obj = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
print(obj.findMedianSortedArrays(nums1, nums2))
