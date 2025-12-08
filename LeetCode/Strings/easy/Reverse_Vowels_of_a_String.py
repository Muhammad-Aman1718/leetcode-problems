# Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:

# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"


class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        string = list(s)
        lp, rp = 0, len(string) - 1

        while lp < rp:
            # Move left pointer until vowel found
            while lp < rp and string[lp] not in vowels:
                lp += 1

            # Move right pointer until vowel found
            while lp < rp and string[rp] not in vowels:
                rp -= 1

            # Now both are vowels → swap
            string[lp], string[rp] = string[rp], string[lp]
            lp += 1
            rp -= 1

        return "".join(string)


obj = Solution()
s = "IceCreAm"
print(obj.reverseVowels(s))
