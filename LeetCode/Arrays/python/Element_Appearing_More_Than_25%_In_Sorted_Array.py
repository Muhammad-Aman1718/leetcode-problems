# Element Appearing More Than 25% In Sorted Array


# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.


# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

# Example 2:

# Input: arr = [1,1]
# Output: 1


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:

        freq: dict[int, int] = {}

        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        return max(freq, key=freq.get)

obj = Solution()
arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
print(obj.findSpecialInteger(arr))
