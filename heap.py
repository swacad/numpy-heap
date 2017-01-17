"""
Array based implementation of min-heaps to solve median maintenance problem in O(log(i)) time.
Where X[i] is the ith number to be given in iteration and the median must be computed for each new ith number.
Test numbers are Median.txt
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

    def get_children_idx(self, parent_idx):
        return 2 * (parent_idx + 1) - 1, 2 * (parent_idx + 1)

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


def median_maintenance():
    file = 'Median.txt'

    X = list()
    with open(file) as f:
        for line in f:
            X.append(int(line))

    h_lo = Heap()

    h_hi = Heap()

    medians = np.zeros(len(X), dtype=int)

    if X[0] < X[1]:
        h_lo.insert(X[0] * -1)
        h_hi.insert(X[1])
    else:
        h_lo.insert(X[1] * -1)
        h_hi.insert(X[0])

    medians[0] = X[0]
    medians[1] = X[1]

    for i in range(2, len(X)):
        if i < 20:
            print('i = ' + str(i))
            print('h_lo = ' + str(h_lo.heap))
            print('h_lo.size = ' + str(h_lo.size))
            print('h_hi = ' + str(h_hi.heap))
            print('h_hi.size = ' + str(h_hi.size))

        if abs(h_lo.size - h_hi.size) > 1:
            print('IMBALANCED HEAPS!!!')

        if X[i] <= h_lo.heap[0] * -1:
            h_lo.insert(X[i] * -1)
        else:
            h_hi.insert(X[i])

        if h_lo.size - h_hi.size > 1:
            key = h_lo.extract_min()
            key *= -1
            h_hi.insert(key)
            medians[i] = h_lo.heap[0] * -1
        elif h_hi.size - h_lo.size > 1:
            key = h_hi.extract_min()
            h_lo.insert(key * -1)
            medians[i] = h_lo.heap[0] * -1
        else:
            if h_lo.size > h_hi.size:
                medians[i] = h_lo.heap[0] * -1
            elif h_hi.size > h_lo.size:
                medians[i] = h_hi.heap[0]
            else:  # size of both h_lo and h_hi heaps are equal
                medians[i] = h_lo.heap[0] * -1

    print(h_lo.heap)
    print(h_hi.heap)

    answer = np.sum(medians) % 10000
    print('answer = ' + str(answer))

    for i in range(medians.shape[0]):
        print(medians[i])


if __name__ == '__main__':
    # median_maintenance()
    # h = np.array([4, 4, 8, 9, 4, 12, 9, 11, 13, np.nan, np.nan, np.nan])
    a = [4, 4, 8, 9, 4, 12, 9, 11, 13]
    h = Heap()
    h.insert(a)
    print(h.heap)
    h.insert([7, 10, 5])
    print(h.heap)
