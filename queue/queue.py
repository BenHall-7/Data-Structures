"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# using arrays
"""
class Queue:
    def __init__(self):
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self) == 0:
            return None
        return self.storage.pop(0)
"""

# using singly_linked_list's

"""
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
"""

"""
3. when implementing each, arrays may require more time to run each operation because
when adding elements, it may need to reallocate all elements. Removing elements requires
shifting potentially all elements too. LinkedLists, however, are faster for adding
because they don't need contiguous memory. Removing is also fast because we can re-assign
the head easily. We must keep track of size manually here because the LinkedList requires
iteration to find the last element, which is O(n)
"""

# for stretch, start with array-based stacks:
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

class Queue:
    def __init__(self):
        # 1st holds all the data
        # 2nd stores items while we "dig to the bottom" to dequeue
        self.storage = Stack()
        self.temporary_storage = Stack()
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.push(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        # length of all elements minus the one being dequeued
        size = len(self.storage) - 1
        # pop all except the last element, push into temporary storage
        for _ in range(size):
            top = self.storage.pop()
            self.temporary_storage.push(top)
        # get the final element, which would be the first one added
        ret = self.storage.pop()
        # now put them back
        for _ in range(size):
            bottom = self.temporary_storage.pop()
            self.storage.push(bottom)
        return ret
