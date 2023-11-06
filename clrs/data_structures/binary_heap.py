import math

class BinaryHeap:

    def __init__(self, keys:list = [], handles = [])->None:
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

        if len(keys) != len(handles):
            raise ValueError(f'Length of keys {len(keys)} must equal lenght of handles {len(handles)}')

        self.size = len(keys)
        self.keys = [None] + keys
        self.handles = [None] + handles

        self.build_heap()

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
            print(f'New top idx: {top}, value {self.keys[top]}')

        return top

    def heapify(self, n : int, recursive : bool=True, verbose : bool=False)->None:
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
        recursive : bool
            If true, function runs recursively
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
            print(f'Max-heapify')
            self.print_node(n)
            
        top = self.get_new_top_idx(parent_idx=n, child_idx=l, verbose=verbose)
        top = self.get_new_top_idx(parent_idx=top, child_idx=r, verbose=verbose)

        if top != n:
            self.switch_values(top, n)
            
            if verbose:
                print(f'Switching node {top}, value {self.keys[top]} with node {n}, value {self.keys[n]}. Keys = {self.get_keys()}, size = {self.size}')

            if recursive:
                self.heapify(top, recursive=recursive, verbose=verbose)

        return None


    def build_heap(self, recursive : bool=True, verbose : bool=False)->None:
        """
        Builds a heap from a randomly ordered array.
        The function moves bottom-up and starts from size//2 to 1
        At each node, the subtree where the node is the top node heapify is called recursively
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
                self.heapify(m)

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

    def switch_handles(self, idx_1 : int, idx_2 : int)->None:
        """
        Handle value of index 1 and index 2 is switched 
        
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

        value_idx_1 = self.handles[idx_1]
        self.handles[idx_1] = self.handles[idx_2]
        self.handles[idx_2] = value_idx_1

    def switch_values(self, idx_1 : int, idx_2 : int)->None:
        """
        Values of index 1 and index 2 is switched for keys and handles
        
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

        self.switch_keys(idx_1=idx_1, idx_2=idx_2)
        self.switch_handles(idx_1=idx_1, idx_2=idx_2)

    def switch_keys(self, idx_1 : int, idx_2 : int)->None:
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

        value_idx_1 = self.keys[idx_1]
        self.keys[idx_1] = self.keys[idx_2]
        self.keys[idx_2] = value_idx_1

    def search_handle(self, handle)->int:
        """
        Increase key value of hanldle
        
        Parameters
        ----------
        handle : Any
            Handle
       
        Returns
        -------
        int : Handle index

        """

        # Naive search implementation
        handle_index = self.handles.index(handle)

        return handle_index

    def increase_key(self, handle, new_key : int, verbose : bool=False)->None:
        """
        Increase key value of hanldle
        
        Parameters
        ----------
        handle : Any
            Handle
        new_key : int
            Handle key
        verbose : bool
            If true, debug print
       
        Returns
        -------
        None

        """

        handle_index = self.search_handle(handle=handle)

        if self.keys[handle_index] > new_key:
            raise ValueError(f'New key {new_key} smaller than existing key {self.keys[handle_index]} for handle {handle}')

        i = handle_index

        self.keys[handle_index] = new_key

        if verbose:
            print(f'Set key index {handle_index} to {new_key}')

        # The new key value is larger than or equal to the old one
        # It might need to be moved up, keep switching parent with current value
        # while parent key is larger
        print(f'While: i = {i}, self.keys[self.parent(i)]: {self.keys[self.parent(i)]}, self.keys[i] = {self.keys[i]}')
        while i >= 1 and self.compare(parent_idx=self.parent(i), child_idx=i) == False:
            print(f'Switched values for index {i}, value {self.keys[i]} and index {self.parent(i)}, value {self.keys[self.parent(i)]}')
            self.switch_values(self.parent(i) , i)
            
            i = self.parent(i)

    def insert(self, handle, key : int, verbose : bool=False)->None:
        """
        Increase key value of hanldle
        
        Parameters
        ----------
        handle : Any
            Handle
        key : int
            Handle key
        verbose : bool
            If true, debug print
       
        Returns
        -------
        None

        """

        self.keys += [-math.inf]
        self.handles += [handle]
        self.size += 1

        self.print()

        self.increase_key(handle=handle, new_key=key)

    def extract_top(self, verbose : bool=False)->tuple:
        """
        Extracts top node of the heap.
        This is done by exchanging top node with last node and then recursicely call heapify on the node
        to let it sink to it's final position.
        
        Parameters
        ----------
        verbose : bool
            If true, debug print
       
        Returns
        -------
        None

        """

        if self.size < 1:
            return None

        # Switch max and last index
        self.switch_values(1, self.size)

        top_key = self.keys[self.size]
        top_val = self.handles[self.size]

        # Decrease size
        self.keys = self.keys[:self.size]
        self.handles = self.handles[:self.size]
        self.size = self.size - 1

        if verbose:
            print(f'Extracted key-handle pair {top_key}:{top_val}, keys left: {self.get_keys()}, size: {self.size}')

        # Max-heapify first index if it exits
        self.heapify(1)

        return top_key, top_val

    def get_keys(self)->None:
        return self.keys[1:self.size+1]

    def get_handles(self)->None:
        return self.handles[1:self.size+1]

    def print(self)->None:
        print(f'Heap keys: {self.get_keys()}')
        print(f'Heap handles: {self.get_handles()}')

    def print_node(self, n : int)->None:

        l = self.left(n)
        r = self.right(n)
        
        if l > self.size:
            l_val = None
        else:
            l_val = self.keys[l]

        if r > self.size:
            r_val = None
        else:
            r_val = self.keys[r]

        print(f'Node {n}, value {self.keys[n]}, left node {l}, value {l_val}, right node {r}, value {r_val}, size = {self.size}')

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
        handles_sorted = []
        while self.size > 0:
            key_top, val_top = self.extract_top()
            keys_sorted += [key_top]
            handles_sorted += [val_top]

        self.size = len(keys_sorted)
        self.keys = [None] + keys_sorted
        self.handles = [None] + handles_sorted
        

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
                print(f'Compare parent_idx {n}, value {self.keys[n]}, child_idx {n+1}, value {self.keys[n+1]} is False')
                return False
        return True


class MaxBinaryHeap(BinaryHeap):

    def compare(self, parent_idx : int, child_idx : int)->bool:
        """
        Compares the values of two indexes in the heap
        Returns True is value of parent index is larger than value of child index
        
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
        
        if self.keys[parent_idx] >= self.keys[child_idx]:
            return True
        else:
            return False

class MinBinaryHeap(BinaryHeap):

    def compare(self, parent_idx : int, child_idx : int)->bool:
        """
        Compares the values of two indexes in the heap
        Returns True is value of parent index is larger than value of child index
        
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
        
        if self.keys[parent_idx] <= self.keys[child_idx]:
            return True
        else:
            return False
