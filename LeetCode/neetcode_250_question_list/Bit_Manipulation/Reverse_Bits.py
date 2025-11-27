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

        binaryForm = str(bin(n))[2::]
        reverseBinFrom = binaryForm[::-1]
        while len(reverseBinFrom) != 32:
            reverseBinFrom += "0"

        return int(reverseBinFrom, 2)


obj = Solution()
n = 43261596
print(obj.reverseBits(n))
