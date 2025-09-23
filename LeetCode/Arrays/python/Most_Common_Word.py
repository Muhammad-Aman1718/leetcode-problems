# Most Common Word

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Note that words can not contain punctuation symbols.


# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        paragraph = paragraph.lower()
        cleaned = ""
        for ch in paragraph:
            if ch.isalnum():
                cleaned += ch
            else:
                cleaned += " "

        # 3. words split
        words = cleaned.split()

        freq: dict[str, int] = {}
        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        max_word = ""
        max_count = 0
        for word, count in freq.items():
            if count > max_count:
                max_word = word
                max_count = count

        return max_word


obj = Solution()
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
paragraph = "a."
banned = []
print(obj.mostCommonWord(paragraph, banned))
