# Find The Least Frequent Digit

# Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have the same frequency, choose the smallest digit.
# Return the chosen digit as an integer.
# The frequency of a digit x is the number of times it appears in the decimal representation of n.


# Example 1:

# Input: n = 1553322
# Output: 1
# Explanation:
# The least frequent digit in n is 1, which appears only once. All other digits appear twice.

# Example 2:

# Input: n = 723344511
# Output: 2
# Explanation:
# The least frequent digits in n are 7, 2, and 5; each appears only once.


class Solution:
    def getLeastFrequentDigit(self, b: int) -> int:

        n = str(b)
        countFreq: dict[str, int] = {}

        for i in n:
            countFreq[i] = countFreq.get(i, 0) + 1

        result: list[int] = []
        for i in countFreq:
            if countFreq[i] == 1:
                result.append(int(i))
        if result:
            return min(result)
        else:
            return 0


obj = Solution()
n = 723344511
print(obj.getLeastFrequentDigit(n))
