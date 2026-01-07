import math

# Four Divisors

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.


# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.

# Example 2:

# Input: nums = [21,21]
# Output: 64

# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0


class Solution:

    # Brute Force

    # def checkDivision(self, num: int):

    #     countDivisidor = 0
    #     sumOfNumDivisidor = 0
    #     i = 1
    #     while i != num + 1:
    #         if num % i == 0:
    #             countDivisidor += 1
    #             sumOfNumDivisidor += i
    #         i += 1

    #     if countDivisidor == 4:
    #         return sumOfNumDivisidor

    #     return 0

    # def sumFourDivisors(self, nums: list[int]) -> int:
    #     sumOfValues = 0
    #     for i in nums:
    #         num = self.checkDivision(i)
    #         if num != 0:
    #             sumOfValues += num

    #     return sumOfValues

    # Optimize solution

    def checkDivision(self, num: int) -> int:
        divisors = set()
        # Sirf square root tak check karein
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)

                if len(divisors) > 4:
                    return 0

        if len(divisors) == 4:
            return sum(divisors)

        return 0

    def sumFourDivisors(self, nums: list[int]) -> int:
        total_sum = 0
        for n in nums:
            total_sum += self.checkDivision(n)
        return total_sum


obj = Solution()
# nums = [21, 4, 7]
nums = [21, 21]
print(obj.sumFourDivisors(nums))
