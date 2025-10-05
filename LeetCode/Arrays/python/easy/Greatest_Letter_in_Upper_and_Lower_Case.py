# Greatest English Letter in Upper and Lower Case

# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

# An English letter b is greater than another letter a if b appears after a in the English alphabet.


# Example 1:

# Input: s = "lEeTcOdE"
# Output: "E"
# Explanation:
# The letter 'E' is the only letter to appear in both lower and upper case.

# Example 2:

# Input: s = "arRAzFif"
# Output: "R"
# Explanation:
# The letter 'R' is the greatest letter to appear in both lower and upper case.
# Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

# Example 3:

# Input: s = "AbCdEfGhIjK"
# Output: ""
# Explanation:
# There is no letter that appears in both lower and upper case.


class Solution:
    def greatestLetter(self, s: str) -> str:

        lower_set: set[str] = set()

        upper_set: set[str] = set()

        for ch in s:
            if ch.islower():
                lower_set.add(ch)
            else:
                upper_set.add(ch)

        common: list[str] = []
        for ch in upper_set:
            if ch.lower() in lower_set:
                common.append(ch)

        return max(common) if common else ""


obj = Solution()
# s = "lEeTcOdE"
# s = "arRAzFif"
s = "nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM"
print(obj.greatestLetter(s))
