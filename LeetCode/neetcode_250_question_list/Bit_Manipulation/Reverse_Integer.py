# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        MIN_32 = -2**31
        MAX_32 = 2**31 - 1

        if x < 0:
            rev = "-" + str(x)[1:][::-1]
        else:
            rev = str(x)[::-1]

        rev = int(rev)

        if rev < MIN_32 or rev > MAX_32:
            return 0

        return rev


obj = Solution()
# x = -123
x = 120
print(obj.reverse(x))
