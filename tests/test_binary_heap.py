import random
import time
import logging

from clrs.algorithms.insertion_sort import *
from clrs.data_structures.binary_heap import MaxBinaryHeap, MinBinaryHeap, MinIndexBinaryHeap

def test_sorting():

    trials = 100
    max_list_len = int(1e3)
    min_list_len = int(1e1)
    max_list_val = max_list_len
    min_list_val = 0

    execution_inputs = []
    execution_outputs = []
    execution_outputs_baseline = []

    for n in range(trials):
        logging.info(f'Trial {n+1} of {trials}')
        list_len = random.randint(min_list_len, max_list_len)
        
        execution_inputs += [list_len]

        random_list = random.sample(range(min_list_val, max_list_val), list_len)

        keys = [(key, handle) for key, handle in zip(random_list, random_list[::-1])]

        t0 = time.time()
        max_heap = MinBinaryHeap(keys=keys, max_size=len(keys))
        max_heap.sort()
       
        execution_outputs += [time.time() - t0]

        assert max_heap.is_sorted()



def test_extract_top():
    keys = [1, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    handles = list(range(len(keys)))
    max_key_idx = keys.index(max(keys))
    print(f'max_key_idx: {max_key_idx}, max_key: {keys[max_key_idx]}, max_handle: {handles[max_key_idx]}')

    keys = [(key, handle) for key, handle in zip(keys, keys)]
    max_heap = MaxBinaryHeap(keys=keys)
    
    top_key = max_heap.extract_top()

    assert top_key == keys[max_key_idx]

    max_heap.print()
    assert max_heap.is_heap()
    logging.info(f'top_key: {top_key}')

'''
def test_increase_key():
    keys = [1, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    handles = list(range(len(keys)))
    
    max_heap = MaxBinaryHeap(keys=keys, handles=handles)
    max_heap.heapify(1, recursive=False, verbose=True)
    max_heap.build_heap()
    print(max_heap.get_keys(), max_heap.size)
    max_heap.print()

    max_heap.increase_key(handle_index=0, new_key=20)
    max_heap.print()
    assert max_heap.is_heap() == True

    expected_keys =  [20, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    expected_handles =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert expected_keys.sort() == max_heap.get_keys().sort()
    assert expected_handles.sort() == max_heap.get_handles().sort()
'''
    
def test_insert():
    
    keys = [1, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    
    keys = [(key, handle) for key, handle in zip(keys, keys)]
    max_heap = MaxBinaryHeap(keys=keys, max_size=len(keys)+1)

   
    max_heap.insert((20, 11))
    max_heap.print()
    assert max_heap.is_heap()

    expected_keys =  [23, 20, 4, 6, 9, 1, 3, 2, 6, 5, 8]
    expected_handles =  [6, 11, 5, 3, 9, 0, 2, 7, 8, 1, 4]

    assert expected_keys.sort() == max_heap.get_keys().sort()
    logging.info(f'heap keys: {max_heap.get_keys()}')

def test_index_change():

    
    keys = [4, 5, 3, 6, 8, 1, 23, 2, 7, 9]
    indexes = [var + 1 for var in range(len(keys))]
        
    keys = [(key, handle) for key, handle in zip(keys, keys)]
    max_heap = MinIndexBinaryHeap(indexes=indexes, keys=keys, max_size=len(keys))

    max_heap.sort()

    logging.info(max_heap.keys)
    logging.info(max_heap.is_sorted())

    max_heap.change(index=1, key=(25,25))

    keys_expected = [None, (1, 1), (2, 2), (3, 3), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (23, 23), (25, 25)]

    max_heap.sort()
    logging.info(max_heap.keys)
    logging.info(keys_expected)
    logging.info(max_heap.is_sorted())

    assert keys_expected == max_heap.keys

    
    