# Maximum Nesting Depth of the Parentheses

# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.


# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation:
# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"
# Output: 3
# Explanation:
# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: s = "()(())((()()))"
# Output: 3


class Solution:
    def maxDepth(self, s: str) -> int:

        res = []
        count = 0

        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            res.append(count)
        return max(res)


obj = Solution()
s = "(1+(2*3)+((8)/4))+1"
# s = "(1)+((2))+(((3)))"
# s = "()(())((()()))"
print(obj.maxDepth(s))
