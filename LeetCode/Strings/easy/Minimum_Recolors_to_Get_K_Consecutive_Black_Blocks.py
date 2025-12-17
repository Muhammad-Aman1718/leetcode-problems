# Minimum Recolors to Get K Consecutive Black Blocks

# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.


# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW".
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # Self solving

        # count = float("inf")
        # left = 0
        # right = k

        # while right != len(blocks) + 1:

        #     number = blocks[left:right].count("W")
        #     count = min(count, number)
        #     right += 1
        #     left += 1

        # return count

        current_white_count = 0
        for i in range(k):
            if blocks[i] == "W":
                current_white_count += 1

        min_recolors = current_white_count
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                current_white_count += 1
            if blocks[i - k] == "W":
                current_white_count -= 1
            min_recolors = min(min_recolors, current_white_count)

        return min_recolors


obj = Solution()
blocks = "WBBWWBBWBW"
k = 7
print(obj.minimumRecolors(blocks, k))
