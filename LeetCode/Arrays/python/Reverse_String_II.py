# Reverse String II


# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.


# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"


class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        def chunk_string(text: str, size: int):
            return [text[i : i + size] for i in range(0, len(text), size)]

        chunks = chunk_string(s, 2 * k)

        for i in range(len(chunks)):
            if len(chunks[i]) < k:
                # case 1: fewer than k chars → reverse all
                chunks[i] = chunks[i][::-1]
            else:
                # case 2: >= k chars → reverse first k, leave the rest
                chunks[i] = chunks[i][:k][::-1] + chunks[i][k:]

        return "".join(chunks)


obj = Solution()
s = "abcdefg"
k = 2
print(obj.reverseStr(s, k))
