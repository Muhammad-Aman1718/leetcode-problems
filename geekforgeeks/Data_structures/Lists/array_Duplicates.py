# Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

# Note: You can return the elements in any order but the driver code will print them in sorted order.

# Examples:

# Input: arr[] = [2, 3, 1, 2, 3]
# Output: [2, 3]
# Explanation: 2 and 3 occur more than once in the given array.

# Input: arr[] = [3, 1, 2]
# Output: []
# Explanation: There is no repeating element in the array, so the output is empty.


class Solution:
    def findDuplicates(self, arr: list[int]) -> list[int]:
        # code here
        seen: set[int] = set()
        duplicates: set[int] = set()

        for i in arr:
            if i in seen:
                duplicates.add(i)
            else:
                seen.add(i)

        return list(duplicates)


obj = Solution()


# arr: list[int] = [2, 3, 1, 2, 3]
arr = [3, 1, 2]

print(obj.findDuplicates(arr))
