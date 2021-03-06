# Course: CS261 - Data Structures
# Assignment 5
# Student: Ashley Owens
# Description: Uses a dynamic array to implement a min heap data structure. 


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *

class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining min heap structure.
        Args:
            node (object): item to be added to the heap
        """
        # Saves the index position of the new node.
        position = self.heap.length()
        self.heap.append(node)

        # Percolates node upwards to maintain min heap structure.
        self.trickle_up(position)
    
    def trickle_up(self, position: int) -> None:
        """
        Recursively swaps nodes as needed to maintain min heap structure.
        Args:
            position (int): node index position in the heap
        """
        # Stops recursion at 0th index.
        if position == 0:
           return

        # Index position of parent node.
        j = (position - 1) // 2

        # Obtains values for comparison.
        parent = self.heap.get_at_index(j)
        node = self.heap.get_at_index(position)
        
        # Swaps nodes if needed to maintain min heap structure.
        if node < parent:
            self.heap.swap(position, j)
            self.trickle_up(j)
        return

    def get_min(self) -> object:
        """
        Raises:
            MinHeapException: empty heap
        Returns:
            object: minimum object in the heap
        """
        if self.is_empty():
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes the minimum value from the heap and returns it.
        Utilizes a recursive helper method to maintain min heap structure.
        Raises:
            MinHeapException: for an empty heap
        Returns:
            object: the minimum value
        """
        if self.is_empty():
            raise MinHeapException
        
        # Swaps first and last elements, removing the smallest element.
        self.heap.swap(0, self.heap.length() - 1)
        min_val = self.heap.pop()

        # Percolates first element downward into min heap position.
        self.trickle_down(0)
        return min_val

    def trickle_down(self, parent) -> None:
        """
        Recursive helper method for maintaining min heap
        structure after removing root node.
        Args:
            parent (int): index of parent node
        """  
        # Calculates indices of child nodes.
        left = 2 * parent + 1
        right = 2 * parent + 2

        # Stops percolation at the end of the DA.
        if left >= (self.heap.length()) and right >= (self.heap.length()):
            return

        # Checks for a parent node with a single left child that's smaller. 
        if left == (self.heap.length() - 1) and right == (self.heap.length()):
            if self.heap.get_at_index(parent) > self.heap.get_at_index(left):
                self.heap.swap(parent, left)
            return

        # Calculates values of parent and chilren nodes.
        left_val = self.heap.get_at_index(left)
        right_val = self.heap.get_at_index(right)
        parent_val = self.heap.get_at_index(parent)

        # Swaps parent and child values.
        if parent_val > left_val or parent_val > right_val:

            if left_val < right_val:
                self.heap.swap(parent, left)
                self.trickle_down(left)
            else:
                self.heap.swap(parent, right)
                self.trickle_down(right)

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a dynamic array and builds a proper MinHeap object.
        Args:
            da (DynamicArray): DA object in any order
        """
        # Initializes the DA elements into a heap object.
        self.heap = DynamicArray()
        for i in range(da.length()):
            item = da.get_at_index(i)
            self.heap.append(item)

        # First non-leaf node.
        start = (self.heap.length() // 2) - 1

        # Iterates through half the array, ordering elements into min heap structure.
        for i in range(start, -1, -1):
            self.trickle_down(i)
        

# BASIC TESTING
if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)

    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)


    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # # da = DynamicArray([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
