# Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true

# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:

# Input: s = "abc"
# Output: false


class Solution:
    def validPalindrome(self, s: str) -> bool:

        string = ""

        freq: dict[str, int] = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        for i in freq:
            if freq[i] == 1:
                string = s.replace(i, "", 1)
                break
            else:
                string = s
        return string == string[::-1]


obj = Solution()
# s = "abca"
# s = "aba"
s = "eeccccbebaeeabebccceea"
print(obj.validPalindrome(s))
