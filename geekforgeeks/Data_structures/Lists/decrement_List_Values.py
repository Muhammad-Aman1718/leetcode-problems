# Decrement List Values

# You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

# Example:

# Input: arr = [54, 43, 2, 1, 5]
# Output: 53 42 1 0 4
# Explanation: Just decrement the numbers by 1.


def decrementList(arr: list[int]) -> list[int]:
    # code here
    return [x - 1 for x in arr]


arr: list[int] = [54, 43, 2, 1, 5]
print(decrementList(arr))
