# First and Second Smallests


# Given an array, arr[] of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

# Examples:

# Input: arr[] = [2, 4, 3, 5, 6]
# Output: [2, 3]
# Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
# Input: arr[] = [1, 1, 1]
# Output: [-1]
# Explanation: Only element is 1 which is smallest, so there is no second smallest element.


class Solution:
    def minAnd2ndMin(self, arr: list[int]) -> list[int]:
        # code here
        elements: list[int] = []
        arr.sort()
        print("this is sorted arr ===> ", arr)
        for i in arr:
            if i not in elements:
                elements.append(i)
            if i != elements[0]:
                print("this is if  ===> ", i)
                elements.append
                return elements

        return [-1]


obj = Solution()
# arr = [2, 4, 3, 5, 6]
# arr = [1, 1, 1]
arr = [87, 76, 7, 12, 83, 89, 8, 100, 36, 2, 50, 51, 2, 41, 41, 38, 41]
print(obj.minAnd2ndMin(arr))
