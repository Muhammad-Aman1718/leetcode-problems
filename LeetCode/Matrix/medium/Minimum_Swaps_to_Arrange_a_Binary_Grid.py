# Minimum Swaps to Arrange a Binary Grid

# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

# A grid is said to be valid if all the cells above the main diagonal are zeros.

# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).


# Example 1:


# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3

# Example 2:


# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.

# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0


class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:

        countTrialingZero = []
        n = len(grid)

        for i in grid:
            countZero = 0
            for j in range(len(i) - 1, -1, -1):

                if i[j] == 0:
                    countZero += 1
                else:
                    break
            countTrialingZero.append(countZero)
        ans = 0
        # 2. Main Logic
        for i in range(n):
            target = n - 1 - i
            # Sahi row dhoondne ke liye loop
            for j in range(i, n):
                if countTrialingZero[j] >= target:
                    # Jitni doori par hai, utne hi swaps honge
                    ans += j - i
                    # Row ko utha kar sahi jagah shift kar do
                    row_val = countTrialingZero.pop(j)
                    countTrialingZero.insert(i, row_val)
                    break
            else:
                # Agar poora loop khatam ho jaye aur break na ho (yaani row nahi mili)
                return -1

        return ans


obj = Solution()
grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
print(obj.minSwaps(grid))
