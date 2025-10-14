# Queue Implementation using list
# Queue is a linear data structure that follows the FIFO (First In First Out) principle.

# operations:
# 1. Enqueue: Add an element to the end of the queue.
# 2. Dequeue: Remove the element from the front of the queue.
# 3. Front: Get the element at the front of the queue without removing it.
# 4. Rear: Get the element at the end of the queue without removing it.
# 5. isEmpty: Check if the queue is empty.
# 6. isFull: Check if the queue is full.
# 7. Size: Get the number of elements in the queue.


class Queue:
    def __init__(self) -> None:
        self.q: list[int] = []
        self.front = -1

    def add(self, data: int):
        if self.front == -1:
            self.front = 0
        self.q.append(data)

    def remove(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x

    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front


queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
queue.remove()
queue.remove()
print(queue.q)
print(queue.getFront())
print(queue.size())
