# Maximum Difference Between Even and Odd Frequency I

# You are given a string s consisting of lowercase English letters.

# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.


# Example 1:

# Input: s = "aaaaabbc"
# Output: 3
# Explanation:
# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.

# Example 2:

# Input: s = "abcabcab"
# Output: 1
# Explanation:
# The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
# The maximum difference is 3 - 2 = 1.


class Solution:
    def maxDifference(self, s: str) -> int:

        countFreq: dict[str, int] = {}

        for i in s:
            countFreq[i] = countFreq.get(i, 0) + 1
        evenFreq: list[int] = []
        oddFreq: list[int] = []
        for i in countFreq:
            if countFreq[i] % 2 == 0:
                evenFreq.append(countFreq[i])
            else:
                oddFreq.append(countFreq[i])

        return max(oddFreq) - min(evenFreq)


obj = Solution()
# s = "aaaaabbc"
# s = "abcabcab"
s = "mmsmsym"
print(obj.maxDifference(s))
