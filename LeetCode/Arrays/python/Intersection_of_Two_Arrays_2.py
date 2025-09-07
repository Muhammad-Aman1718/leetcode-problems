# Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set1 | set2)

        # freq = {}
        # for i in nums2:
        #     if i in freq:
        #         freq[i] += 1
        #     else:
        #         freq[i] = 1

        result: list[int] = []
        for i in nums2:
            if i in nums1:
                result.append(i)
                nums1.remove(i)
        return result


obj = Solution()
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(obj.intersect(nums1, nums2))
