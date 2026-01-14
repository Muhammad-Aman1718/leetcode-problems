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
        
        vowels_set = set("aeiouAEIOU")

        # Word ke vowels count karne ka function
        def count_vowels(word):
            return sum(1 for char in word if char in vowels_set)

        words = s.split()
        L, R = 0, len(words) - 1

        while L < R:
            count_L = count_vowels(words[L])
            count_R = count_vowels(words[R])

            if count_L == count_R:
                # Agar vowel count barabar hai to swap karein
                words[L], words[R] = words[R], words[L]
                L += 1
                R -= 1
            else:
                # Yeh step problem ki specific condition par depend karta hai
                # Agar sirf barabar count wale swap karne hain aur baaki nahi
                # To humein decide karna hoga ke kis pointer ko move karna hai
                # Note: Usually aisi problems mein nested loops use hote hain 
                # sahi pair dhundne ke liye.
                L += 1 

        return " ".join(words)




obj = Solution()
s = "cat and mice"
print(obj.reverseWords(s))
