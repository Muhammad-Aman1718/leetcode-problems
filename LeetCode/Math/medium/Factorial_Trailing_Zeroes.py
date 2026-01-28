# Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.


# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# Example 3:

# Input: n = 0
# Output: 0


class Solution:
    def trailingZeroes(self, n: int) -> int:

        factorial = 1
        for i in range(n, 0, -1):
            factorial *= i

        count = 0
        remainderFactorial = 0

        while remainderFactorial == 0:
            remainderFactorial = factorial % 10
            print(remainderFactorial)
            factorial = factorial / 10
            print(factorial)
            count += 1

        return count - 1

        # strFactorial = str(factorial)
        # count = 0
        # for x in range(len(strFactorial), 0, -1):
        #     if strFactorial[x - 1] == "0":
        #         count += 1
        #     else:
        #         return count

        # return count


obj = Solution()
# n = 5
# n = 10
n = 30
# n = 1574
print(obj.trailingZeroes(n))
