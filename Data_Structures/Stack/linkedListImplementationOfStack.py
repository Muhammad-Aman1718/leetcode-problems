# Linked List Implementation Of Stack

# Stack is a linear data structure that follows the LIFO (Last In First Out) principle.

# operations:
# 1. Push: Add an element to the top of the stack.
# 2. Pop: Remove the element from the top of the stack.
# 3. Peek: Get the element at the top of the stack without removing it.
# 4. isEmpty: Check if the stack is empty.
# 5. isFull: Check if the stack is full.
# 6. Size: Get the number of elements in the stack.


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.lenght = 0

    def add(self, data: int):
        self.lenght += 1
        if self.top is None:
            self.top = Node(data)
            return
        else:
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode

    def remove(self):
        if self.top == None:
            return -1
        self.lenght -= 1
        x = self.top.data
        self.top = self.top.next
        return x

    def getData(self):
        if self.top == None:
            return -1
        return self.top.data

    def size(self):
        return self.lenght


stack = Stack()

stack.add(2)
stack.add(3)
stack.add(4)
stack.add(5)
print(stack.lenght)
print(stack.getData())
print(stack.remove())
print(stack.getData())
