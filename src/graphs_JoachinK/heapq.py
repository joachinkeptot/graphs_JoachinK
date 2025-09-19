"""
Min-heap implementation for Dijkstra's algorithm.
"""

class MinHeap:
    """
    A min-heap implementation that maintains the heap property where
    the parent is always smaller than its children.
    """
    
    def __init__(self):
        """Initialize an empty heap."""
        self.heap = []
    
    def push(self, item):
        """
        Add an item to the heap and maintain heap property.
        
        Args:
            item: A tuple (priority, value) where priority is used for comparison
        """
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        """
        Remove and return the smallest item from the heap.
        
        Returns:
            The smallest item in the heap, or None if heap is empty
        """
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store the root (minimum element)
        root = self.heap[0]
        
        # Move the last element to the root and remove the last element
        self.heap[0] = self.heap.pop()
        
        # Restore heap property
        self._heapify_down(0)
        
        return root
    
    def empty(self):
        """
        Check if the heap is empty.
        
        Returns:
            True if heap is empty, False otherwise
        """
        return len(self.heap) == 0
    
    def size(self):
        """
        Get the number of items in the heap.
        
        Returns:
            Number of items in the heap
        """
        return len(self.heap)
    
    def _heapify_up(self, index):
        """
        Move an element up the heap until heap property is satisfied.
        
        Args:
            index: Index of the element to move up
        """
        parent_index = (index - 1) // 2
        
        # If we're at the root or heap property is satisfied, stop
        if index == 0 or self.heap[parent_index] <= self.heap[index]:
            return
        
        # Swap with parent
        self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
        
        # Continue heapifying up
        self._heapify_up(parent_index)
    
    def _heapify_down(self, index):
        """
        Move an element down the heap until heap property is satisfied.
        
        Args:
            index: Index of the element to move down
        """
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index
        
        # Find the smallest among parent and children
        if (left_child < len(self.heap) and 
            self.heap[left_child] < self.heap[smallest]):
            smallest = left_child
        
        if (right_child < len(self.heap) and 
            self.heap[right_child] < self.heap[smallest]):
            smallest = right_child
        
        # If the smallest is not the parent, swap and continue
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)