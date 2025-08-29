# Move all negative elements to end


# Given an unsorted array arr[ ] having both negative and positive integers. The task is to place all negative elements at the end of the array without changing the order of positive elements and negative elements.

# Note: Don't return any array, just in-place on the array.

# Examples:

# Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
# Output : [1, 3, 2, 11, 6, -1, -7, -5]
# Explanation: By doing operations we separated the integers without changing the order.

# Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
# Output : [7, 9, 10, 11, -5, -3, -4, -1]

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)


class Solution:
    def segregateElements(self, arr: list[int]):

        # Your code goes here
        nagetive: list[int] = []
        postive: list[int] = []

        for i in range(len(arr)):
            if arr[i] < 0:
                nagetive.append(arr[i])
            else:
                postive.append(arr[i])

        for i in nagetive:
            postive.append(i)

        return postive


obj = Solution()
# arr = [1, -1, 3, 2, -7, -5, 11, 6]
arr = [-5, 7, -3, -4, 9, 10, -1, 11]
print(obj.segregateElements(arr))
