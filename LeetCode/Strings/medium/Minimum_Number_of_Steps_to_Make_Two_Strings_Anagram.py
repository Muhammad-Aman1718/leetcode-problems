# Minimum Number of Steps to Make Two Strings Anagram

# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

# Return the minimum number of steps to make t an anagram of s.

# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


# Example 1:

# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

# Example 2:

# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

# Example 3:

# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams.


class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # Using Hash map

        freqS = {}
        count = 0

        for i in s:
            freqS[i] = freqS.get(i, 0) + 1

        for i in t:
            if i not in freqS or freqS[i] == 0:
                count += 1
            else:
                freqS[i] -= 1

        return count

        # Using Array

        # 26 letters ke liye array

        char_counts = [0] * 26

        # Ek hi loop mein dono ko process karo
        for i in range(len(s)):
            char_counts[ord(s[i]) - ord("a")] += 1
            char_counts[ord(t[i]) - ord("a")] -= 1

        # Sirf positive values ka sum lo
        # (Positive matlab wo s ke characters jo t mein nahi mil sakay)
        return sum(x for x in char_counts if x > 0)


obj = Solution()
s = "leetcode"
t = "practice"
# s = "bab"
# t = "aba"
print(obj.minSteps(s, t))
