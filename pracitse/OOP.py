class Node:
    def __init__(self, data: int):
        print("this is constructor    ", data)
        self.data = data
        self.next: "Node | None" = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1


def printLinkedList(head: Node):
    curr = head

    while curr:
        print(curr.data, end="->")
        curr = curr.next
    print(None)


printLinkedList(head)


newNode = Node(0)
newNode.next = head
head = newNode
printLinkedList(head)

lastNode = Node(7)
curr = head
while curr.next != None:
    curr = curr.next
curr.next = lastNode

printLinkedList(head)
