# Check if Any Element Has Prime Frequency

# You are given an integer array nums.

# Return true if the frequency of any element of the array is prime, otherwise, return false.

# The frequency of an element x is the number of times it occurs in the array.

# A prime number is a natural number greater than 1 with only two factors, 1 and itself.


# Example 1:

# Input: nums = [1,2,3,4,5,4]

# Output: true

# Explanation:

# 4 has a frequency of two, which is a prime number.

# Example 2:

# Input: nums = [1,2,3,4,5]

# Output: false

# Explanation:

# All elements have a frequency of one.

# Example 3:

# Input: nums = [2,2,2,4,4]

# Output: true

# Explanation:

# Both 2 and 4 have a prime frequency.


class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        # Step 1: frequency count karo
        freq: dict[int, int] = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        def isPrime(n: int) -> bool:
            if n <= 1:
                return False
            for x in range(2, int(n**0.5) + 1):
                if n % x == 0:
                    return False
            return True

        for count in freq.values():
            if isPrime(count):
                return True
        return False


obj = Solution()
# nums = [1, 2, 3, 4, 5, 4]
# nums = [1,2,3,4,5]
nums = [2, 2, 2, 4, 4]
print(obj.checkPrimeFrequency(nums))
