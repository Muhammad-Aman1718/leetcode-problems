# Maximum Length Substring With Two Occurrences

# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.


# Example 1:

# Input: s = "bcbbbcba"
# Output: 4
# Explanation:
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

# Example 2:

# Input: s = "aaaa"
# Output: 2
# Explanation:
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".



class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = ii = 0 
        freq = Counter()
        for i, ch in enumerate(s): 
            freq[ch] += 1
            while freq[ch] == 3: 
                freq[s[ii]] -= 1
                ii += 1
            ans = max(ans, i-ii+1)
        return ans 
        
        
        
obj = Solution()
s = "bcbbbcba"
print(obj.maximumLengthSubstring(s))