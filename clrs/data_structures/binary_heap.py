import math

class BinaryHeap:

    size = 0

    def __init__(self, keys:list = [], max_size=10)->None:
        """
        Initialized the Max Heap
        In the heap, index 0 is not defined and is set to None
        After keys are initialized the heap is built
        
        Parameters
        ----------
        keys : list
            List of keys
       
        Returns
        -------
        None

        """

        self.max_size = max_size

        self.priority_queue = [None] * (self.max_size + 1)

        for key in keys:
            self.insert(key=key)

    def left(self, n:int)->int:
        """
        Returns the index of the left node in the heap
        
        Parameters
        ----------
        n : int
            None n
       
        Returns
        -------
        int

        """

        return n*2

    def right(self, n:int)->int:
        """
        Returns the index of the right node in the heap
        
        Parameters
        ----------
        n : int
            None n
       
        Returns
        -------
        int

        """

        return n*2+1

    def parent(self, n:int)->int:
        """
        Returns the index of the parent node in the heap
        
        Parameters
        ----------
        n : int
            None n
       
        Returns
        -------
        int

        """

        return n//2

    def get_new_top_idx(self, parent_idx : int, child_idx : int, verbose : bool=False)->int:
        """
        Yields the new top index given two indexes.
        Index 1 and index 2 is compared and index 1 is returned
        if condition og compare(parent_idx, child_idx) i satified, otherwise child_idx is returned
        
        Parameters
        ----------
        parent_idx : int
            Heap index
        child_idx : int
            Heap index
       
        Returns
        -------
        Int

        """
        
        if parent_idx > self.size and child_idx > self.size:
            raise ValueError(f'Index {parent_idx} and index {child_idx} outside of heap')
        elif child_idx > self.size:
            return parent_idx
        elif parent_idx > self.size:
            return child_idx

        if self.compare(parent_idx=parent_idx, child_idx=child_idx):
            top = parent_idx
        else:
            top = child_idx 
        
        if verbose:
            print(f'New top idx: {top}, value {self.priority_queue[top]}')

        return top

    def sink(self, n : int, verbose : bool=False)->None:
        """
        Heapifys a subtree. Given a binary subtree of 3 nodes, the new top node is found

        The following assumes an implementation of a Max Heap
        If the comparision function is implemented as "larger than", the largest key will
        be switched with the top key, unless the top key is the largest key
        Heapify works recursively top-to-bottom so after procesing one subtree, it moves down to where the largest of the sub nodes were located. 
        
        Parameters
        ----------
        n : int
            Heap index
        verbose : bool
            If true, debug print
       
        Returns
        -------
        Int

        """

        # If the heap is empty, it is already heapified
        if n > self.size:
            return None

        l = self.left(n)
        r = self.right(n)

        if verbose:
            self.print_node(n)
            
        # Should the current parent, left or right node be top?
        top = self.get_new_top_idx(parent_idx=n, child_idx=l, verbose=verbose)
        top = self.get_new_top_idx(parent_idx=top, child_idx=r, verbose=verbose)

        if top != n:
            self.switch_values(top, n)
            
            if verbose:
                print(f'Switching node {top}, value {self.priority_queue[top]} with node {n}, value {self.priority_queue[n]}. Keys = {self.get_keys()}, size = {self.size}')

            self.sink(top, verbose=verbose)

        return None


    def heapify(self, recursive : bool=True, verbose : bool=False)->None:
        """
        Heapify's a randomly ordered array.
        The function moves bottom-up and starts from size//2 to 1
        At each node, the subtree where the node is the top node sink is called recursively
        to make a node sink to where it belongs
        
        Parameters
        ----------
        recursive : bool
            If true, function runs recursively
        verbose : bool
            If true, debug print
       
        Returns
        -------
        Int

        """
        
        sub_node_range = list(range(1, self.size//2+1))[::-1]

        for m in sub_node_range:

            if recursive:
                self.sink(m)

    def is_heap(self):
        return self.is_heap_(1)

    def is_heap_(self, n : int, recursive : bool=True, verbose : bool=False)->bool:
        """
        Evaluates a heap. Returns true if the heap satisfies the heap conditions 
        
        Parameters
        ----------
        n : int
            Heap index
        recursive : bool
            If true, function runs recursively
        verbose : bool
            If true, debug print
       
        Returns
        -------
        Int

        """

        l = self.left(n)
        r = self.right(n)
        
        if verbose:
            print(f'Is-heap')
            self.print_node(n)

        # If Node n is the top compared to the left node and compared to the right node
        # the heap condition i satisfied
        is_heap = (n == self.get_new_top_idx(n, l) and n == self.get_new_top_idx(n, r))
        if is_heap is False:
            return False
        
        if recursive:
            if l <= self.size:
                l_heap = self.is_heap_(l)
            else:
                l_heap = True
            if r <= self.size:
                r_heap = self.is_heap_(r)
            else:
                r_heap = True

            return l_heap and r_heap

        return True

    def switch_values(self, idx_1 : int, idx_2 : int)->None:
        """
        Values of index 1 and index 2 is switched for keys
        
        Parameters
        ----------
        idx_1 : int
            Heap index
        idx_1 : int
            Heap index
       
        Returns
        -------
        None

        """

        self.switch_priority_queue(idx_1=idx_1, idx_2=idx_2)

    def switch_priority_queue(self, idx_1 : int, idx_2 : int)->None:
        """
        Key value of index 1 and index 2 is switched 
        
        Parameters
        ----------
        idx_1 : int
            Heap index
        idx_1 : int
            Heap index
       
        Returns
        -------
        None

        """

        value_idx_1 = self.priority_queue[idx_1]
        self.priority_queue[idx_1] = self.priority_queue[idx_2]
        self.priority_queue[idx_2] = value_idx_1

    def increase_key(self, index : int, new_key : int, verbose : bool=False)->None:
        """
        Increase key value of key
        
        Parameters
        ----------
        index : int
            Key index
        new_key : int
            New key
        verbose : bool
            If true, debug print
       
        Returns
        -------
        None

        """

        if self.priority_queue[index] is None:
            raise ValueError(f'No key found at index {index}')

        if self.priority_queue[index] > new_key:
            raise ValueError(f'New key {new_key} smaller than existing key {self.priority_queue[index]} for index {index}')

        self.priority_queue[index] = new_key

        if verbose:
            print(f'Set key index {index} to {new_key}')

        self.swim(i = index)

    def swim(self, i, verbose=False):

        # The value keys[i] may be larger than or equal to the old one
        # It might need to be moved up, keep switching parent with current value
        # while parent key is larger

        while i > 1 and i <= self.size and self.compare(parent_idx=self.parent(i), child_idx=i) == False:
            
            if verbose:
                print(f'Switched values for index {i}, value {self.priority_queue[i]} and index {self.parent(i)}, value {self.priority_queue[self.parent(i)]}')
            
            self.switch_values(self.parent(i) , i)
            
            i = self.parent(i)


    def insert(self, key : int, verbose : bool=False)->None:
        """
        Increase key value of hanldle
        
        Parameters
        ----------
        key : Any
            Comparable key
        verbose : bool
            If true, debug print
       
        Returns
        -------
        None

        """

        self.size += 1
        self.priority_queue[self.size] = key

        #self.print()
        
        self.swim(i=self.size)
        print(f'Inserted key: {key} at index {self.size}. Priority Queue: {self.priority_queue}')

    def extract_top(self, verbose : bool=False):
        """
        Extracts top node of the heap.
        This is done by exchanging top node with last node and then recursively call sink on the node
        to let it sink to it's final position.
        
        Parameters
        ----------
        verbose : bool
            If true, debug print
       
        Returns
        -------
        Top key

        """

        if self.size < 1:
            return None

        # Switch max and last index
        self.switch_values(1, self.size)

        top_key = self.priority_queue[self.size]
      
        # Decrease size
        self.priority_queue = self.priority_queue[:self.size]
        self.size = self.size - 1

        if verbose:
            print(f'Extracted key {top_key}, keys left: {self.get_keys()}, size: {self.size}')

        # Sink first index if it exits
        self.sink(1)

        return top_key

    def get_keys(self)->None:
        return self.priority_queue[1:self.size+1]

    def print(self)->None:
        print(f'Heap keys: {self.get_keys()}')

    def print_node(self, n : int)->None:

        l = self.left(n)
        r = self.right(n)
        
        if l > self.size:
            l_val = None
        else:
            l_val = self.priority_queue[l]

        if r > self.size:
            r_val = None
        else:
            r_val = self.priority_queue[r]

        print(f'Node {n}, value {self.priority_queue[n]}, left node {l}, value {l_val}, right node {r}, value {r_val}, size = {self.size}')

    def sort(self)->None:
        """
        Sorts heap by extracting top node until no more nodes exists in the heap

        Parameters
        ----------
        None
       
        Returns
        -------
        None

        """

        keys_sorted = []

        while self.size > 0:
            key_top = self.extract_top()
            keys_sorted += [key_top]
          
        self.size = len(keys_sorted)
        self.priority_queue = [None] + keys_sorted

    def is_sorted(self)->bool:
        """
        Returns true if heap keys are sorted

        Parameters
        ----------
        None
       
        Returns
        -------
        Bool

        """

        for n in range(1, self.size-1):
            if self.compare(parent_idx=n, child_idx=n+1) is False:
                return False
        return True

class IndexBinaryHeap(BinaryHeap):

    def __init__(self, indexes : list = [], keys:list = [], max_size=10)->None:
        """
        Initialized the Max Heap
        In the heap, index 0 is not defined and is set to None
        After keys are initialized the heap is built
        
        Parameters
        ----------
        keys : list
            List of keys
       
        Returns
        -------
        None

        """

        self.max_size = max_size

        self.indexes = [None] * (self.max_size + 1)
        self.inverse_indexes = [None] * (self.max_size + 1)
        self.keys = [None] * (self.max_size + 1)

        print(f'Init: keys = {self.keys}')

        for key, index in zip(keys, indexes):
            self.insert(index=index, key=key)

    def insert(self, index : int, key : int, verbose : bool=False)->None:
        """
        Increase key value of hanldle
        
        Parameters
        ----------
        key : Any
            Comparable key
        verbose : bool
            If true, debug print
       
        Returns
        -------
        None

        """

        # Let priority queue hold the indexes to the keys, and let inverse priority queue be inverse of priority queue
        # such that priority_queue[inverse_priority_queue[i]] = i

        self.size += 1
        
        print(f'Insert index {index}, key {key}')

        self.inverse_indexes[index] = self.size
        self.indexes[self.size] = index

        self.keys[self.size] = key

        self.swim(i=self.size)

        print(f'Keys: {self.keys}, pq: {self.indexes}, qp: {self.inverse_indexes}')

    def change(self, index, key):

        # Find placement in priority queue for index
        index_idx = self.inverse_indexes[index]
        print(f'Overwriting index {index} with key {key}. Current priority queue index {index_idx}, key {self.keys[index_idx]}')
        self.keys[index_idx] = key

        self.swim(index_idx)
        self.sink(index_idx)

    def contains(self, index : int):
        return self.inverse_indexes[index] != None
    
    def upsert(self, index, key):

        if self.contains(index):
            self.change(index=index, key=key)
        else:
            self.insert(index=index, key=key)


    def switch_values(self, idx_1 : int, idx_2 : int)->None:
        """
        Values of index 1 and index 2 is switched 
        
        Parameters
        ----------
        idx_1 : int
            Heap index
        idx_1 : int
            Heap index
       
        Returns
        -------
        None

        """

        inverse_idx_1 = self.indexes[idx_1]
        inverse_idx_2 = self.indexes[idx_2]

        self.indexes = self.switch_array(idx_1=idx_1, 
                                                idx_2=idx_2, 
                                                arr=self.indexes)

        self.inverse_indexes = self.switch_array(idx_1=inverse_idx_1, 
                                                        idx_2=inverse_idx_2, 
                                                        arr=self.inverse_indexes)
        
        self.keys = self.switch_array(idx_1=idx_1, 
                                      idx_2=idx_2, 
                                      arr=self.keys)

    def switch_array(self, idx_1 : int, idx_2 : int, arr):
        """
        Index value of index 1 and index 2 in arr is switched 
        
        Parameters
        ----------
        idx_1 : int
            Heap index
        idx_1 : int
            Heap index
        arr : List
            List to swtich
       
        Returns
        -------
        None

        """

        value_idx_1 = arr[idx_1]
        arr[idx_1] = arr[idx_2]
        arr[idx_2] = value_idx_1

        return arr

    def switch_indexes(self, idx_1 : int, idx_2 : int)->None:
        """
        Index value of index 1 and index 2 is switched 
        
        Parameters
        ----------
        idx_1 : int
            Heap index
        idx_1 : int
            Heap index
       
        Returns
        -------
        None

        """

        value_idx_1 = self.indexes[idx_1]
        self.indexes[idx_1] = self.indexes[idx_2]
        self.indexes[idx_2] = value_idx_1

    def extract_top(self, verbose : bool=False):
        """
        Extracts top node of the heap.
        This is done by exchanging top node with last node and then recursively call sink on the node
        to let it sink to it's final position.
        
        Parameters
        ----------
        verbose : bool
            If true, debug print
       
        Returns
        -------
        Top key

        """

        if self.size < 1:
            return None

        # Switch max and last index
        self.switch_values(1, self.size)

        print(f'\nExctrating')

        
        print(f'Extract top: keys: {self.keys}, {self.indexes}, {self.inverse_indexes}')


        top_key = self.keys[self.size]
        top_index = self.indexes[self.size]
        
        print(f'Extracting top key: {top_key}, index: {top_index}')
      
        # Decrease size
        self.keys[self.size] = None
        self.indexes[self.size] = None
        self.inverse_indexes[self.size] = None
        self.size = self.size - 1

        if verbose:
            print(f'Extracted key {top_key}, keys left: {self.get_keys()}, size: {self.size}')

        # Sink first index if it exits
        self.sink(1)

        return top_key, top_index
        
    def sort(self)->list:
        """
        Sorts heap by extracting top node until no more nodes exists in the heap

        Parameters
        ----------
        None
       
        Returns
        -------
        None

        """

        keys_sorted = [None] * (self.max_size + 1)
        index_sorted = [None] * (self.max_size + 1)
        inverse_index_sorted = [None] * (self.max_size + 1)

        count = 1

        while self.size > 0:
            top_key, top_index = self.extract_top()

            keys_sorted[count] = top_key
            index_sorted[count] = top_index
            inverse_index_sorted[top_index] = count
            
            count += 1
          
        self.size = count - 1
        self.keys = keys_sorted
        self.indexes = index_sorted
        self.inverse_indexes = inverse_index_sorted
        


class MaxBinaryHeap(BinaryHeap):
    
    def compare(self, parent_idx : int, child_idx : int)->bool:
        """
        Compares the values of two indexes in the heap
        Returns True if parent key is larger than child key
        
        Parameters
        ----------
        parent_idx : int
            Heap index
        child_idx : int
            Heap index
       
        Returns
        -------
        Bool

        """
        
        #print(f'Comparing parent_idx: {parent_idx} value {self.priority_queue[parent_idx]} with child_idx: {child_idx} value {self.priority_queue[child_idx]}, {self.priority_queue[parent_idx] >= self.priority_queue[child_idx]}')
        if self.priority_queue[parent_idx] >= self.priority_queue[child_idx]:
            return True
        else:
            return False
        

class MinBinaryHeap(BinaryHeap):

    def compare(self, parent_idx : int, child_idx : int)->bool:
        if self.priority_queue[parent_idx] <= self.priority_queue[child_idx]:
            return True
        else:
            return False
        
class MinIndexBinaryHeap(IndexBinaryHeap):
    
    def compare(self, parent_idx : int, child_idx : int)->bool:
        if self.keys[parent_idx] <= self.keys[child_idx]:
            return True
        else:
            return False
        
class MaxIndexBinaryHeap(IndexBinaryHeap):
    
    def compare(self, parent_idx : int, child_idx : int)->bool:
        if self.keys[parent_idx] >= self.keys[child_idx]:
            return True
        else:
            return False

'''
keys = [4, 5, 3, 6, 8, 1, 23, 2, 7, 9]
indexes = [var + 1 for var in range(len(keys))]

keys = [(key, handle) for key, handle in zip(keys, keys)]
max_heap = MinIndexBinaryHeap(indexes=indexes, keys=keys, max_size=len(keys))

max_heap.sort()

print(max_heap.keys)

max_heap.change(index=1, key=(25,25))

print(max_heap.keys)

max_heap.sort()

print(max_heap.keys)
'''