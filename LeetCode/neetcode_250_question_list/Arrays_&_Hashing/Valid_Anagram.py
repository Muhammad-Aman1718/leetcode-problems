# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = sorted(s)
        t1 = sorted(t)
        if s1 == t1:
            return True
        return False

        # ChatGpt suggestion

        # return sorted(s) == sorted(t)


obj = Solution()
s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"
print(obj.isAnagram(s, t))
