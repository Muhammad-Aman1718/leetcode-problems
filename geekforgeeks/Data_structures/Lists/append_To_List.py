#  Append To List

# You are given three inputs a, b, c. You need to create a list and append a, b, c to the list and then return that list.

# Examples:

# Input: a = 1, b = 2, c = 3
# Output: 1 2 3
# Explanation: Just create a list and append 1 2 3 to it. Then return [1,2,3] list.

# Input: a = 4, b = 5, c = 6
# Output: 4 5 6
# Explanation: Just create a list and append 4 5 6 to it. Then return [4,5,6] list.


def appendToList(a: int, b: int, c: int) -> list[int]:
    # code here
    newList: list[int] = []
    newList.append(a)
    newList.append(b)
    newList.append(c)

    return newList


a = 1
b = 2
c = 3


print(appendToList(a, b, c))
