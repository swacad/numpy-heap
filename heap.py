"""
NumPy based implemenation of min-heap data structure.
"""

import numpy as np


class Heap(object):

    def __init__(self, length=2):
        self.heap = np.zeros(length)
        self.heap.fill(np.nan)
        self.size = 0

    def get_parent_idx(self, child_idx):
        if child_idx % 2 == 0:
            parent_idx = int(child_idx / 2 - 1)
        else:
            parent_idx = int(np.floor(child_idx / 2))
        return parent_idx

    def get_parent(self, child_idx):
        parent_idx = self.get_parent_idx(child_idx)
        return self.heap[parent_idx]

    def insert(self, key):
        print('Inserting key ' + str(key))
        if type(key) == list or type(key) == np.ndarray:
            for i in range(len(key) - 1):
                self.insert(key[i])
            key = key[-1]

        if self.heap.shape[0] == self.size + 1:  # Check if heap is at max capacity
            # Resize heap to double the current capacity
            self.heap = np.resize(self.heap, self.heap.shape[0] * 2)
        elif self.heap.shape[0] > self.size * 4:
            self.heap = np.resize(self.heap, int(self.heap.shape[0] / 2) + 1)

        self.heap[self.size] = key
        key_idx = self.size
        parent_idx = self.get_parent_idx(key_idx)

        # Bubble up until heap property is restored
        while self.heap[key_idx] < self.heap[parent_idx]:
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[key_idx]
            self.heap[key_idx] = temp
            key_idx = parent_idx
            parent_idx = self.get_parent_idx(key_idx)

        self.size += 1

    def get_left_child_idx(self, parent_idx):
        return 2 * parent_idx + 1

    def get_right_child_idx(self, parent_idx):
        return 2 * parent_idx + 2

    def get_left_child(self, parent_idx):
        left_child = self.heap[self.get_left_child_idx(parent_idx)]
        return left_child

    def get_right_child(self, parent_idx):
        right_child = self.heap[self.get_right_child_idx(parent_idx)]
        return right_child

    def get_children_idx(self, parent_idx):
        return 2 * parent_idx + 1, 2 * parent_idx + 2

    def get_children(self, parent_idx):
        child_1_idx, child_2_idx = self.get_parent_idx(parent_idx)
        return self.heap[child_1_idx], self.heap[child_2_idx]

    def extract_min(self):
        root = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap[self.size] = np.nan

        key_idx = 0
        c1_idx, c2_idx = self.get_children_idx(key_idx)

        # Bubble down root until heap property restored
        while self.heap[key_idx] > self.heap[c1_idx] or self.heap[key_idx] > self.heap[c2_idx]:
            if self.heap[c1_idx] < self.heap[c2_idx]:
                smaller_child_idx = c1_idx
            else:
                smaller_child_idx = c2_idx
            temp = self.heap[smaller_child_idx]
            self.heap[smaller_child_idx] = self.heap[key_idx]
            self.heap[key_idx] = temp

            key_idx = smaller_child_idx
            c1_idx, c2_idx = self.get_children_idx(key_idx)
            if c1_idx >= self.size or c2_idx >= self.size:
                break

        return root

