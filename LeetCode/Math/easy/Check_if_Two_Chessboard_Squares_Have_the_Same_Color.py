# Check if Two Chessboard Squares Have the Same Color

# You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8 chessboard.

# Below is the chessboard for reference.


# Return true if these two squares have the same color and false otherwise.

# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).


# Example 1:

# Input: coordinate1 = "a1", coordinate2 = "c3"
# Output: true
# Explanation:
# Both squares are black.

# Example 2:

# Input: coordinate1 = "a1", coordinate2 = "h3"
# Output: false
# Explanation:
# Square "a1" is black and "h3" is white.


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        def color_value(coord: str):
            col = ord(coord[0]) - ord("a") + 1
            row = int(coord[1])
            return (col + row) % 2  # 0 = black, 1 = white

        return color_value(coordinate1) == color_value(coordinate2)


obj = Solution()
coordinate1 = "a1"
coordinate2 = "c3"
print(obj.checkTwoChessboards(coordinate1, coordinate2))
