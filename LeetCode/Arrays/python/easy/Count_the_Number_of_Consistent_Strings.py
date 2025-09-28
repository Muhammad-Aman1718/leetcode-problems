# Count the Number of Consistent Strings

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.


# Example 1:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# Example 2:

# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.

# Example 3:

# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:

        countConsistent = 0
        allowedSort = set(sorted(allowed))
        sortedArray: list[list[str]] = []
        for i in words:
            sortedArray.append(list(sorted(set(i))))
        print(sortedArray, "     this i")
        print("     this i", allowedSort)
        for i in sortedArray:
            print("this is           i ", i)
            check = True
            for n in i:
                if n not in allowedSort:
                    check = False
            if check:
                countConsistent += 1

        return countConsistent


obj = Solution()
# allowed = "ab"
# words = ["ad", "bd", "aaab", "baa", "badab"]
# allowed = "abc"
# words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
allowed = "cad"
words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
print(obj.countConsistentStrings(allowed, words))
