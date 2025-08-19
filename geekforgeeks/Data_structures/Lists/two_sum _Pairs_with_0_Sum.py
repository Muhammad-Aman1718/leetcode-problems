# Two sum -Pairs with 0 Sum


# Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

# Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

# Examples:

# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 1]]
# Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
# arr[2] + arr[4] = 1 + (-1) = 0.
# The distinct pair are [-1,1].

# Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# Output: [[-6, 6],[-1, 1]]
# Explanation: The distinct pairs are [-1, 1] and [-6, 6].


class Solution:
    def getPairs(self, arr: list[int]) -> list[int]:
        # code here

        # This is code is written by me

        # twoDArray: list[int] = []

        # for i in range(len(arr)):
        #     array: list[int] = []
        #     for j in range(i + 1, len(arr)):
        #         if arr[i] + arr[j] == 0:
        #             if arr[i] not in array:
        #                 array.append(arr[i])
        #                 array.append(arr[j])
        #     array.sort()
        #     if len(array) != 0 and array not in twoDArray:
        #         twoDArray.append(array)
        # twoDArray.sort()
        # return twoDArray

        # this code is written by chatgpt

        original_set = set(arr)

        result_pairs: set[int] = set()

        zero_count = arr.count(0)  # count how many zeros

        for num in arr:
            # handle zero: only accept if there are at least 2 zeros
            if num == 0:
                if zero_count >= 2:
                    result_pairs.add((0, 0))
                # skip the rest so it doesn't get added again
                continue

            opp = -num
            if opp in original_set:
                pair = tuple(sorted((num, opp)))
                result_pairs.add(pair)

        # convert each tuple to list & sort final result
        final_result: list[int] = [list(p) for p in result_pairs]
        final_result.sort()
        return final_result


obj = Solution()
# arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# arr = [-1, 0, 1, 2, -1, -4]
# arr = [-1, 10, 7, 3, -9, -9, -7]
# arr = [-1, 0, 1, 2, -1, -4]
arr = [-8, -10, -10, -10, 10, 6, 1, 10]

print(obj.getPairs(arr))
