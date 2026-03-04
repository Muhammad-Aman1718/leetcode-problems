# Special Positions in a Binary Matrix

# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).


# Example 1:

# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

# Example 2:

# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:

        rows = len(mat)
        cols = len(mat[0])

        row_count = [0] * rows
        col_count = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1 

        special_positions = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    # Agar row aur col dono mein sirf yehi ek '1' hai
                    if row_count[r] == 1 and col_count[c] == 1:
                        special_positions += 1

        return special_positions


obj = Solution()
# mat = [[1,0,0],[0,1,0],[0,0,1]]
# mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
mat = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(obj.numSpecial(mat))
