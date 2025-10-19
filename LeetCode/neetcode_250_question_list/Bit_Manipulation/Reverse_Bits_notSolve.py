# Reverse Bits

# Reverse bits of a given 32 bits signed integer.


# Example 1:

# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Example 2:

# Input: n = 2147483644
# Output: 1073741822
# Explanation:
# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110


class Solution:
    def reverseBits(self, n: int) -> int:

        # result = 0
        # for i in range(32):
        #     bit = n & 1
        #     print(n & 1)
        #     result = (result << 1) | bit  # shift result left, add bit
        #     n >>= 1  # shift n right for next bit
        # return result
        for i in range(10):
            print(i & 1)
            print(i | 1)


obj = Solution()
n = 43261596
print(obj.reverseBits(n))
