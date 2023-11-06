from typing import Any, Dict, List, Optional, Union
import copy 

BLACK = False
RED = True

class ColouredNode:

    left = None
    right = None

    def __init__(self, key : Any = None, value : int = None, size : int = 1, color : bool = RED) -> None:

        self.key = key
        self.value = value
        self.size = size
        self.color = color

    def print(self):

        string = self.print_string()

        if self.left is not None:
            string += f'. Left - {self.left.print_string()}'

        if self.right is not None:
            string += f'. Right - {self.right.print_string()}'

        print(string)

    def print_string(self):
        return (f'Node key: {self.key}, value: {self.value}, color: {self.color}')

class RedBlackBinarySearchTree:

    root = None
    compares = 0

    def size(self) -> int:
        return self.size_(self.root)

    def size_(self, node : ColouredNode) -> int:

        if node is None:
            return 0
        else:
            return node.size

    def flip_colors(self, node : ColouredNode) -> ColouredNode:

        print(f'Flipping color on node : {node.print_string()}')

        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

        return node

    def is_red(self, node : ColouredNode) -> bool:
        
        if node is None:
            return False

        return node.color

    def rotate_left(self, node : ColouredNode) -> ColouredNode:

        print(f'Rotating node : {node.print_string()} left')

        node_high = copy.deepcopy(node.right)

        # Rotate
        node.right = node_high.left
        node_high.left = node

        # Switch colors
        node_high.color = node.color
        node.color = RED
        
        # Adjust size
        node_high.size = node.size
        node.size = 1 + self.size_(node.left) + self.size_(node.right)

        return node_high

    def rotate_right(self, node : ColouredNode) -> ColouredNode:

        print(f'Rotating node : {node.print_string()} right')

        node_low = copy.deepcopy(node.left)

        # Rotate
        node.left = node_low.right
        node_low.right = node

        # Switch colors
        node_low.color = node.color
        node.color = RED
        
        # Adjust size
        node_low.size = node.size
        node.size = 1 + self.size_(node.left) + self.size_(node.right)

        return node_low

    def compare(self, key_1 : Any, key_2 : Any) -> int:

        if key_1 > key_2:
            self.compares += 1
            return -1
        elif key_1 < key_2:
            self.compares += 2
            return 1
        else:
            self.compares += 2
            return 0


    def put(self, key : Any, value : int) -> ColouredNode:

        # Reset compares
        self.compares = 0

        self.root = self.put_(node = self.root, key = key, value = value)
        self.root.color = BLACK

    def put_(self, node : ColouredNode, key : Any, value : int) -> ColouredNode:

        print(f'put_ - key: {key}, value: {value}')

        if node is None:
            return ColouredNode(key = key, value = value)

        compared = self.compare(key_1=node.key, key_2=key)

        if compared < 0:
            node.left = self.put_(node = node.left, key = key, value = value)
            print(f'Put left')
        elif compared > 0:
            node.right = self.put_(node = node.right, key = key, value = value)
            print(f'Put right')
        # If the key is a match, overwrite value
        else:
            node.value = value

        # If the right node is red and the left node is black - Perform a left rotation
        if self.is_red(node.right) and self.is_red(node.left) == False:
            node = self.rotate_left(node)

        # If the left node is red and it's child left node is red(Two succesive red nodes) - Perform a right rotation
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)

        # If both child nodes are red - Perform color flip
        if self.is_red(node.left) and self.is_red(node.right):
            node = self.flip_colors(node)

        node.size = self.size_(node.left) + self.size_(node.right) + 1

        # Return the node
        return node

    def get(self, key : Any) -> ColouredNode:

        # Reset compares
        self.compares = 0

        return self.get_(node = self.root, key = key)

    def get_(self, node : ColouredNode, key : Any) -> Any:

        if node is None:
            return None

        compared = self.compare(key_1=node.key, key_2=key)

        if compared < 0:
            return self.get_(node = node.left, key = key)
        elif compared > 0:
            return self.get_(node = node.right, key = key)
        # If the key is a match, overwrite value
        else:
            return node.value


node = ColouredNode(key='hello', value=1)
node.print()

bst = RedBlackBinarySearchTree()

bst.put(key='hello', value=1)
bst.put(key='b', value=2)
bst.put(key='a', value=3)
    
bst.root.print()


bst.put(key='k', value=3)

import random

tests = 100

test_bst = RedBlackBinarySearchTree()
test_dict = {}

for n in range(tests):

    key = random.randint(0, tests)#random.choice(string.ascii_letters)
    value = random.randint(0, tests)
    print(key, value)
    test_dict[key] = value

    test_bst.put(key=key, value=value)

    print(f'Put key: {key}, value: {value}, BST size: {test_bst.size()}')

for key, value_true in test_dict.items():

    value = test_bst.get(key)
    print(f'key: {key}, value_true: {value_true}, value: {value}, BST size: {test_bst.size()}, compares: {test_bst.compares}')

    assert value == value_true



num_tests = 1000
max_entries = 100


compares_result = []
bst_size = []



for n in range(num_tests):
    print(f'Test {n} of {num_tests}')
    entries = random.randint(1, max_entries+1)

    test_bst = RedBlackBinarySearchTree()

    for m in range(entries):

        key = random.randint(0, entries)
        value = random.randint(0, entries)

        test_bst.put(key=key, value=value)

        compares_result += [test_bst.compares]
        bst_size += [test_bst.size()]



import pandas as pd

import matplotlib.pyplot as plt

results = pd.DataFrame({'size':bst_size, 'compares':compares_result})

compares_average_result = []
size_average = []

for size in results['size'].unique():

    size_average += [size]

    compares_average_result += [results[results['size'] == size]['compares'].mean()]

print(results)

plt.figure()
plt.scatter(bst_size, compares_result, alpha=0.2)
plt.plot(size_average, compares_average_result, label='Compares average', alpha=1, color='C1')
plt.title('Simulation output')
plt.xlabel('BST Size [Nodes]')
plt.ylabel('Compares')
plt.legend()
plt.savefig('simulation_output/red_black_binary_search_tree/compares.png')

plt.close()
