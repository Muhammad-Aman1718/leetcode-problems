# Find if Digit Game Can Be Won

# You are given an array of positive integers nums.
# Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.
# Return true if Alice can win this game, otherwise, return false.


# Example 1:

# Input: nums = [1,2,3,4,10]
# Output: false
# Explanation:
# Alice cannot win by choosing either single-digit or double-digit numbers.

# Example 2:

# Input: nums = [1,2,3,4,5,14]
# Output: true
# Explanation:
# Alice can win by choosing single-digit numbers which have a sum equal to 15.

# Example 3:

# Input: nums = [5,5,5,25]
# Output: true
# Explanation:
# Alice can win by choosing double-digit numbers which have a sum equal to 25.


class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:

        sumOfAllSingleDigits = 0
        sumOfAllDoubleDigits = 0

        for i in nums:
            stringI = str(i)
            if len(stringI) == 1:
                sumOfAllSingleDigits += i
            if len(stringI) == 2:
                sumOfAllDoubleDigits += i
        if sumOfAllSingleDigits == sumOfAllDoubleDigits:
            return False

        return True


obj = Solution()
nums = [1, 2, 3, 4, 10]
print(obj.canAliceWin(nums))
