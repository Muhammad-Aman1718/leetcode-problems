# Check Distances Between Same Letters

# You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.
# Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
# In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

# Return true if s is a well-spaced string, otherwise return false.


# Example 1:

# Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: true
# Explanation:
# - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
# - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
# - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
# Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
# Return true because s is a well-spaced string.

# Example 2:

# Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: false
# Explanation:
# - 'a' appears at indices 0 and 1 so there are zero letters between them.
# Because distance[0] = 1, s is not a well-spaced string.


class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:

        distanceDict: dict[str, int] = {
            "a": distance[0],
            "b": distance[1],
            "c": distance[2],
            "d": distance[3],
            "e": distance[4],
            "f": distance[5],
            "g": distance[6],
            "h": distance[7],
            "i": distance[8],
            "j": distance[9],
            "k": distance[10],
            "l": distance[11],
            "m": distance[12],
            "n": distance[13],
            "o": distance[14],
            "p": distance[15],
            "q": distance[16],
            "r": distance[17],
            "s": distance[18],
            "t": distance[19],
            "u": distance[20],
            "v": distance[21],
            "w": distance[22],
            "x": distance[23],
            "y": distance[24],
            "z": distance[25],
        }

        checkStringDistance: dict[str, int] = {}

        for i in range(len(s)):
            if s[i] in checkStringDistance:
                checkStringDistance[s[i]] = abs(checkStringDistance[s[i]] - i) - 1
            else:
                checkStringDistance[s[i]] = i

        for i in checkStringDistance:
            if checkStringDistance[i] != distanceDict[i]:
                return False

        return True


obj = Solution()
# s = "abaccb"
# distance = [
#     1,
#     3,
#     0,
#     5,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
# ]

s = "aa"
distance = [
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]


print(obj.checkDistances(s, distance))
