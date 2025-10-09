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

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left + 1 : right + 1]) or is_palindrome(
                    s[left:right]
                )
            left += 1
            right -= 1
        return True


obj = Solution()
# s = "abca"
# s = "aba"
s = "eeccccbebaeeabebccceea"
print(obj.validPalindrome(s))
