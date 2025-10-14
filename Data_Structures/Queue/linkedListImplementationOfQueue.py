# Queue Implementation using Linked list
# Queue is a linear data structure that follows the FIFO (First In First Out) principle.

# operations:
# 1. Enqueue: Add an element to the end of the queue.
# 2. Dequeue: Remove the element from the front of the queue.
# 3. Front: Get the element at the front of the queue without removing it.
# 4. Rear: Get the element at the end of the queue without removing it.
# 5. isEmpty: Check if the queue is empty.
# 6. isFull: Check if the queue is full.
# 7. Size: Get the number of elements in the queue.


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.length = 0

    def add(self, x: int):
        self.length += 1
        newNode = Node(x)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def remove(self):
        if self.front is None:
            return -1
        self.length -= 1
        x = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return x

    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data

    def size(self):
        return self.length


queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
print(queue.remove())
print(queue.getFront())
