# Find Unique Binary String

# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.


# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.

# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:

        numsSet = set(nums)

        n = len(nums[0])
        if nums[0] == "1":
            return "0"
        elif nums[0] == "0":
            return "1"
        num = 2 ** (n - 1)
        if n < 3:
            num = 0
        loopEnd = 2**n
        for i in range(num, loopEnd):
            binNum = bin(i)[2::].zfill(2)
            if binNum not in numsSet:
                return binNum


obj = Solution()
# nums = ["111", "011", "001"]
# nums = ["01", "10"]
nums = ["10", "11"]
print(obj.findDifferentBinaryString(nums))
