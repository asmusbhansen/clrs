import random
import time
import logging

from clrs.algorithms.insertion_sort import *
from clrs.data_structures.binary_heap import MaxBinaryHeap, MinBinaryHeap

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

        t0 = time.time()
        max_heap = MinBinaryHeap(keys=random_list, handles=random_list)
        max_heap.sort()
       
        execution_outputs += [time.time() - t0]

        assert max_heap.is_sorted()



def test_extract_top():
    keys = [1, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    handles = list(range(len(keys)))
    max_key_idx = keys.index(max(keys))
    print(f'max_key_idx: {max_key_idx}, max_key: {keys[max_key_idx]}, max_handle: {handles[max_key_idx]}')
    max_heap = MaxBinaryHeap(keys=keys, handles=handles)
    max_heap.heapify(1, recursive=False, verbose=True)
    max_heap.build_heap()
    print(max_heap.get_keys(), max_heap.size)
    max_heap.print()

    top_key, top_handle = max_heap.extract_top()
    print(f'top_handle: {top_handle}, top_key: {top_key}')
    assert top_key == keys[max_key_idx]
    assert top_handle == handles[max_key_idx]
    max_heap.print()
    assert max_heap.is_heap()

def test_increase_key():
    keys = [1, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    handles = list(range(len(keys)))
    max_heap = MaxBinaryHeap(keys=keys, handles=handles)
    max_heap.heapify(1, recursive=False, verbose=True)
    max_heap.build_heap()
    print(max_heap.get_keys(), max_heap.size)
    max_heap.print()

    max_heap.increase_key(handle=0, new_key=20)
    max_heap.print()
    assert max_heap.is_heap()

    expected_keys =  [20, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    expected_handles =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert expected_keys.sort() == max_heap.get_keys().sort()
    assert expected_handles.sort() == max_heap.get_handles().sort()

def test_insert():
    keys = [1, 5, 3, 6, 8, 4, 23, 2, 6, 9]
    handles = list(range(len(keys)))
    max_heap = MaxBinaryHeap(keys=keys, handles=handles)
    max_heap.heapify(1, recursive=False, verbose=True)
    max_heap.build_heap()
    print(max_heap.get_keys(), max_heap.size)
    max_heap.print()

    max_heap.insert(handle=11, key=20)
    max_heap.print()
    assert max_heap.is_heap()

    expected_keys =  [23, 20, 4, 6, 9, 1, 3, 2, 6, 5, 8]
    expected_handles =  [6, 11, 5, 3, 9, 0, 2, 7, 8, 1, 4]

    assert expected_keys.sort() == max_heap.get_keys().sort()
    assert expected_handles.sort() == max_heap.get_handles().sort()

#test_insert()