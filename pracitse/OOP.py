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


# Node class
# class Node:
#     def __init__(self, data):
#         self.data = data  # value store karta hai
#         self.next = None  # next node ka reference


# # LinkedList class
# class LinkedList:
#     def __init__(self):
#         self.head = None  # starting node

#     # insert at end
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:  # last tak jao
#             current = current.next
#         current.next = new_node

#     # print linked list
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")


# # Test
# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.display()


# num = 10
# num2 = 40
# print(num)
# print(id(num))
# num = 20

# print(num)
# print(num2)
# print(id(num))
# print(id(num2))


# class Node:
#     def __init__(self, data: int) -> None:
#         print("this is constructor", data)
#         self.data = data
#         self.next = None


# a = Node(4)
# b = Node(5)
# c = Node(6)

# a.next = b
# b.next = c
# b.data = 10
# head = a
# print(head.data)
# print(head.next.data)


# num = 10
# print(id(num))
# num = 20
# print(id(num))
# num2 = []


# arr = [1, 2, 43, 4]
# print(id(arr))
# arr2 = arr
# arr2.append(49)
# print(id(arr))
# num = 12
# int *p = &num




