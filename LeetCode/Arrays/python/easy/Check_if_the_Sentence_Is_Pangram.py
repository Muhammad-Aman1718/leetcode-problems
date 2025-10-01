# Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:

# Input: sentence = "leetcode"
# Output: false


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        sets = set(sentence)

        alphabet = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        for i in alphabet:
            if i not in sets:
                return False
        return True


obj = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(obj.checkIfPangram(sentence))
