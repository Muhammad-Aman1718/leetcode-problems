# Uncommon Words from Two Sentences

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.


# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Explanation:
# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# Example 2:

# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]


class Solution:
    def uncommonFromSentence(self, s1: str, s2: str) -> list[str]:

        arrayS1 = s1.split(" ")
        arrayS1 += s2.split(" ")
        countFreq: dict[str, int] = {}

        for i in arrayS1:
            countFreq[i] = countFreq.get(i, 0) + 1

        result: list[str] = []
        for i in countFreq:
            if countFreq[i] == 1:
                result.append(i)

        return result


obj = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(obj.uncommonFromSentence(s1, s2))
