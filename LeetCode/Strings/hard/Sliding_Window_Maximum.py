# Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        # if not nums:
        #     return []

        # res = []
        # current_max = max(nums[:k])
        # res.append(current_max)

        # for i in range(1, len(nums) - k + 1):
        #     left_out = nums[i - 1]
        #     new_in = nums[i + k - 1]

        #     if new_in >= current_max:
        #         current_max = new_in

        #     elif left_out == current_max:
        #         current_max = max(nums[i : i + k])

        #     res.append(current_max)

        # return res

        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        right = [0] * n

        # 1. Left side se max bharo har k-size block ke liye
        for i in range(n):
            if i % k == 0:  # Block shuru ho raha hai
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

        # 2. Right side se max bharo
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if (i + 1) % k == 0:  # Block ka end hai
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        res = []
        for i in range(n - k + 1):
            res.append(max(right[i], left[i + k - 1]))

        return res


obj = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# nums = [1, -1]
# k = 1
print(obj.maxSlidingWindow(nums, k))
