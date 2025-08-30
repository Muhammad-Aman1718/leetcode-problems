# Non-Repeating Element


# Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0

# Note: The array consists of only positive and negative integers and not zero.

# Examples:

# Input: arr[] = [-1, 2, -1, 3, 2]
# Output: 3
# Explanation: -1 and 2 are repeating whereas 3 is the only number occuring once. Hence, the output is 3.

# Input: arr[] = [1, 1, 1]
# Output: 0
# Explanation: There is not present any non-repeating element so answer should be 0.
# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(n).


class Solution:
    def firstNonRepeating(self, arr: list[int]):
        # Complete the function

        nonRepeating = 0
        count = 1
        elements: dict[int, int] = {}
        for i in range(len(arr)):
            if arr[i] in elements:
                elements[arr[i]] = elements[arr[i]] + 1
            else:
                elements[arr[i]] = count

        for x in elements:
            if elements.get(x) == 1:
                nonRepeating += x
                break

        if nonRepeating != 0:
            return nonRepeating
        return -1


obj = Solution()
# arr = [-1, 2, -1, 3, 2, 2, -1, -1, 2]
arr = [1, 1, 1, 1]
print(obj.firstNonRepeating(arr))
