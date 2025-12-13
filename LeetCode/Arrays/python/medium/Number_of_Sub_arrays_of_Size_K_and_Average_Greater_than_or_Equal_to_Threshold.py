# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.


# Example 1:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

# Example 2:

# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        # l = 0
        # r = k
        # count = 0

        # while r != len(arr) + 1:
        #     sumSubArr = sum(arr[l:r]) // k
        #     if sumSubArr >= threshold:
        #         count += 1

        #     l += 1
        #     r += 1

        # return count

        # Optimal Solution

        l = 0
        count = 0
        windowSum = sum(arr[:k])
        if windowSum // k >= threshold:
            count += 1

        for r in range(k, len(arr)):
            windowSum += arr[r]
            windowSum -= arr[l]
            if windowSum // k >= threshold:
                count += 1
            l += 1

        return count


obj = Solution()
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(obj.numOfSubarrays(arr, k, threshold))
