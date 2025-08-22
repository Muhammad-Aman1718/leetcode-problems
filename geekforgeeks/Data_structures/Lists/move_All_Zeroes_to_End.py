# Move All Zeroes to End


# You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.


class Solution:
    def pushZerosToEnd(self, arr: list[int]):
        # code here
        for i in arr:
            print("ths is  i , ", i)
            if i == 0:
                print("this is i , ", i)
                for x in range(i + 1, len(arr)):
                    print("this is  x , ", arr[x])
                    if arr[x] != 0:
                        arr[x] = i
        return arr


obj = Solution()

arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(obj.pushZerosToEnd(arr))
