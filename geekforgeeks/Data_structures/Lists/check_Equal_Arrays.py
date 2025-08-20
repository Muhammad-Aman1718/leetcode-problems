# Check Equal Arrays


# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
# Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

# Examples:

# Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
# Output: true
# Explanation: Both the array can be rearranged to [0,1,2,4,5]
# Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
# Output: false
# Explanation: a[] and b[] have only one common value.


class Solution:
    def checkEqual(self, a: list[int], b: list[int]):
        # code here
        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False


obj = Solution()
a: list[int] = [1, 2, 5, 4, 0]
b: list[int] = [2, 4, 5, 0, 1]

print(obj.checkEqual(a, b))
