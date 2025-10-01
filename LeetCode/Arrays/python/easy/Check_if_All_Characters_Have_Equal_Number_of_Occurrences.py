# Check if All Characters Have Equal Number of Occurrences

# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).


# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        freq: dict[str, int] = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1

        for i in freq:
            if freq[i] != freq[s[0]]:
                return False
        return True


obj = Solution()
# s = "abacbc"
s = "aaabb"
print(obj.areOccurrencesEqual(s))
