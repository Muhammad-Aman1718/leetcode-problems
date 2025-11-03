# Remove Trailing Zeros From a String

# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.


# Example 1:

# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

# Example 2:

# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".


class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        # numN = int(num)
        # while True:
        #     if numN % 10 == 0:
        #         numN = numN // 10
        #     else:
        #         break
        # return str(numN)
        
        return num.rstrip('0')


obj = Solution()

num = "51230100"
print(obj.removeTrailingZeros(num))
