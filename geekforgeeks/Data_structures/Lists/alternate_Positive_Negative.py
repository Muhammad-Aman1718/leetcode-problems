# Alternate Positive Negative

# Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

# Note:
# - Resulting array should start with a positive integer (0 will also be considered as a positive integer).
# - If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
# - The array may or may not have the equal number of positive and negative integers.

# Examples:

# Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
# Explanation: The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 4 and then -1 and so on.


class Solution:
    def rearrange(self, arr: list[int]) -> list[int]:
        # code here
        positive: list[int] = []
        negative: list[int] = []
        newList: list[int] = []

        for i in arr:
            if i >= 0:
                positive.append(i)
            if i < 0:
                negative.append(i)

        for n in range(len(arr)):
            if n < len(positive):
                newList.append(positive[n])
            if n < len(negative):
                newList.append(negative[n])

        return newList


sol = Solution()
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]

print(sol.rearrange(arr))
