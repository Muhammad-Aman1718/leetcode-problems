# Reverse Words With Same Vowel Count

# You are given a string s consisting of lowercase English words, each separated by a single space.
# Determine how many vowels appear in the first word. Then, reverse each following word that has the same vowel count. Leave all remaining words unchanged.
# Return the resulting string.
# Vowels are 'a', 'e', 'i', 'o', and 'u'.


# Example 1:

# Input: s = "cat and mice"
# Output: "cat dna mice"
# Explanation:​​​​​​​
# The first word "cat" has 1 vowel.
# "and" has 1 vowel, so it is reversed to form "dna".
# "mice" has 2 vowels, so it remains unchanged.
# Thus, the resulting string is "cat dna mice".

# Example 2:

# Input: s = "book is nice"
# Output: "book is ecin"
# Explanation:
# The first word "book" has 2 vowels.
# "is" has 1 vowel, so it remains unchanged.
# "nice" has 2 vowels, so it is reversed to form "ecin".
# Thus, the resulting string is "book is ecin".
# Example 3:

# Input: s = "banana healthy"
# Output: "banana healthy"


class Solution:
    def reverseWords(self, s: str) -> str:

        # Brute Force

        # vowels = {"a", "e", "i", "o", "u"}
        # countVowels = {}
        # sArr = s.split()

        # for i in sArr:
        #     count = 0
        #     for n in i:
        #         if n in vowels:
        #             count += 1
        #     countVowels[i] = count

        # res = []
        # firstVowel = countVowels[sArr[0]]

        # for i in countVowels:
        #     if i != sArr[0]:
        #         if countVowels[i] == firstVowel:
        #             res.append(i[::-1])
        #             continue
        #     res.append(i)
        

        # return " ".join(res)


        # Optimize Solution 
        
        vowels = set("aeiou")
        words = s.split()
        
        # count vowels in first word
        first_vowel_count = sum(1 for ch in words[0] if ch in vowels)
        
        # process remaining words
        for i in range(1, len(words)):
            vowel_count = sum(1 for ch in words[i] if ch in vowels)
            if vowel_count == first_vowel_count:
                words[i] = words[i][::-1]
        
        return " ".join(words)




obj = Solution()
s = "cat and mice"
print(obj.reverseWords(s))
