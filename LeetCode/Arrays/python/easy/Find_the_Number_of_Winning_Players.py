# Find the Number of Winning Players

# You are given an integer n representing the number of players in a game and a 2D array pick where pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.

# Player i wins the game if they pick strictly more than i balls of the same color. In other words,

# Player 0 wins if they pick any ball.
# Player 1 wins if they pick at least two balls of the same color.
# ...
# Player i wins if they pick at least i + 1 balls of the same color.
# Return the number of players who win the game.

# Note that multiple players can win the game.


# Example 1:

# Input: n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
# Output: 2
# Explanation:
# Player 0 and player 1 win the game, while players 2 and 3 do not win.

# Example 2:

# Input: n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]
# Output: 0
# Explanation:
# No player wins the game.

# Example 3:

# Input: n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]
# Output: 1
# Explanation:
# Player 2 wins the game by picking 3 balls with color 4.


class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:

        res = 0
        seen: set[int] = set()
        players = [[0] * 11 for _ in range(n)]
        for x, y in pick:
            if players[x][y] == x and x not in seen:
                res += 1
                seen.add(x)
            players[x][y] += 1
        return res


obj = Solution()
# n = 4
# pick = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]
n = 5
pick = [[1, 1], [2, 4], [2, 4], [2, 4]]
print(obj.winningPlayerCount(n, pick))
