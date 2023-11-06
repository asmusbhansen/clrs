import random

def quicksort(keys, p : int=-1, r : int=-1, method : str='last')->None:
    """
    Recursive implementation of the quicksort algorithm
    
    Parameters
    ----------
    keys : list
        Keys to be sorted
    p : int
        Low index of the subset of keys to be sorted
    r : int
        High index of the subset of keys to be sorted
    method : string
        specifies the method to find the pivot 
    
    Returns
    -------
    None

    """

    if r == -1:
        r = len(keys) - 1
    if p == -1:
        p = 0

    if p < r:

        q = partition(keys, p=p, r=r, method=method)
        quicksort(keys, p=p, r=q-1, method=method)
        quicksort(keys, p=q+1, r=r, method=method)

def partition(keys, p : int, r : int, method : str='last')->int:
    """
    Partitions the keys in two subarray around a pivot
    
    Parameters
    ----------
    keys : list
        Keys to be sorted
    p : int
        Low index of the subset of keys to be sorted
    r : int
        High index of the subset of keys to be sorted
    method : string
        specifies the method to find the pivot 
    
    Returns
    -------
    int : 
        The pivot index used to partition the subarray

    """

    if method == 'random':
        pivot = random.randint(p, r)
    else:
        pivot = r  
    
    x = keys[pivot]

    i = p - 1

    for j in range(p, r):
        
        if keys[j] <= x:

            i += 1
            
            switch(keys, i, j)

    switch(keys, i+1, r)

    return i+1

def switch(keys, idx_1, idx_2):

    val = keys[idx_1]
    keys[idx_1] = keys[idx_2]
    keys[idx_2] = val

'''


keys = [2,8,7,1,3,5,6,4]
keys = random.sample(range(0, 100000), 100000)

print(f'Sort input: {keys}')

quicksort(keys=keys, method='random')

print(f'Sort output: {keys}')
'''