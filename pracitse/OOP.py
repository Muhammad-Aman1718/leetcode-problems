class Solution:
    def is_possible_to_get_seats(self, n: int, m: int, seats: list[int]) -> bool:
        # code here
        for i in range(m):
            if (
                seats[i] == 0
                and (i == 0 or seats[i - 1] == 0)
                and (i == m - 1 or seats[i + 1] == 0)
            ):
                seats[i] = 1  # ✅ mark seat as occupied
                n -= 1
                if n == 0:  # ✅ early stop if all seated
                    return True

        return n <= 0


obj = Solution()
n = 2
m = 7
seats = [0, 0, 1, 0, 0, 0, 1]
# n = 1
# m = 3
# seats = [0, 1, 0]
n = 2
m = 2
seats = [0, 0]
print(obj.is_possible_to_get_seats(n, m, seats))
