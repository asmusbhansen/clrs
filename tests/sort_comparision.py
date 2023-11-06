import random
import matplotlib.pyplot as plt
import time
import logging
import copy

from clrs.algorithms.insertion_sort import *
from clrs.algorithms.quicksort import *
from clrs.data_structures.binary_heap import MaxBinaryHeap, MinBinaryHeap

def sort_comparision():

    trials = 100
    max_list_len = 2000
    min_list_len = int(1e1)
    max_list_val = max_list_len
    min_list_val = 0

    execution_inputs = []
    output_heapsort = []
    output_insertion_sort = []
    output_quick_sort = []
    output_random_quick_sort = []

    for n in range(trials):
        print(f'Trial {n+1} of {trials}')
        list_len = random.randint(min_list_len, max_list_len)
        
        execution_inputs += [list_len]

        random_list = random.sample(range(min_list_val, max_list_val), list_len)
        copy.deepcopy(random_list)

        t0 = time.time()
        max_heap = MinBinaryHeap(keys=copy.deepcopy(random_list), handles=copy.deepcopy(random_list))
        max_heap.sort()
        #print(f'Max Heap Keys: {max_heap.get_keys()}')
        #print(f'Max Heap Handles: {max_heap.get_handles()}')

        output_heapsort += [time.time() - t0]

        t0 = time.time()
        quicksort(copy.deepcopy(random_list), method='random')
        output_random_quick_sort += [time.time() - t0]

        t0 = time.time()
        quicksort(copy.deepcopy(random_list), method='last')
        output_quick_sort += [time.time() - t0]

        t0 = time.time()
        insertion_sort(copy.deepcopy(random_list))
        output_insertion_sort += [time.time() - t0]

    plt.figure()
    plt.scatter(execution_inputs, output_heapsort, label='Heap Sort', alpha=1)
    plt.scatter(execution_inputs, output_quick_sort, label='Quicksort', alpha=1)
    plt.scatter(execution_inputs, output_random_quick_sort, label='Random Quicksort', alpha=1)
    plt.scatter(execution_inputs, output_insertion_sort, label='Insertion Sort', alpha=1)
    plt.title('Simulation output')
    plt.xlabel('Array length [Samples]')
    plt.ylabel('Execution time [s]')
    plt.legend()
    plt.savefig('simulation_output/sort_comparision/list_sorting.png')

    plt.close()

sort_comparision()