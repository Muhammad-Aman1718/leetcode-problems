# Find Common Characters


# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.


# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        def countFreq(word: str):
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            return freq

        # base frequency from first word
        common = countFreq(words[0])

        # update with min frequency of each word
        for word in words[1:]:
            freq = countFreq(word)
            for i in range(26):
                common[i] = min(common[i], freq[i])

        # convert frequency back to character list
        result: list[str] = []
        for i in range(26):
            result.extend([chr(i + ord("a"))] * common[i])

        return result


obj = Solution()
words = ["bella", "label", "roller"]
print(obj.commonChars(words))
