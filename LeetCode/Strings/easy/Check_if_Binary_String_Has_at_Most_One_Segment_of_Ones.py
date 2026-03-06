# Check if Binary String Has at Most One Segment of Ones

# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.


# Example 1:

# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.

# Example 2:

# Input: s = "110"
# Output: true


class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        return "01" not in s


obj = Solution()
# s = "1001"
s = "110"
s = "100"
s = "11"
print(obj.checkOnesSegment(s))
