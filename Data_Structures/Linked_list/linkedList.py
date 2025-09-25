# Linked List Implementation in Python

# Singly Linked List


class Node:  # Node Class
    def __init__(self, data: "str | int  | list[int]"):
        self.data = data
        self.next: "Node | None" = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1


def printNodes(head: Node):  # Function to print the linked list
    curr = head
    while curr:
        print(curr.data, end="-> ")
        curr = curr.next
    print(None)


printNodes(head)

# Add Node in first

newNodeFirst = Node(0)

newNodeFirst.next = head
head = newNodeFirst
printNodes(head)

#  Add Node in last

newNodeLast = Node(6)
curr = head
while curr.next != None:
    curr = curr.next

curr.next = newNodeLast

printNodes(head)


#  Add Node in kth index

k = 3
newNodeMiddle = Node(3)
curr = head
for i in range(k - 1):
    curr = curr.next

newNodeMiddle.next = curr.next
curr.next = newNodeMiddle
printNodes(head)


#  Remove Node in first

head = head.next
printNodes(head)


# Remove Node in last

curr = head
while curr.next.next != None:
    curr = curr.next
curr.next = None
printNodes(head)


# Remove Node in kth index

k = 2
curr = head
for i in range(k - 1):
    curr = curr.next
curr.next = curr.next.next
printNodes(head)


# Doubly Linked List


class DNode:  # Node Class
    def __init__(self, data: "str | int  | list[int]"):
        self.data = data
        self.next: "DNode | None" = None
        self.prev: "DNode | None" = None


dNode1 = DNode(10)
dNode2 = DNode(20)
dNode3 = DNode(30)
dNode4 = DNode(40)
dNode5 = DNode(50)


dNode1.next = dNode2
dNode2.prev = dNode1
dNode2.next = dNode3
dNode3.prev = dNode2
dNode3.next = dNode4
dNode4.prev = dNode3
dNode4.next = dNode5
dNode5.prev = dNode4

dHead = dNode1




# Curcular Linked List


class CNode:  # Node Class
    def __init__(self, data: "str | int  | list[int]"):
        self.data = data
        self.next: "CNode | None" = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1  # Making it circular
head = node1


def printCNodes(head: CNode):  # Function to print the linked list
    curr = head
    if head is not None:
        while True:
            print(curr.data, end="-> ")
            curr = curr.next
            if curr == head:
                break
    print("(head)")


printCNodes(head)
