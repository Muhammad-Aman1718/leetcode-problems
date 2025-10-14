# Stack Implementation using list
# Stack is a linear data structure that follows the LIFO (Last In First Out) principle.

# operations:
# 1. Push: Add an element to the top of the stack.
# 2. Pop: Remove the element from the top of the stack.
# 3. Peek: Get the element at the top of the stack without removing it.
# 4. isEmpty: Check if the stack is empty.
# 5. isFull: Check if the stack is full.
# 6. Size: Get the number of elements in the stack.


class Stack:
    def __init__(self) -> None:
        self.data: list[int] = []
        self.length = 5

    def add(self, data: int):
        if self.length == len(self.data):
            return "The length of the list is full"
        self.data.append(data)

    def remove(self):
        self.data.pop()

    def getElement(self) -> int:  # Peek Element
        return self.data[-1]

    def isEmpty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def isFull(self):
        if self.length == len(self.data):
            return True
        return False

    def size(self):
        return len(self.data)

    def printList(self):
        print(self.data)


stack = Stack()
stack.add(2)
stack.add(3)
stack.add(4)
stack.add(5)
stack.add(6)
stack.add(8)
print(stack.add(8))
stack.printList()
# obj.remove()
# obj.remove()
# obj.remove()
# obj.remove()
# obj.remove()
stack.printList()
# print(obj.getElement())
print(stack.isEmpty())
print(stack.isFull())
print(stack.size())
