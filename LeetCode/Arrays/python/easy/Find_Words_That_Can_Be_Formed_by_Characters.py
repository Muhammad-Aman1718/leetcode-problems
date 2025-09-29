# Find Words That Can Be Formed by Characters

# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
# Return the sum of lengths of all good strings in words.


# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:

        result = 0
        char_count = Counter(chars)
        for word in words:
            word_count = Counter(word)
            if all(word_count[char] <= char_count[char] for char in word):
                result += len(word)
        return result


obj = Solution()
words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(obj.countCharacters(words, chars))
