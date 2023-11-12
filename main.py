class CircularQueue:
    def _init_(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Enqueue on a full queue")
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        removed_item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed_item

    def size(self):
        if self.is_empty():
            return 0
        elif self.is_full():
            return self.capacity
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.capacity - (self.front - self.rear - 1)


cq = CircularQueue(5)

print("Is the circular queue empty?", cq.is_empty())

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)

print("Is the circular queue full?", cq.is_full())
print("Circular queue size:", cq.size())

print("Dequeue:", cq.dequeue())
print("Circular queue size after dequeue:", cq.size())