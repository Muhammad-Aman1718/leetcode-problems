# Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq: dict[int, int] = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        result: list[int] = []
        for i in range(k):
            max_value = max(freq, key=freq.get)
            result.append(max_value)
            del freq[max_value]
        return result


obj = Solution()
nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2
print(obj.topKFrequent(nums, k))
