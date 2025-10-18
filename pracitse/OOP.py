# # class Solution:
# #     def is_possible_to_get_seats(self, arr: list[int]) -> bool:
# #         # code here
# #         result = []
# #         freq: dict[int, int] = {}
# #         for i in arr:
# #             freq[i] = freq.get(i, 0) + 1
# #         print(freq)
# #         t = max(freq.values())
# #         print(t)
# #         for i in freq:
# #             if freq[i] == t:
# #                 result.append(i)
# #         return min(result)


# # obj = Solution()
# # seats = [2, 2, 1, 1, 0, 0, ]

# # print(obj.is_possible_to_get_seats(seats))


# class Node:
#     def __init__(self, data: int) -> None:
#         self.data = data
#         self.next = None


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# # Linked List 2

# node10 = Node(1)
# node11 = Node(2)
# node12 = Node(3)
# node13 = Node(4)
# node14 = Node(5)

# node10.next = node11
# node11.next = node12
# node12.next = node13
# node13.next = node14


# def printNode(head: Node):
#     curr = head
#     while curr:
#         print(curr.data, end="-> ")
#         curr = curr.next

#     print("None")


# # newNode = Node(0)
# # newNode.next = head
# # head = newNode
# # printNode(head)

# # curr = head
# # prev = None
# # nxt = None
# # while curr:
# #     nxt = curr.next
# #     curr.next = prev
# #     prev = curr
# #     curr = nxt

# # printNode(head)

# # elements = []
# # count = 0
# # curr = head
# # while curr:
# #     elements.append(curr.data)
# #     count += curr.data
# #     curr = curr.next
# # print(elements)
# # print(count)

# head1 = node1
# head10 = node10
# curr10 = head10
# curr1 = head1
# # printNode(head)
# newNodeList = Node(0)
# dummy = newNodeList
# tail = dummy
# while curr1 and curr10:
#     if curr1.data <= curr10.data:
#         tail.next = curr1
#         curr1 = curr1.next
#     else:
#         tail.next = curr10
#         curr10 = curr10.next
#     tail = tail.next

# if node1:
#     tail.next = curr1
# else:
#     tail.next = curr10

# printNode(dummy.next)


# def printN(n: int) -> int:
#     if n == 0:
#         return 0

#     printN(n - 1)
#     print(n, end=" ")


# printN(5)


a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)
