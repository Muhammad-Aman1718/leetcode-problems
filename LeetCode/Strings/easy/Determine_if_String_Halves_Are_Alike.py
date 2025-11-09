# Determine if String Halves Are Alike

# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowelSet = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        # count = 0
        # for i in s:
        #     if i in vowelSet:
        #         count += 1

        # if count % 2 == 0:
        #     return True
        # else:
        #     return False

        countA = 0
        countB = 0
        for i in range(len(s)):
            if i < len(s) // 2:
                if s[i] in vowelSet:
                    countA += 1
            else:
                if s[i] in vowelSet:
                    countB += 1

        if countA == countB:
            return True
        else:
            return False


obj = Solution()
# s = "textbook"
s = "tkPAdxpMfJiltOerItiv"
print(obj.halvesAreAlike(s))
