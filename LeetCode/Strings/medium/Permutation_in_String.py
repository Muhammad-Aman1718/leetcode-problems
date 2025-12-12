# Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


class Solution:

    def findFreq(self, s: str):
        s2Freq: dict[str, int] = {}

        for i in s:
            s2Freq[i] = s2Freq.get(i, 0) + 1
        return s2Freq

    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Freq: dict[str, int] = {}

        for i in s1:
            s1Freq[i] = s1Freq.get(i, 0) + 1

        left = 0
        right = len(s1)

        while right <= len(s2):
            string = s2[left:right]
            freq: dict[str, int] = self.findFreq(string)

            if freq == s1Freq:
                return True

            left += 1
            right += 1

        return False

        # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # left = 0
        # right = 3  # window size

        # while right <= len(a):
        #     window = a[left:right]

        #     print(window)

        #     left += 1
        #     right += 1


obj = Solution()
s1 = "ab"
s2 = "eidboaoo"
print(obj.checkInclusion(s1, s2))
