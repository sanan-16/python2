class Queue:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def size(self):
        return len(self.items)


my_queue = Queue()

print("Is the queue empty?", my_queue.is_empty())
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue size:", my_queue.size())

print("Dequeue:", my_queue.dequeue())
print("Queue size after dequeue:", my_queue.size())