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
    def findTwoElement(self, arr:list[int]):
        # code here
        array =[]
        arr.sort()
        
        

obj = Solution()

arr = [4, 3, 6, 2, 1, 1]

print(obj.findTwoElement(arr))

