# class Solution:
#     def chocolates(self, s: str) -> str:
#         # code str
#         s: list[str] = list(s)
#         print(s)
#         left = 0
#         right = len(s) - 1

#         while left <= right:
#             if s[left] == " ":
#                 left += 1
#             elif s[right] == " ":
#                 right -= 1
#             else:
#                 s[right], s[left] = s[left], s[right]
#                 left += 1
#                 right -= 1

#         print(s)
#         return "".join(s)


# obj = Solution()
# s = "Help others"
# # s = "geeksforgeeks"
# print(obj.chocolates(s))


# class Car:
#     wheels = None

#     def __init__(self, wheel: int) -> None:
#         self.wheels = wheel


# car1 = Car(2)
# print(Car.wheels)
# print(car1.wheels)
