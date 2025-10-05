# Minimum Deletions for At Most K Distinct Characters

# You are given a string s consisting of lowercase English letters, and an integer k.

# Your task is to delete some (possibly none) of the characters in the string so that the number of distinct characters in the resulting string is at most k.

# Return the minimum number of deletions required to achieve this.


# Example 1:

# Input: s = "abc", k = 2
# Output: 1
# Explanation:
# s has three distinct characters: 'a', 'b' and 'c', each with a frequency of 1.
# Since we can have at most k = 2 distinct characters, remove all occurrences of any one character from the string.
# For example, removing all occurrences of 'c' results in at most k distinct characters. Thus, the answer is 1.

# Example 2:

# Input: s = "aabb", k = 2
# Output: 0
# Explanation:
# s has two distinct characters ('a' and 'b') with frequencies of 2 and 2, respectively.
# Since we can have at most k = 2 distinct characters, no deletions are required. Thus, the answer is 0.

# Example 3:

# Input: s = "yyyzz", k = 1
# Output: 2
# Explanation:
# s has two distinct characters ('y' and 'z') with frequencies of 3 and 2, respectively.
# Since we can have at most k = 1 distinct character, remove all occurrences of any one character from the string.
# Removing all 'z' results in at most k distinct characters. Thus, the answer is 2.


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq: dict[str, int] = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: If already at most k distinct characters, no deletions needed
        if len(freq) <= k:
            return 0

        # Step 3: Extract all frequencies
        values: list[int] = []
        for key in freq:
            values.append(freq[key])

        # Step 4: Sort frequencies (ascending)
        values.sort()

        # Step 5: Calculate deletions
        deletions = 0
        extra = len(values) - k
        for i in range(extra):
            deletions += values[i]

        # Step 6: Return result
        return deletions


obj = Solution()
# s = "abc"
s = "yyyzz"
k = 1
# k = 2
# s = "aabb"
# k = 2
print(obj.minDeletion(s, k))
