# Relative Sort Array


# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]


# Example 2:

# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        sortArray: list[int] = []
        frequency: dict[int, int] = {}
        for i in arr1:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        for i in arr2:
            for x in range(frequency[i]):
                sortArray.append(i)
                arr1.remove(i)
        arr1.sort()
        for i in arr1:
            sortArray.append(i)
        return sortArray


obj = Solution()
# arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# arr2 = [2, 1, 4, 3, 9, 6]
arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]

print(obj.relativeSortArray(arr1, arr2))
