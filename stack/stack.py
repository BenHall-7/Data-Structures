"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# using arrays
"""
class Stack:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self) == 0:
            return None
        return self.storage.pop()
"""

# using LinkedList's

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if len(self) == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()

"""
3. with arrays, adding new elements is O(n) whereas with LinkedLists, it runs with constant time.
Removing elements is constant time in both cases, because we explicitly only remove from the end
of the array. Length is instant in both cases, the first case because arrays store length, the
second because insering or removing updates size
"""