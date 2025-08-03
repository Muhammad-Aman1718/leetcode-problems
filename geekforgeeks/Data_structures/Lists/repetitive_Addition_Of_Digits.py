#  Repetitive Addition Of Digits


# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num >= 10:
#             print("While loop is started", num)
#             sum_digits = 0
#             print("sum_digits : ", sum_digits)
#             while num > 0:
#                 print("nested loop is started =====>")
#                 sum_digits += num % 10
#                 print("modulus =====> ", num % 10)
#                 num //= 10
#                 # print("floor division =====> ", num //= 10)
#             num = sum_digits
#         return num


# sol = Solution()

# n = 5674
# # print(len(n))
# print(sol.addDigits(n))

