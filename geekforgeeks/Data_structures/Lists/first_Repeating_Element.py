# First Repeating Element


# Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

# Note:- The position you return should be according to 1-based indexing.

# Examples:

# Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
# Output: 2
# Explanation: 5 appears twice and its first appearance is at index 2 which is less than 3 whose first the occurring index is 3.
# Input: arr[] = [1, 2, 3, 4]
# Output: -1
# Explanation: All elements appear only once so answer is -1.


class Solution:
    def firstRepeated(self, arr: list[int]):
        # code here
        index_map: dict[int, int] = {}
        min_index = float("inf")

        for i in range(len(arr)):
            if arr[i] in index_map:
                min_index = min(min_index, index_map[arr[i]])
            else:
                index_map[arr[i]] = i + 1  # 1-based indexing
        return min_index if min_index != float("inf") else -1


obj = Solution()
arr = [1, 5, 3, 4, 3, 5, 6]
print(obj.firstRepeated(arr))
