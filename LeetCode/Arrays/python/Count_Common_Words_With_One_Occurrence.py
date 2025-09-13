# Count Common Words With One Occurrence


# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.


# Example 1:

# Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
# Output: 2
# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this string.
# - "amazing" appears exactly once in each of the two arrays. We count this string.
# - "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
# - "as" appears once in words1, but does not appear in words2. We do not count this string.
# Thus, there are 2 strings that appear exactly once in each of the two arrays.

# Example 2:

# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.

# Example 3:

# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two arrays is "ab".


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        freqWords1: dict[str, int] = {}
        freqWords2: dict[str, int] = {}
        count = 0
        for i in words1:
            freqWords1[i] = freqWords1.get(i, 0) + 1

        for i in words2:
            freqWords2[i] = freqWords2.get(i, 0) + 1

        if len(freqWords1) > len(freqWords2):
            for n in freqWords1:
                if (n in freqWords2) and (freqWords2[n] == 1) and (freqWords1[n] == 1):
                    count += 1
        else:
            for n in freqWords2:
                if (n in freqWords1) and (freqWords1[n] == 1) and (freqWords2[n] == 1):
                    count += 1

        return count


obj = Solution()
# words1 = ["leetcode", "is", "amazing", "as", "is"]
# words2 = ["amazing", "leetcode", "is"]

words1 = ["a","ab"]
words2 = ["a","a","a","ab"]

print(obj.countWords(words1, words2))
