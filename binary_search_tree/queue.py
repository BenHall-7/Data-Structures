
# using singly_linked_list's

from singly_linked_list import LinkedList
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if len(self) == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()
