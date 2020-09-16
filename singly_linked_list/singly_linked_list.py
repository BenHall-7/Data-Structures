class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next_node = self.head
            self.head = new

    def add_to_tail(self, value):
        new = Node(value)
        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next_node = new
            self.tail = new

    def remove_head(self):
        if self.head is None:
            return None
        
        ret = self.head.value
        # check if the list has only 1 element
        # because then we need to update the tail too
        if self.head.next_node is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
        return ret

    def remove_tail(self):
        if self.tail is None:
            return None
        ret = self.tail.value
        # same logic as in remove_head
        if self.head.next_node is None:
            self.head = None
            self.tail = None
        else:
            current = self.head
            tail_prev = None
            while current is not None:
                if current.next_node == self.tail:
                    tail_prev = current
                    break
                current = current.next_node
            
            if tail_prev is None:
                raise Exception("Tail pointed to un-linked node")

            tail_prev.next_node = None
            self.tail = tail_prev
        return ret

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next_node
        return False

    def get_max(self):
        maximum = None
        current = self.head
        while current is not None:
            if maximum is None or current.value > maximum:
                maximum = current.value
        return maximum