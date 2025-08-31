# More than n/k Occurrences


# Given an array arr and an element k. The task is to find the count of elements in the array
# that appear more than n/k times and n is length of arr.

# Examples :

# Input: arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
# Output: 2
# Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times.

# Input: arr = [2, 3, 3, 2], k = 3
# Output: 2
# Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times. So the count of elements are 2.

# Input: arr = [1, 4, 7, 7], k = 2
# Output: 0
# Explanation: In the given array, no element appears more than n/k times.


class Solution:

    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self, arr: list[int], k: int):
        # Your code here
        avrg: float = len(arr) / k
        frequncy: dict[int, int] = {}
        count = 1
        maxNumber = 0
        for i in arr:
            if i in frequncy:
                frequncy[i] += 1
            else:
                frequncy[i] = count

        for x in frequncy:
            if frequncy[x] > avrg:
                maxNumber += 1
        return maxNumber


obj = Solution()
arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
print(obj.countOccurence(arr, k))
