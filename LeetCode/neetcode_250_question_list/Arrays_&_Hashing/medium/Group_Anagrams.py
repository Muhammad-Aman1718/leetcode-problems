# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        dictionary: dict[str, list[str]] = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(strs[i])

        result: list[list[str]] = []
        for n in dictionary:
            result.append(dictionary[n])

        return result


obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(obj.groupAnagrams(strs))
