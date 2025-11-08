# Decrypt String from Alphabet to Integer Mapping

# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.


# Example 1:

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

# Example 2:

# Input: s = "1326#"
# Output: "acz"


class Solution:
    def freqAlphabets(self, s: str) -> str:

        i = 0
        result = ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                num = int(s[i : i + 2])
                result += chr(num + 96)
                i += 3
            else:
                num = int(s[i])
                result += chr(num + 96)
                i += 1

        return result


obj = Solution()
s = "10#11#12"
print(obj.freqAlphabets(s))
