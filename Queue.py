class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def __len__(self):
        return len(self.q)

    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)

    def dequeue(self):
        'remove and return item at front of queue'
        return self.q.pop(0)
