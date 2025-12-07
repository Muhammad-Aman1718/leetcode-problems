# Strictly Palindromic Number

# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

# Given an integer n, return true if n is strictly palindromic and false otherwise.

# A string is palindromic if it reads the same forward and backward.


# Example 1:

# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.

# Example 2:

# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
# Therefore, we return false.


class Solution:
    def to_base(self, n: int, b: int):
        digits = ""
        while n > 0:
            digits = str(n % b) + digits
            n //= b
        return digits

    def is_palindrome(self, s: str):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def isStrictlyPalindromic(self, n: int):
        for b in range(2, n - 1):
            converted = self.to_base(n, b)
            if not self.is_palindrome(converted):
                return False
        return True


obj = Solution()
n = 9
print(obj.isStrictlyPalindromic(n))
