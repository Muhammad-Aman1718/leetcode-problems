# # class Solution:

# #     # Default Constructor
# #     # def __init__(self) -> None:
# #     #     print("this is constructor ----> ")

# #     # parameterized Constructor    # is ki priority zayda hoti ha
# #     def __init__(self, name: str, marks: list[int]) -> None:
# #         self.name = name
# #         self.marks = marks
# #         print("this is parameterized constructor ----> ")

# #     def average():


# # obj = Solution()
# # # print(obj.aman("aman", 34))
# # # print(obj.aman)

# # # arr = [111, 222, 333, 444, 555]
# # # print(obj.check_elements(arr))


# class Solution:
#     def getOddOccurrence(self, arr, x, y):
#         # code here

#         freq: dict[int, int] = {}

#         for i in arr:
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1

#         for i in freq:
#             if freq[x] > freq[y]:
#                 return x
#             elif freq[y] > freq[x]:
#                 return y
#             elif freq[x] == freq[y]:
#                 return min(x, y)


# obj = Solution()
# # arr = [1, 2, 3, 2, 3, 1, 3]
# # arr = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]
# arr = [4]
# x = 2
# y = 1
# print(obj.getOddOccurrence(arr, x, y))


# class Student:
#     total_students = 0  # Class variable

#     def __init__(self, name):
#         self.name = name
#         Student.total_students += 1

#     @classmethod
#     def get_total_students(cls):  # Class method
#         return cls.total_students


# student1 = Student("Ali")
# student2 = Student("Sara")
# print(Student.get_total_students())  # Output: 2
