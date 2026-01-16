# Reverse String Prefix

# You are given a string s and an integer k.

# Reverse the first k characters of s and return the resulting string.


# Example 1:

# Input: s = "abcd", k = 2
# Output: "bacd"
# Explanation:​​​​​​​
# The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".

# Example 2:

# Input: s = "xyz", k = 3
# Output: "zyx"
# Explanation:
# The first k = 3 characters "xyz" are reversed to "zyx". The final resulting string is "zyx".

# Example 3:

# Input: s = "hey", k = 1
# Output: "hey"
# Explanation:
# The first k = 1 character "h" remains unchanged on reversal. The final resulting string is "hey".


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        sArr = list(s)

        left = 0
        right = k - 1
        while left <= right:
            sArr[left], sArr[right] = sArr[right], sArr[left]
            left += 1
            right -= 1

        return "".join(sArr)


obj = Solution()
s = "abcd"
k = 2
print(obj.reversePrefix(s, k))
