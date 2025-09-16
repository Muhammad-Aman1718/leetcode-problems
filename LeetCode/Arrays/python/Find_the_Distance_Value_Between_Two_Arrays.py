# Find the Distance Value Between Two Arrays

# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.


# Example 1:

# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation:
# For arr1[0]=4 we have:
# |4-10|=6 > d=2
# |4-9|=5 > d=2
# |4-1|=3 > d=2
# |4-8|=4 > d=2
# For arr1[1]=5 we have:
# |5-10|=5 > d=2
# |5-9|=4 > d=2
# |5-1|=4 > d=2
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2

# Example 2:

# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2

# Example 3:

# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # This is brute force approach

        # result: list[int] = []

        # for i in arr1:
        #     count = 0
        #     for n in arr2:
        #         if abs(i - n) > d:
        #             count += 1
        #     result.append(count)
        # count = 0
        # for i in result:
        #     if i == len(arr2):
        #         count += 1

        # return count

        # This is optimize code

        arr2.sort()

        def binary_search(target: int) -> bool:
            """Check if koi element arr2 me [target-d, target+d] range me exist karta hai"""
            left, right = 0, len(arr2) - 1
            while left <= right:
                mid = (left + right) // 2
                if abs(arr2[mid] - target) <= d:
                    return True  # range ke andar element mila
                elif arr2[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        # Step 2: har arr1[i] ke liye binary search karo
        count = 0
        for num in arr1:
            if not binary_search(num):
                count += 1

        return count


obj = Solution()
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
# arr1 = [2, 1, 100, 3]
# arr2 = [-5, -2, 10, -3, 7]
# d = 6
print(obj.findTheDistanceValue(arr1, arr2, d))
