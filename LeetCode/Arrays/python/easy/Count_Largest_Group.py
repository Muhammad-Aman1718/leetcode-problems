# Count Largest Group

# You are given an integer n.

# We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

# Return the number of groups that have the largest size, i.e. the maximum number of elements.


# Example 1:

# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.

# Example 2:

# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.


class Solution:
    def countLargestGroup(self, n: int) -> int:
        countFreq: dict[int, int] = {}

        for i in range(1, n + 1):
            eleSum = sum(int(d) for d in str(i))
            countFreq[eleSum] = countFreq.get(eleSum, 0) + 1

        maxFreq = max(countFreq.values())
        return sum(1 for v in countFreq.values() if v == maxFreq)


obj = Solution()
n = 13
print(obj.countLargestGroup(n))
