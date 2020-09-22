"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        cur = self
        while True:
            if value >= cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = BSTNode(value)
                    break
            else: # value < cur.value
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = BSTNode(value)
                    break

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur = self
        while True:
            if target > cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    return False
            elif target < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    return False
            else: # equals
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        ret = self.value
        cur = self.right
        while cur:
            if cur.value > ret:
                ret = cur.value
            cur = cur.right
        
        return ret

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # left first (least)
        if self.left:
            self.left.in_order_print()
        # then current node (greater than left)
        # every print happens here because all nodes are iterated
        print(self.value)
        # right last (greater than both)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)
        while True:
            if len(queue) == 0:
                break

            for _ in range(len(queue)):
                node = queue.dequeue()
                print(node.value)
                queue.enqueue(node.left)
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        print(self.value)
        self.left.dft_print()
        self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
