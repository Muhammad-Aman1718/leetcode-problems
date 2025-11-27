class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: "Node | None" = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


def PrintNodes(head: Node):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# Add new node in first
node0 = Node(0)
node0.next = head
head = node0


#  Add last node in the end
lastNode = Node(5)

curr = head

while curr.next != None:
    curr = curr.next

curr.next = lastNode


PrintNodes(head)