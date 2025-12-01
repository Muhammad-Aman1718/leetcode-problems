# Ugly Number

# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.


# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.

# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.


class Solution:
    def isUgly(self, n: int) -> bool:

        if n == 1:
            return True

        res: list[int] = []
        i = 2

        while n != 1:
            if n % i == 0:
                res.append(i)
                i = 2
                n = n // i
            else:
                i += 1

        for i in res:
            if i != 2 and i != 3 and i != 5:
                return False

        return True


obj = Solution()
n = 6
print(obj.isUgly(n))
