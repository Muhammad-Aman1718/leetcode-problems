# class Solution:
#     def is_possible_to_get_seats(self, arr: list[int]) -> bool:
#         # code here
#         result = []
#         freq: dict[int, int] = {}
#         for i in arr:
#             freq[i] = freq.get(i, 0) + 1
#         print(freq)
#         t = max(freq.values())
#         print(t)
#         for i in freq:
#             if freq[i] == t:
#                 result.append(i)
#         return min(result)


# obj = Solution()
# seats = [2, 2, 1, 1, 0, 0, ]

# print(obj.is_possible_to_get_seats(seats))


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1
curr = head


def printNode(head: Node):
    curr = head
    while curr:
        print(curr.data, end="-> ")
        curr = curr.next

    print("None")


# newNode = Node(0)
# newNode.next = head
# head = newNode
# printNode(head)

# curr = head
# prev = None
# nxt = None
# while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt

# printNode(prev)

# elements = []
# count = 0
# curr = head
# while curr:
#     elements.append(curr.data)
#     count += curr.data
#     curr = curr.next
# print(elements)
# print(count)




