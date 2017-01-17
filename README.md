# numpy-heap
NumPy-based min-heap data structure implementation

###Supported operations:

Insert:  overloaded to support insertion of single elements and lists or ndarrays

Extract-min:  can use like extract-max if you multiply inputs by -1


###Other features:
Dynamically resizes array based on number of elements in array.  No need to manually set array sizes

If you have a heap object, h, array can be accessed directly by using h.heap.  This is useful if you need to slice 
chunks of the heap out without affecting heap or if you want to use NumPy functions on the heap.  Remember that the 
heap data only goes from h.heap[:h.size].  The dynamic resize will leave garbage data in the remaining elements of the 
array.


###Usage:
```python
import heap

# Instantiate heap object
h = heap.Heap()

# Insert key 1, 5 into heap
h.insert(1)
h.insert(5)

# Extract minimum value which is at root of heap
h.extract_min()

# Access first element of heap array directly
x = h.heap[0]

```