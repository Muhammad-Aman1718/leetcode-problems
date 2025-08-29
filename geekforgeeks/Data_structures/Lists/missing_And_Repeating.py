# Missing And Repeating


# Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

# Examples:

# Input: arr[] = [2, 2]
# Output: [2, 1]
# Explanation: Repeating number is 2 and the missing number is 1.

# Input: arr[] = [1, 3, 3]
# Output: [3, 2]
# Explanation: Repeating number is 3 and the missing number is 2.

# Input: arr[] = [4, 3, 6, 2, 1, 1]
# Output: [1, 5]
# Explanation: Repeating number is 1 and the missing number is 5.


class Solution:
    def findTwoElement(self, arr: list[int]):
        # code here
        seen: set[int] = set()
        duplicate = -1

        n = len(arr)

        for num in arr:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)
        missing = -1
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break
        return [duplicate, missing]


obj = Solution()

# arr = [4, 3, 6, 2, 1, 1]
arr = [6, 5, 8, 7, 1, 4, 1, 3, 2]

print(obj.findTwoElement(arr))
